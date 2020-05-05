import sys
import pygame
from pygame.locals import QUIT

display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

BLACK = (0, 0, 0)         #체력바 만들 때필요

monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')


class com_monster():
    def __init__(self, x, y, width, height, health, amount_of_attack):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.height = height
        self.health = health
        self.amount_of_attack = amount_of_attack
    def health_bar(self):
        if self.health <= 0:
            pygame.draw.rect(screen, BLACK, [self.x, self.y - 30, 0, 0])  
        else:
            pygame.draw.rect(screen, BLACK, [self.x - 30, self.y - 30, self.health, 10])    

    '''def __del__(self):
        print('몬스터 처치')'''

monster_1 = com_monster(730, 320, 100, 129, 200, 15)   #몬스터1
monster_2 = com_monster(600, 350, 100, 116, 200, 15)   #몬스터2   