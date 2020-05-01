import sys
import pygame
from pygame.locals import QUIT

pygame.init()
display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("AFK arena")     #창이름

background = pygame.image.load('startbg.png')       #사진
dungeon = pygame.image.load('bg1.png')
character1 = pygame.image.load('character1.png')
character2 = pygame.image.load('character2.png')
character3 = pygame.image.load('character3.png')
character4 = pygame.image.load('character4.png')
character5 = pygame.image.load('character5.png')
play_button = pygame.image.load('playbutton.png')
monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')
star = pygame.image.load('star.png')

pygame.mixer.music.load('bgmusic.mp3')       #배경음악
pygame.mixer.music.play(-1)                  #배경음악 끝나면 다시재생
clock = pygame.time.Clock()
start_screen = True
game_screen = False

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
            
playButton = button(310,380,200,69)

class dealer():       #dealer class
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, effect):
            screen.blit(effect, (self.x, self.y))

class healer(dealer):       #healer class
    pass

class tanker(dealer):       #tanker class
    pass

class magician(dealer):       #magician class
    pass

class com_monster():      #monster class
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

dealer1 = dealer(60, 350, 70, 78)
healer1 = healer(150, 380, 70, 78)
tanker1 = tanker(230, 350, 70, 78)
magician1 = magician(370, 380, 70, 78)

monster_1 = com_monster(730, 320, 100, 129)
monster_2 = com_monster(600, 350, 100, 116)

def main_view():
    global start_screen, game_screen
    if start_screen is True:
        screen.blit(background, (0, 0))
        screen.blit(play_button, (playButton.x, playButton.y))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isOver(pos):
                    start_screen = False
                    game_screen = True

    if game_screen is True:
        screen.blit(dungeon, (0, 0))
        screen.blit(character4, (dealer1.x, dealer1.y))
        screen.blit(character2, (healer1.x, healer1.y))
        screen.blit(character5, (tanker1.x, tanker1.y))
        screen.blit(character3, (magician1.x, magician1.y))
        screen.blit(monster1, (monster_1.x, monster_1.y))
        screen.blit(monster2, (monster_2.x, monster_2.y))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYUP:
                if e.key == ord('q'):
                    dealer1.skill = True
                    dealer1.draw(star)
                if e.key == ord('w'):
                    healer1.skill = True
                    healer1.draw(star)
                if e.key == ord('e'):
                    tanker1.skill = True
                    tanker1.draw(star)
                if e.key == ord('r'):
                    magician1.skill = True
                    magician1.draw(star)

def main():
    while True:
        main_view()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()