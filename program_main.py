from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from PyQt5.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self, question, *args):
        super().__init__()
        self.common_line = QVBoxLayout()
        self.question_label = QLabel(self)
        self.question_label.setText(question)
        self.question_line = QHBoxLayout()
        self.question_line.addWidget(self.question_label, alignment=Qt.AlignTop)
        self.common_line.addLayout(self.question_line)
        self.setLayout(self.common_line)
        self.show()
        sys.exit(app.exec_())

app = QApplication(sys.argv)
m = MainWindow('Сколько капель в море?')