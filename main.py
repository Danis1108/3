import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import QRect, Qt
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Circle Example'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.button = QPushButton('Создать круг', self)
        self.button.setGeometry(250, 390, 100, 50)
        self.button.clicked.connect(self.generate_circle)

    def generate_circle(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        qp.setBrush(QBrush(color, Qt.SolidPattern))
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width - diameter)
        y = random.randint(0, self.height - diameter)
        qp.drawEllipse(x, y, diameter, diameter)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
