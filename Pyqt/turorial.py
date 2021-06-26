import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def clicked():
    print("clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Tech with Peter.")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    label.move(50, 50)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

    []


if __name__ == '__main__':
    window()
