from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расписание ПИЭ32")
        self.setMinimumWidth(1000)
        self.setMinimumHeight(500)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setRowCount(6)

        self.table.setStyleSheet("QTableView { gridline-color: green; }")

        self.table.setRowHeight(0, 100)
        self.table.setRowHeight(1, 100)
        self.table.setRowHeight(2, 100)
        self.table.setRowHeight(3, 100)
        self.table.setRowHeight(4, 100)
        self.table.setRowHeight(5, 100)

        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 100)

        self.table.setHorizontalHeaderLabels(['Понедельник', 'Вторник', "Среда", "Четверг", "Пятница"])
        self.table.setVerticalHeaderLabels(['1 пара', "2 пара", "", "3 пара", "4 пара", "5 пара"])
        self.table.setShowGrid(True)
        self.table.setItem(0, 0, QTableWidgetItem("Разработка программных приложений - 210"))
        self.table.setItem(1, 0, QTableWidgetItem("Разработка программных приложений - 210"))
        self.table.setItem(2, 0, QTableWidgetItem("Управленческий учет и контроллинг - 210"))
        self.table.setItem(3, 0, QTableWidgetItem("Управленческий учет и контроллинг - 210"))
        self.table.setSpan(4, 0, 4, 1)
        self.table.setItem(4, 0, QTableWidgetItem("Курс по выбору - Huawei"))
        self.table.setItem(0, 1, QTableWidgetItem("Алгоритмы обработки информации - 312"))
        self.table.setItem(1, 1, QTableWidgetItem("Разработка программных приложений - 210"))
        self.table.setSpan(1, 1, 2, 1)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.show()


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
