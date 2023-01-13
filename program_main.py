from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup, QPushButton, QListWidget, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
import sys

class TestWind(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        global cur_question_number
        self.line_h = QHBoxLayout()
        self.list_answers = QListWidget()
        global elements
        for element in elements:
            self.list_answers.addItem(element)
            def func_cur():
                message = QMessageBox()
                need_text = 'Текущий елемент:'+self.list_answers.selectedItems()[0].text()
                message.setText(need_text)
                message.show()
                message.exec_()
            self.list_answers.itemSelectionChanged.connect(func_cur)
        self.line_h.addWidget(self.list_answers)
        self.line_v = QVBoxLayout()
        self.line_v.addLayout(self.line_h)
        win = QWidget()
        win.setLayout(self.line_v)
        self.setCentralWidget(win)
        self.show()
        if cur_question_number==0:
            sys.exit(app.exec_())

app = QApplication(sys.argv)
elements = ['element_1', 'element_2']
cur_question_number = 0
win = TestWind()