import sys
import pygame
from pygame.locals import QUIT
from player import *

display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

GREEN = (0, 255, 0)         #체력바 만들 때필요


mon1_0 = pygame.image.load('image/mon1/mon1_0.png')
mon1_1 = pygame.image.load('image/mon1/mon1_1.png')
mon1_2 = pygame.image.load('image/mon1/mon1_2.png')
mon1_3 = pygame.image.load('image/mon1/mon1_3.png')

mon2_0 = pygame.image.load('image/mon2/mon2_0.png')
mon2_1 = pygame.image.load('image/mon2/mon2_1.png')
mon2_2 = pygame.image.load('image/mon2/mon2_2.png')
mon2_3 = pygame.image.load('image/mon2/mon2_3.png')

death = pygame.image.load('image/death.png')

class com_monster():
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 240 + stage_level * 30
        self.amount_of_attack = stage_level * 3
        self.level = stage_level

    def health_bar(self):
        if self.health <= 0:
            screen.blit(death, (self.x, self.y))              
        else:
            pygame.draw.rect(screen, GREEN, [self.x - 30, self.y - 30, self.health, 10])    


monster_1 = com_monster(730, 320, 100, 129)   #몬스터1
monster_2 = com_monster(600, 350, 100, 116)   #몬스터2   