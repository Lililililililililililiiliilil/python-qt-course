from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QWidget):
    @Slot()
    def handle_radio_buttons(self):
        print(self.group.checkedId())

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Времена года")
        self.setMinimumWidth(500)
        self.setMinimumHeight(200)

        layout = QVBoxLayout()
        self.radioWinter = QRadioButton('Зима')
        self.radioWinter.setChecked(True)
        self.radioSpring = QRadioButton('Весна')
        self.radioSummer = QRadioButton('Лето')
        self.radioAutumn = QRadioButton('Осень')

        self.seasonLabel = QLabel()
        self.seasonLabel.setWordWrap(True)
        self.seasonLabel.setText(
            "Зима — одно из четырёх времён года, самый холодный и тёмный период времени между осенью и весной.")

        self.group = QButtonGroup()
        self.group.addButton(self.radioWinter, id=1)
        self.group.addButton(self.radioSpring, id=2)
        self.group.addButton(self.radioSummer, id=3)
        self.group.addButton(self.radioAutumn, id=4)
        layout.addWidget(self.radioWinter)
        layout.addWidget(self.radioSpring)
        layout.addWidget(self.radioSummer)
        layout.addWidget(self.radioAutumn)
        layout.addWidget(self.seasonLabel)
        self.setLayout(layout)
        self.show()

        @Slot()
        def winter():
            self.seasonLabel.setText(
                "Зима — одно из четырёх времён года, самый холодный и тёмный период времени между осенью и весной.")

        @Slot()
        def spring():
            self.seasonLabel.setText(
                "Весна – время пробуждения природы, и людей, которые являются ее частью.")

        @Slot()
        def summer():
            self.seasonLabel.setText(
                "Лето — одно из четырёх времён года, между весной и осенью, характеризующееся наиболее высокой "
                "температурой окружающей среды")

        @Slot()
        def autumn():
            self.seasonLabel.setText(
                "Следом за летом осень идёт, Жёлтые песни ей ветер поёт. Красную пoд ноги стелет листву,"
                "Белой снежинкой летит в синеву.")

        self.radioWinter.clicked.connect(winter)
        self.radioSpring.clicked.connect(spring)
        self.radioSummer.clicked.connect(summer)
        self.radioAutumn.clicked.connect(autumn)


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
