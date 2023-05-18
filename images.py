from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QFileDialog, QLabel, QScrollArea, QWidget, \
    QVBoxLayout, QDialog
from PySide6.QtGui import QIcon, QPixmap, QAction
from PySide6.QtWidgets import QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_list = QListWidget(self)
        self.setCentralWidget(self.image_list)

        self.add_image_action = QAction(QIcon("icons/add.png"), "Добавить картинку", self)
        self.add_image_action.triggered.connect(self.add_image)
        self.toolbar = self.addToolBar("Добавить картинку")
        self.toolbar.addAction(self.add_image_action)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QListWidget {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
            }
            QListWidget::item {
                padding: 10px;
            }
            """)

        self.image_list.itemDoubleClicked.connect(self.view_image)

    def add_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *jpeg)")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]

            pixmap = QPixmap(file_path)
            item = QListWidgetItem(QIcon(pixmap), file_path.split("/")[-1])
            self.image_list.addItem(item)

    def view_image(self, item):
        dialog = QDialog(self)
        dialog.setWindowTitle(item.text())

        label = QLabel(dialog)
        label.setPixmap(item.icon().pixmap(400, 400))

        layout = QVBoxLayout(dialog)
        layout.addWidget(label)

        dialog.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
