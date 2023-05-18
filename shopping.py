from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        self.setMinimumWidth(500)
        self.setMinimumHeight(200)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        products = [
            {'name': 'Пиво Балтика 3', 'price': 45},
            {'name': 'Сухарики', 'price': 25},
            {'name': 'Чипсы', 'price': 56},
            {'name': 'Жвачка', 'price': 13},
            {'name': 'Молоко', 'price': 59},
        ]
        self.product_widgets = []
        for product in products:
            checkbox = QCheckBox(product['name'])
            checkbox.setChecked(False)
            checkbox.stateChanged.connect(self.update_total_price)

            price_label = QLabel(str(product['price']) + "₽")

            quantity_widget = QDoubleSpinBox()
            quantity_widget.setMinimum(0)
            quantity_widget.setMaximum(10)
            quantity_widget.setValue(0)
            quantity_widget.valueChanged.connect(self.update_total_price)

            product_widget = QWidget()
            product_layout = QHBoxLayout()
            product_widget.setLayout(product_layout)
            product_layout.addWidget(checkbox)
            product_layout.addWidget(price_label)
            product_layout.addWidget(quantity_widget)

            main_layout.addWidget(product_widget)

            self.product_widgets.append({
                'name': product['name'],
                'price': product['price'],
                'checkbox': checkbox,
                'quantity_widget': quantity_widget,
            })

        self.total_price_label = QLabel('Сумма: 0 ₽')
        main_layout.addWidget(self.total_price_label)
        self.show()

    def update_total_price(self):
        total_price = 0.0
        for product_widget in self.product_widgets:
            if product_widget['checkbox'].isChecked():
                quantity = product_widget['quantity_widget'].value()
                price = product_widget['price']
                total_price += quantity * price

        self.total_price_label.setText('Сумма: {:.2f} ₽'.format(total_price))


App = QApplication(sys.argv)

window = MainWindow()

sys.exit(App.exec())
