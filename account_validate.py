import re

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ваш аккаунт")
        self.setMinimumWidth(200)
        self.setMinimumHeight(500)

        self.form = QFormLayout()

        self.form.setVerticalSpacing(10)

        self.labelName = QLabel("Фамилия")
        self.labelSurname = QLabel("Имя")
        self.labelSecondName = QLabel("Отчество")
        self.labelMail = QLabel("Email")
        self.labelMobile = QLabel("Номер телефона")
        self.labelHobbies = QLabel("Интересующие темы")
        self.labelData = QLabel("Вы даёте согласие на обработку персональных данных ")
        self.labelMailing = QLabel("Подпишитесь на нашу рассылку ")

        self.nameEdit = QLineEdit()
        self.surnameEdit = QLineEdit()
        self.secondNameEdit = QLineEdit()
        self.mailEdit = QLineEdit()
        self.mobileEdit = QLineEdit()

        self.approveButton = QPushButton("Подтвердить")

        self.collectData = QCheckBox()
        self.mailing = QCheckBox()

        self.hobbies = QListWidget()
        # hobbies.setFixedSize(300, 100)
        self.hobbies.addItems(["Спорт", "Видеоигры", "Фотография", "Фильмы", "Книги"])
        self.hobbies.setSelectionMode(QAbstractItemView.MultiSelection)

        self.form.addRow(self.labelName, self.nameEdit)
        self.form.addRow(self.labelSurname, self.surnameEdit)
        self.form.addRow(self.labelSecondName, self.secondNameEdit)
        self.form.addRow(self.labelMail, self.mailEdit)
        self.form.addRow(self.labelMobile, self.mobileEdit)
        self.form.addRow(self.labelHobbies, self.hobbies)
        self.form.addRow(self.labelData, self.collectData)
        self.form.addRow(self.labelMailing, self.mailing)
        self.form.addRow(self.approveButton)

        self.approveButton.clicked.connect(self.check_input)

        self.setLayout(self.form)
        self.show()

    def check_input(self):

        firstname = self.labelName.text()
        lastname = self.labelSurname.text()
        secondName = self.labelSecondName.text()
        mail = self.labelMail.text()
        mobile = self.labelMobile.text()
        rule = re.compile(r'^(?:\+?7)?[07]\d{9,13}$')
        hobbiesList = [item.text() for item in self.hobbies.selectedItems()]
        data = self.collectData.isChecked()

        QMessageBox.warning(self, "введено", firstname)

        if not firstname or not lastname or not secondName:
            QMessageBox.warning(self, "Ошибка", "Введите ФИО!")
            return

        if not mail:
            QMessageBox.warning(self, "Ошибка", "Введите адрес электронной почты!")
            return

        if rule.search(mobile):
            QMessageBox.warning(self, "Ошибка", "Некоректный номер телефона!")
            return

        if not mobile:
            QMessageBox.warning(self, "Ошибка", "Введите номер телефона!")
            return

        if not hobbiesList:
            QMessageBox.warning(self, "Ошибка", "Добавьте хотя бы одну интересующую тему!")
            return

        if not data:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, подтвердите согласие на обработку персональных данных")
            return


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
