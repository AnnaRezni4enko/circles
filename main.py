from PyQt5 import uic
import sys
from PyQt5.QtCore import QPoint
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Круги')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(5, 70)
        qp.drawEllipse(QPoint(150, 200), r, r)
        r = randint(5, 70)
        qp.drawEllipse(QPoint(300, 200), r, r)
        r = randint(5, 70)
        qp.drawEllipse(QPoint(450, 200), r, r)
        r = randint(5, 70)
        qp.drawEllipse(QPoint(150, 400), r, r)
        r = randint(5, 70)
        qp.drawEllipse(QPoint(300, 400), r, r)
        r = randint(5, 70)
        qp.drawEllipse(QPoint(450, 400), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())