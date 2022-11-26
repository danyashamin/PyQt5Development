from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup, QPushButton
from PyQt5.QtCore import Qt
import sys

class TestWind(QWidget):
    def __init__(self, questions):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.show()
        global cur_question_number
        self.line_box = QHBoxLayout()
        self.box_answers = QGroupBox('Варианты ответов:')
        self.box_line_1 = QHBoxLayout()
        self.answer_1 = QRadioButton(questions[cur_question_number])
        if cur_question_number==0:
            sys.exit(app.exec_())

app = QApplication(sys.argv)
questions = [['Что обычно капает с неба?', 'Капли дождя', 'Деньги','Цинк', 'Ртуть']]
cur_question_number = 0
win = TestWind(questions)