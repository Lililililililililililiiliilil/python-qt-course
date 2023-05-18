from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog, QCheckBox, QMessageBox, \
    QVBoxLayout, QWidget


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главный экран")
        vbox = QVBoxLayout()
        self.main_m = QWidget()
        self.button = QPushButton("Открыть диалог", self)
        self.button.clicked.connect(self.open_dialog)
        self.label = QLabel()
        self.label.setText("----")
        vbox.addWidget(self.button)
        vbox.addWidget(self.label)

        self.container = QWidget()
        self.container.setLayout(vbox)
        self.setCentralWidget(self.container)
        self.show()

    def open_dialog(self):
        dialog = Dialog(self)
        if dialog.exec_() == QDialog.Accepted:

            if dialog.checkbox.isChecked():
                self.label.setText("Чекбокс выбран")
            else:
                self.label.setText("Чекбокс не выбран")


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Диалоговое окно")
        self.checkbox = QCheckBox("Соглашаюсь", self)
        self.ok_button = QPushButton("ОК", self)
        self.ok_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    app.exec_()
