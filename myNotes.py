import sys
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListView, \
    QMessageBox


class Note:
    count = 0

    def __init__(self, text):
        self.id = Note.count + 1
        self.text = text
        Note.count += 1

    def getId(self):
        return self.id


class NoteListModel(QAbstractListModel):
    def __init__(self, notes=None):
        super().__init__()
        self._notes = notes or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._notes)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._notes[index.row()]

    def addNote(self, note):
        if not note.text.strip():
            raise Exception("Заметка не может быть пустой!")

        if any(c for c in note.text if c.isspace() and not c.isascii()):
            raise Exception("Заметка содержит недопустимые символы!")
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._notes.append(str(note.getId()) + " - " + note.text)
        self.endInsertRows()

    def removeNote(self, index):
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self._notes[index.row()]
        self.endRemoveRows()

    def getNoteId(self, index):
        return str(id(self._notes[index.row()]))


class NoteWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.note_list_model = NoteListModel()

        self.note_input = QLineEdit()
        self.note_input.setFixedSize(150, 300)
        self.add_button = QPushButton("Добавить")
        self.note_list_view = QListView()

        self.note_list_view.setModel(self.note_list_model)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.note_input)
        input_layout.addWidget(self.add_button)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.note_list_view)
        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

        self.add_button.clicked.connect(self.addNote)
        self.note_list_view.clicked.connect(self.removeNote)

    def addNote(self):
        note = Note(self.note_input.text())
        try:
            self.note_list_model.addNote(note)
        except Exception as e:
            QMessageBox.warning(None, "Ошибка", str(e))
        self.note_input.clear()

    def removeNote(self, index):
        self.note_list_model.removeNote(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = NoteWidget()
    widget.show()
    with open("style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    sys.exit(app.exec())
