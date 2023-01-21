from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup, QPushButton, QListWidget, QMessageBox, QMainWindow, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
import sys
import os

class ImageEditor(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.main_line = QVBoxLayout()
        self.line_h = QHBoxLayout()
        self.line_h.setSpacing(6)
        self.line_folder = QVBoxLayout()
        self.line_folder.setSpacing(6)
        self.folder_button = QPushButton('Папка')
        self.folder_button.clicked.connect(self.folder_fun)
        self.line_folder.addWidget(self.folder_button, stretch=1)
        self.list_folder = QListWidget()
        self.line_folder.addWidget(self.list_folder, stretch=5)
        self.line_h.addLayout(self.line_folder, stretch=1|6)
        self.line_image_and_buttons = QVBoxLayout()
        self.line_image_and_buttons.setSpacing(6)
        self.label_image = QLabel(self)
        if len(args)>0:
            for i in os.listdir():
                if i.find('.small')==-1:
                    self.list_folder.addItem(i)
                    def func_cur():
                        with Image.open(self.list_folder.selectedItems()[0].text()) as self.f_image:
                            if self.f_image.size[0]>1000 or self.f_image.size[1]>500:
                                self.f_small = self.f_image.resize((int(self.f_image.size[0]/3), int(self.f_image.size[1]/3)))
                                self.f_small.save(self.list_folder.selectedItems()[0].text()[0:len(self.list_folder.selectedItems()[0].text())-4]+'.small.png')
                                pix = QPixmap(self.list_folder.selectedItems()[0].text()[0:len(self.list_folder.selectedItems()[0].text())-4]+'.small.png')
                                self.label_image.setPixmap(pix)
                    self.list_folder.itemSelectionChanged.connect(func_cur)
        self.line_image_and_buttons.addWidget(self.label_image, stretch=5)
        self.line_buttons = QHBoxLayout()
        self.line_buttons.setSpacing(5)
        self.left_button = QPushButton('Лево')
        self.left_button.clicked.connect(self.left_fun)
        self.line_buttons.addWidget(self.left_button, stretch=1|5)
        self.right_button = QPushButton('Право')
        self.right_button.clicked.connect(self.right_fun)
        self.line_buttons.addWidget(self.right_button, stretch=1|5)
        self.mirror_button = QPushButton('Зеркало')
        self.mirror_button.clicked.connect(self.mirror_fun)
        self.line_buttons.addWidget(self.mirror_button, stretch=1|5)
        self.enchance_button = QPushButton('Резкость')
        self.enchance_button.clicked.connect(self.enchance_fun)
        self.line_buttons.addWidget(self.enchance_button, stretch=1|5)
        self.black_white = QPushButton('Ч/Б')
        self.black_white.clicked.connect(self.black_white_fun)
        self.line_buttons.addWidget(self.black_white, stretch=1|5)
        self.line_image_and_buttons.addLayout(self.line_buttons, stretch=1|6)
        self.line_h.addLayout(self.line_image_and_buttons, stretch=5|6)
        self.main_line.addLayout(self.line_h)
        self.win = QWidget()
        self.win.setLayout(self.main_line)
        self.setCentralWidget(self.win)
        self.show()
        if ImageEditor.count==0:
            ImageEditor.count+=1
            sys.exit(app.exec_())
    def folder_fun(self):
        self.file_dialog = QFileDialog()
        work_dir = self.file_dialog.getExistingDirectory()
        os.chdir(work_dir)
        self.hide()
        self.__init__(work_dir)
    def left_fun(self):
        try:
            d = QInputDialog()
            text, _ = d.getText(self, 'Поворот влево', 'Введите новое имя')
            f_image = self.f_image.transpose(Image.ROTATE_90)
            f_image.save(text)
        except:
            m = QMessageBox()
            m.setText('Введите нормальное имя!')
            m.show()
            m.exec_()
    def right_fun(self):
        try:
            d = QInputDialog()
            text, _ = d.getText(self, 'Поворот влево', 'Введите новое имя:')
            f_image = self.f_image.transpose(Image.ROTATE_180)
            f_image = f_image.transpose(Image.ROTATE_90)
            f_image.save(text)
        except:
            m = QMessageBox()
            m.setText('Введите нормальное имя!')
            m.show()
            m.exec_()
    def mirror_fun(self):
        f_image = self.f_image.transpose(Image.FLIP_LEFT_RIGHT)
        d = QInputDialog()
        text, _ = d.getText(self, 'Отзеркаливание', 'Введите новое имя:')
        try:
            f_image.save(text)
        except:
            m = QMessageBox()
            m.setText('Введите нормальное имя!')
            m.show()
            m.exec_()
    def enchance_fun(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Увеличение контраста', 'Во сколько раз вы хотите увеличить контраст:')
        en_im = ImageEnhance.Contrast(self.f_image)
        try:
            en_im = en_im.enhance(float(text))
            d = QInputDialog()
            name, _ = d.getText(self, 'Увеличение контраста', 'Введите имя:')
            en_im.save(name)
        except:
            m = QMessageBox()
            m.setText('Введите контраст дробным числом!')
            m.show()
            m.exec_()
    def black_white_fun(self):
        image_black = self.f_image.convert('L')
        d = QInputDialog()
        try:
            name, _ = d.getText(self, 'Создание чёрно-белого изображения', 'Введите имя:')
            image_black.save(name)
        except:
            m = QMessageBox()
            m.setText('Введите нормальное имя!')
            m.show()
            m.exec_()

ImageEditor.count = 0
app = QApplication(sys.argv)
elements = ['element_1', 'element_2']
win = ImageEditor()