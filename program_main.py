import sys
from unicodedata import name
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self, image_name):
        super().__init__()
        self.image_name = image_name
        self.initGui()
    def initGui(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon(icons[self.image_name]))
        self.show()

icons = {'my_icon_1':'images/my_icon_1.bmp', 'my_icon_2':'images/my_icon_2.bmp'}

if __name__ == '__main__':
    app_1 = QApplication(sys.argv)
    ex = Example('my_icon_1')
    app_2 = QApplication(sys.argv)
    ex_2 = Example('my_icon_2')
    sys.exit(app_1.exec_())
    sys.exit(app_2.exec_())