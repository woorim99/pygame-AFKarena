import sys
import pygame
from pygame.locals import QUIT

pygame.init()
display_width = 980
display_height = 512
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("AFK arena")
background = pygame.image.load('startbg.png')
dungeon = pygame.image.load('bg1.png')
character1 = pygame.image.load('character1.png')
play_button = pygame.image.load('playbutton.png')
monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')
pygame.mixer.music.load('bgmusic.mp3')       #배경음악
pygame.mixer.music.play(-1)                  #배경음악 끝나면 다시재생
clock = pygame.time.Clock()


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

class player():       #캐릭터 포지션마다 클래스 따로?
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class com_monster():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


start_screen = True
game_screen = False

dealer = player(100, 350, 70, 78)
healer = player(180, 420, 70, 78)
tanker = player(260, 350, 70, 78)
magician = player(340, 420, 70, 78)

monster_1 = com_monster(730, 320, 100, 129)
monster_2 = com_monster(600, 350, 100, 116)


def main():
    while True:
        global start_screen
        global game_screen
        if start_screen == True:
            screen.blit(background, (0, 0))
            screen.blit(play_button, (playButton.x, playButton.y))
        
        if game_screen == True:
            screen.blit(dungeon, (0, 0))
            screen.blit(character1, (dealer.x, dealer.y))
            screen.blit(character1, (healer.x, healer.y))
            screen.blit(character1, (tanker.x, tanker.y))
            screen.blit(character1, (magician.x, magician.y))
            screen.blit(monster1, (monster_1.x, monster_1.y))
            screen.blit(monster2, (monster_2.x, monster_2.y))
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:   
                if playButton.isOver(pos):
                    start_screen = False
                    game_screen = True
                    

        pygame.display.update()

if __name__ == '__main__':
    main()