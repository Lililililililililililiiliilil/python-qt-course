from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Counter")

        self.setGeometry(300, 300, 360, 144)

        self.add_button = QPushButton("Add", self)
        self.clear_button = QPushButton("Clear", self)
        self.textLabel = QLabel()
        self.textLabel.setText("0")

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.add_button, 0, 0)
        self.gridLayout.addWidget(self.clear_button, 0, 1)
        self.gridLayout.addWidget(self.textLabel, 1, 0)
        self.container = QWidget()
        self.container.setLayout(self.gridLayout)
        self.setCentralWidget(self.container)
        self.show()

        @Slot()
        def add_point():
            self.textLabel.setText(str(int(self.textLabel.text()) + 1))

        @Slot()
        def clear_text():
            self.textLabel.setText("0")

        self.add_button.clicked.connect(add_point)
        self.clear_button.clicked.connect(clear_text)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
