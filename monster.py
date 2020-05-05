import sys
import pygame
from pygame.locals import QUIT
from player import *

display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

BLACK = (0, 0, 0)         #체력바 만들 때필요

monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')

class com_monster():
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 240 + stage_level * 30
        self.amount_of_attack = stage_level * 3
        self.level = stage_level
    
    def health_bar(self):
        if self.health <= 0:
            pygame.draw.rect(screen, BLACK, [self.x - 60, self.y + 130, 0, 0])  
        else:
            pygame.draw.rect(screen, BLACK, [self.x - 60, self.y + 130, self.health, 10])    

monster_1 = com_monster(730, 310, 100, 129)   #몬스터1
monster_2 = com_monster(600, 350, 100, 116)   #몬스터2   
