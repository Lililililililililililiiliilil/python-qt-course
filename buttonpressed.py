from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Button")

        self.setGeometry(300, 300, 360, 144)

        self.button = QPushButton("Click me!", self)
        self.textLabel = QLabel()
        self.textLabel.setText("1")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.textLabel)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.show()

        @Slot()
        def button_pressed():
            self.textLabel.setText("Нажата")

        @Slot()
        def button_released():
            self.textLabel.setText("Отпущена")

        self.button.pressed.connect(button_pressed)
        self.button.released.connect(button_released)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
