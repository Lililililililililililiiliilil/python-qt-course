from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Calculator")

        self.setGeometry(300, 300, 360, 144)

        self.plus = QPushButton("+", self)
        self.minus = QPushButton("-", self)
        self.multiply = QPushButton("*", self)
        self.divide = QPushButton("÷", self)
        self.pow = QPushButton("^", self)

        self.first_number = QLineEdit()
        self.second_number = QLineEdit()

        self.answer = QLabel()
        self.answer.setText("--------")

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.first_number, 0, 0)
        self.gridLayout.addWidget(self.second_number, 0, 1)
        self.gridLayout.addWidget(self.plus, 1, 0)
        self.gridLayout.addWidget(self.minus, 1, 1)
        self.gridLayout.addWidget(self.multiply, 2, 0)
        self.gridLayout.addWidget(self.divide, 2, 1)
        self.gridLayout.addWidget(self.pow, 3, 0)
        self.gridLayout.addWidget(self.answer, 3, 1)

        self.container = QWidget()
        self.container.setLayout(self.gridLayout)
        self.setCentralWidget(self.container)
        self.show()

        @Slot()
        def plus():
            ans = self.first_number.text() + " + " + self.second_number.text() + " = " + str(
                int(self.first_number.text()) + int(self.second_number.text()))
            self.answer.setText(ans)

        @Slot()
        def minus():
            ans = self.first_number.text() + " - " + self.second_number.text() + " = " + str(
                int(self.first_number.text()) - int(self.second_number.text()))
            self.answer.setText(ans)

        @Slot()
        def multiply():
            ans = self.first_number.text() + " * " + self.second_number.text() + " = " + str(
                int(self.first_number.text()) * int(self.second_number.text()))
            self.answer.setText(ans)

        @Slot()
        def divide():
            try:
                ans = self.first_number.text() + " ÷ " + self.second_number.text() + " = " + str(
                    int(self.first_number.text()) / int(self.second_number.text()))
                self.answer.setText(ans)
            except ZeroDivisionError:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Zero division!")
                msg.exec()

        @Slot()
        def pow():
            ans = self.first_number.text() + " <sup> " + self.second_number.text() + "</sup> = " + str(
                int(self.first_number.text()) ** int(self.second_number.text()))
            self.answer.setText(ans)

        self.plus.clicked.connect(plus)
        self.minus.clicked.connect(minus)
        self.multiply.clicked.connect(multiply)
        self.divide.clicked.connect(divide)
        self.pow.clicked.connect(pow)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
