from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QDialog, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QListWidget, QListWidgetItem
from datetime import datetime


class Note:
    def __init__(self, text, date):
        self.text = text
        self.date = date


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")
        self.notes = []
        self.list_widget = QListWidget(self)
        self.setCentralWidget(self.list_widget)
        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Файл")
        add_action = QAction("Добавить заметку", self)
        add_action.triggered.connect(self.show_dialog)
        file_menu.addAction(add_action)

    def show_dialog(self):
        dialog = AddNoteDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            note = Note(dialog.text_edit.text(), datetime.now())
            self.notes.append(note)
            item = QListWidgetItem(note.text)
            item.setData(1, note.date)
            self.list_widget.addItem(item)


class AddNoteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить заметку")
        self.text_edit = QLineEdit(self)
        self.ok_button = QPushButton("ОК", self)
        self.ok_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Текст заметки:"))
        layout.addWidget(self.text_edit)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    widget = MainWidget()
    widget.show()
    app.exec_()
