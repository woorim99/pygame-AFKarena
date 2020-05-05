import sys
import pygame
from pygame.locals import QUIT
from button import button

charBar = pygame.image.load('charBar.png')

dealerBar_button = pygame.image.load('dealerbarbutton.png')
d_select_button = pygame.image.load('d_select.png')
tankerBar_button = pygame.image.load('tankerbarbutton.png')
t_select_button = pygame.image.load('t_select.png')
healerBar_button = pygame.image.load('healerbarbutton.png')
h_select_button = pygame.image.load('h_select.png')
magicianBar_button = pygame.image.load('magicianbarbutton.png')
m_select_button = pygame.image.load('m_select.png')

class char_Bar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

bar = char_Bar(100,-30,20,800)
dealerBarButton = button(100,10,40,400)
d_selectButton = button(100,10,40,400)
tankerBarButton = button(250,10,40,400)
t_selectButton = button(250,10,40,400)
healerBarButton = button(400,10,40,400)
h_selectButton = button(400,10,40,400)
magicianBarButton = button(550,10,40,400)
m_selectButton = button(550,10,40,400)        