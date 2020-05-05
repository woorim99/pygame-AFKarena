import sys
import pygame
from pygame.locals import QUIT

play_button = pygame.image.load('play.png')
exit_button = pygame.image.load('exit.png')
option_button = pygame.image.load('option.png')
back = pygame.image.load('back.png')                              #빨간색 back버튼
play = pygame.image.load('red_play.png')                          #빨간색 play 버튼

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
stage_screen = False
win_screen = False
lose_screen = False


playButton = button(377,460,273,69)
exitButton = button(90,460,273,69)
optionButton = button(670,460,273,69) 
op_back = button(750, 470, 100, 75)
stage_back = button(522, 460, 100, 75)
stage_play = button(402, 460, 100, 75)
restart_button = button(90, 400, 287, 74)
reexitButton = button(670, 400, 273, 69)
dealer_levelup = button(90, 90, 200, 100)
healer_levelup = button(90, 210, 200, 100)
tanker_levelup = button(90, 330, 200, 100)
magician_levelup = button(90, 450, 200, 100)
