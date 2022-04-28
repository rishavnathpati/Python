from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 300, 500)  # xpos,ypos, width, height
        self.setWindowTitle("SUDOKU- Solve and Play")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Let's begin")
        self.label.move(80, 40)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Start")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Solving started yeah")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())


window()
