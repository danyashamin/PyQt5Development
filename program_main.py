import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QPainter
import pygame as pg
pg.init()

screen = pg.display.set_mode((20, 20))
print(screen.get_buffer())