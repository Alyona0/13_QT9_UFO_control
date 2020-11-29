import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtWidgets import (QApplication, QWidget)


class UFO_tracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Управление НЛО')
        self.x = 0
        self.y = 0
        self.img_r = 40 # учет размера картинки для смещения координат
        self.image = QImage(QSize(10, 10), QImage.Format_RGB32)
        self.image.load('UFO1.png')

    def keyPressEvent(self, event):
        key = event.key()
        step = 10 # шаг смещения по нажатию
        if key == Qt.Key_Left:
            self.x -= step
            if self.x < 0: self.x = self.width() - self.img_r
        elif key == Qt.Key_Up:
            self.y -= step
            if self.y < 0: self.y = self.height() - self.img_r
        elif key == Qt.Key_Right:
            self.x += step
            if self.x > self.width() - self.img_r: self.x = 0
        elif key == Qt.Key_Down:
            self.y += step
            if self.y > self.height() - self.img_r: self.y = 0

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(self.x, self.y, self.image)
        qp.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UFO_tracker()
    ex.show()
    sys.exit(app.exec_())
