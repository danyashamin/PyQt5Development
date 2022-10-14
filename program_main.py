import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w_2 = QWidget()
    w.resize(300, 150)
    w_2.resize(300, 150)
    w.move(300, 300)
    w_2.move(600, 300)
    w.setWindowTitle('My lovely window')
    w_2.setWindowTitle('My not lovely window')
    w.show()
    w_2.show()
    sys.exit(app.exec_())

