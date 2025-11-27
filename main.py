""" Simple debut Main """
from PyQt5.QtWidgets import QApplication, QWidget
import sys

def main():
    app = QApplication(sys.argv)
    widget = QWidget()

    widget.show()

    app.exec_()
    greet = "Hello Python!"
    print(greet)

if __name__ == "__main__":
    main()