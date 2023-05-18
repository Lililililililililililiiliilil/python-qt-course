import book
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont

books = [book.Book("Война и Мир", "Л.Н. Толстой", 1000), book.Book("Преступление и наказание", "Ф.М. Достоевский", 548),
         book.Book("Мастер и Маргарита", "М.А. Булгаков", 450)]
bookText = """"""
for book in books:
    bookText += str(book) + "\n"

app = QApplication([])
window = QMainWindow()
label = QLabel()
linkLabel = QLabel()
booksLabel = QLabel()
layout = QVBoxLayout()

txt = '''Вам, проживающим за оргией оргию,имеющим ванную и теплый клозет! Как вам не стыдно о представленных к 
Георгию вычитывать из столбцов газет?! '''
label.setText(txt)
label.setWordWrap(True)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

label.setFont(QFont("Helvetica [Cronyx]", 12, italic=True))

link = '''<a href=\"http://ivt.uniyar.ac.ru/\">Click Here!</a>'''
linkLabel.setText(link)
linkLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
linkLabel.setFont(QFont("Helvetica [Cronyx]", 24))
linkLabel.setOpenExternalLinks(True)

booksLabel.setText(bookText)
booksLabel.setWordWrap(True)

layout.addWidget(label)
layout.addWidget(booksLabel)
layout.addWidget(linkLabel, alignment=Qt.AlignmentFlag.AlignBottom)

container = QWidget()
container.setLayout(layout)
window.setFixedSize(QSize(400, 300))
window.setCentralWidget(container)
window.show()

app.exec()
