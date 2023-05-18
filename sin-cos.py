from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPainter, QPen, QColor, QPainterPath
from PySide6.QtCore import Qt, QPointF, QRectF, QSizeF, QTimer, QLineF
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = QGraphicsView(self)
        self.setCentralWidget(self.view)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        self.pen_sin = QPen(QColor("red"))
        self.pen_cos = QPen(QColor("blue"))
        self.pen_sin.setWidth(2)
        self.pen_cos.setWidth(2)
        self.x_min = -math.pi
        self.x_max = math.pi
        self.y_min = -1
        self.y_max = 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_graphs)
        self.timer.start(50)

    def update_graphs(self):
        self.scene.clear()

        x_axis = self.scene.addLine(QLineF(-math.pi, 0, math.pi, 0), QPen(Qt.black))
        y_axis = self.scene.addLine(QLineF(0, -1, 0, 1), QPen(Qt.black))

        sin_path = QPainterPath()
        for i in range(30):
            x = self.x_min + (i / 29) * (self.x_max - self.x_min)
            y = math.sin(x)
            x_pixel = (x - self.x_min) / (self.x_max - self.x_min) * self.view.width()
            y_pixel = (y - self.y_min) / (self.y_max - self.y_min) * self.view.height()
            if i == 0:
                sin_path.moveTo(x_pixel, y_pixel)
            else:
                sin_path.lineTo(x_pixel, y_pixel)
        self.scene.addPath(sin_path, self.pen_sin)

        cos_path = QPainterPath()
        for i in range(30):
            x = self.x_min + (i / 29) * (self.x_max - self.x_min)
            y = math.cos(x)
            x_pixel = (x - self.x_min) / (self.x_max - self.x_min) * self.view.width()
            y_pixel = (y - self.y_min) / (self.y_max - self.y_min) * self.view.height()
            if i == 0:
                cos_path.moveTo(x_pixel, y_pixel)
            else:
                cos_path.lineTo(x_pixel, y_pixel)
        self.scene.addPath(cos_path, self.pen_cos)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
