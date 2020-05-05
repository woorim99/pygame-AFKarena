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

dealer_level = 1                                     #각 캐릭터 레벨 초기값
healer_level = 1
tanker_level = 1
magician_level = 1
stage_level = 1
coin = 0

class dealer(pygame.sprite.Sprite):       #dealer class
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.level = dealer_level
        self.health = 130 + dealer_level * 10
        self.amount_of_attack = 10000 + dealer_level * 5  #20

    def draw(self, effect):
        screen.blit(effect, (self.x,self.y))

    def health_bar(self):
        if self.health <= 0:
            pygame.draw.rect(screen, BLACK, [self.x, self.y - 30, 0, 0])   
        else:
            pygame.draw.rect(screen, BLACK, [self.x - 20, self.y - 30, self.health, 10])    

class healer(dealer):       #healer class
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 65 + healer_level * 5
        self.amount_of_attack = healer_level * 5

class tanker(dealer):       #tanker class
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 185 + tanker_level * 15
        self.amount_of_attack = 10000 + tanker_level * 3 #30

class magician(dealer):     #magician class
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 90 + magician_level * 10
        self.amount_of_attack = 10 + magician_level * 7
        self.level = magician_level

dealer1 = dealer(60, 350, 70, 78)             #딜러
healer1 = healer(150, 380, 70, 78)             #힐러
tanker1 = tanker(230, 350, 70, 78)            #탱커
magician1 = magician(370, 380, 70, 78)        #마법사
character_list = [dealer1, dealer1, healer1, tanker1, tanker1, tanker1, magician1, magician1] #몬스터가 자동공격할때 필요(맞을확률)

