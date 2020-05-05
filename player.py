import sys
import pygame
from pygame.locals import QUIT

pygame.init()
display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

BLACK = (0, 0, 0)         #체력바 만들 때필요

character1 = pygame.image.load('character1.png')
character2 = pygame.image.load('character2.png')
character3 = pygame.image.load('character3.png')
character4 = pygame.image.load('character4.png')
star = pygame.image.load('star.png')

class dealer(pygame.sprite.Sprite):       #dealer class
    def __init__(self, x, y, width, height, health, amount_of_attack):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.amount_of_attack = amount_of_attack

    def draw(self, effect):
        screen.blit(effect, (self.x,self.y))

    def health_bar(self):
        if self.health <= 0:
            pygame.draw.rect(screen, BLACK, [self.x, self.y - 30, 0, 0])   
        else:
            pygame.draw.rect(screen, BLACK, [self.x - 20, self.y - 30, self.health, 10])    

class healer(dealer):       #healer class
    pass

class tanker(dealer):       #tanker class
    pass

class magician(dealer):     #magician class
    pass

dealer1 = dealer(60, 350, 70, 78, 100, 20)             #딜러
healer1 = healer(150, 380, 70, 78, 100, 5)             #힐러
tanker1 = tanker(230, 350, 70, 78, 200, 10)            #탱커
magician1 = magician(370, 380, 70, 78, 100, 15)        #마법사
character_list = [dealer1, healer1, tanker1, magician1]#몬스터가 자동공격할때 필요