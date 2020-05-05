import sys
import pygame
from pygame.locals import QUIT

play_button = pygame.image.load('play.png')
exit_button = pygame.image.load('exit.png')
option_button = pygame.image.load('option.png')

class button():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
 
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


# start screen
start_screen = True
game_screen = False
option_screen =False

#character button in charBar
d_button = False
t_button = False
h_button = False
m_button = False

playButton = button(377,462,273,69)
exitButton = button(90,460,273,69)
optionButton = button(670,460,273,69) 
op_exit = button(670, 400, 207, 109)
op_button = button(90, 400, 207, 109)               