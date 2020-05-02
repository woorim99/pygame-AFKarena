import sys
import pygame
import random
from pygame.locals import QUIT

pygame.init()
display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("AFK arena")                           #창이름

background = pygame.image.load('startbg.png')                     #사진
dungeon = pygame.image.load('bg1.png')
character1 = pygame.image.load('character1.png')
character2 = pygame.image.load('character2.png')
character3 = pygame.image.load('character3.png')
character4 = pygame.image.load('character4.png')
character5 = pygame.image.load('character5.png')
play_button = pygame.image.load('play.png')
exit_button = pygame.image.load('exit.png')
option_button = pygame.image.load('option.png')
monster1 = pygame.image.load('monster1.png')
monster2 = pygame.image.load('monster2.png')
star = pygame.image.load('star.png')
white = pygame.image.load('white.png')
black = pygame.image.load('black.png')

pygame.mixer.music.load('bgmusic.mp3')               #배경음악
pygame.mixer.music.play(-1)                          #배경음악 끝나면 다시재생
clock = pygame.time.Clock()
start_screen = True
game_screen = False
option_screen = False

dealer_skill = []                                    #스킬 쿨타임 만들때 필요한 리스트
healer_skill = []
tanker_skill = []
magician_skill = []

dealer_ctime = 1                                     #스킬 쿨타임 초기값                                          
healer_ctime = 1
tanker_ctime = 1
magician_ctime = 1

dauto_list = []                                      #캐릭터가 자동공격 할 때 필요
hauto_list = []
tauto_list = []
mauto_list = []

dealer_auto = 1                                      #캐릭터가 자동공격 할 때 필요
healer_auto = 1
tanker_auto = 1
magician_auto = 1

'''m1_list = []                                         #몬스터가 자동공격 할 때 필요
m2_list = []

m1_auto = 1                                          #몬스터가 자동공격 할 때 필요
m2_auto = 1'''

class button():                                      #버튼 클래스
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
 
    def isOver(self, pos):                           #클릭 한 곳이 버튼 안쪽인지 확인
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
playButton = button(377, 462, 273, 69)               #시작버튼
exitButton = button(90, 460, 273, 69)                #나가는 버튼
optionButton = button(670, 460, 273, 69)             #옵션버튼
op_exit = button(670, 400, 207, 109)
op_button = button(90, 400, 207, 109)

class dealer():       #dealer class
    def __init__(self, x, y, width, height, health, amount_of_attack):   #캐릭터 좌표/가로세로길이/체력/딜량
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.amount_of_attack = amount_of_attack

    def draw(self, effect):                        #스킬 이펙트 그리는함수            
        screen.blit(effect, (self.x, self.y))    

class healer(dealer):       #healer class
    pass

class tanker(dealer):       #tanker class
    pass

class magician(dealer):       #magician class
    pass

class com_monster():      #monster class
    def __init__(self, x, y, width, height, health, amount_of_attack):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.amount_of_attack = amount_of_attack

dealer1 = dealer(60, 350, 70, 78, 100, 20)             #딜러
healer1 = healer(150, 380, 70, 78, 100, 5)             #힐러
tanker1 = tanker(230, 350, 70, 78, 200, 10)            #탱커
magician1 = magician(370, 380, 70, 78, 100, 15)        #마법사
character_list = [dealer1, healer1, tanker1, magician1]

monster_1 = com_monster(730, 320, 100, 129, 200, 15)   #몬스터1
monster_2 = com_monster(600, 350, 100, 116, 200, 15)   #몬스터2

def game():
    global start_screen, game_screen, option_screen                  #화면들
    global dealer_ctime, healer_ctime, tanker_ctime, magician_ctime  #기술들 쿨타임
    global dealer_skill, healer_skill, tanker_skill, magician_skill  #쿨타임 만들 때 필요한 리스트
    global dealer_auto, healer_auto, tanker_auto, magician_auto      #캐릭터가 자동공격 만들때 필요
    global dauto_list, hauto_list, tauto_list, mauto_list            #캐릭터가 자동공격 만들때 필요
    '''global m1_auto, m2_auto, m1_list, m2_list, character_list        #몬스터가 자동공격 할 때 필요'''
    
    if start_screen is True:                         #시작화면일때
        screen.blit(background, (0, 0))              #배경
        screen.blit(play_button, (playButton.x, playButton.y))       #시작버튼
        screen.blit(option_button, (optionButton.x, optionButton.y))   #옵션버튼
        screen.blit(exit_button, (exitButton.x, exitButton.y))       #나가는버튼
        
        for event in pygame.event.get():                   
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isOver(pos):
                    start_screen = False
                    game_screen = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionButton.isOver(pos):
                    start_screen = False
                    game_screen = False
                    option_screen = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.isOver(pos):
                    pygame.quit()
                    sys.exit()          

    if game_screen is True:
        screen.blit(dungeon, (0, 0))
        screen.blit(character4, (dealer1.x, dealer1.y))
        screen.blit(character2, (healer1.x, healer1.y))
        screen.blit(character5, (tanker1.x, tanker1.y))
        screen.blit(character3, (magician1.x, magician1.y))
        screen.blit(monster1, (monster_1.x, monster_1.y))
        screen.blit(monster2, (monster_2.x, monster_2.y))
        
        clock.tick(10)                #쿨타임에필요

        '''m1_auto -= 1
        m2_auto -= 1

        if m1_auto == 0:
            m1_list.append('O')

        if m2_auto == 0:
            m2_list.append('O')

        if len(m1_list) == 1:
            for i in character_list:
                if i.health <= 0:
                    character_list.remove(i)
            a = random.choice(character_list)
            a.health -= 3
            character_list.remove(a)
            m1_auto = 10
            print(dealer1.health, healer1.health, tanker1.health, magician1.health)

        if len(m2_list) == 1:
            for i in character_list:
                if i.health <= 0:
                    character_list.remove(i)
            a = random.choice(character_list)
            a.health -= 3
            character_list.remove(a)
            m2_auto = 10
            print(dealer1.health, healer1.health, tanker1.health, magician1.health)'''
        
        dealer_auto -= 1          #딜러의 자동공격에필요
        healer_auto -= 2
        tanker_auto -= 3
        magician_auto -= 4

        if dealer_auto == 0:
            dauto_list.append('O')

        if healer_auto == 0:
            hauto_list.append('O')

        if tanker_auto == 0:
            tauto_list.append('O')

        if magician_auto == 0:
            mauto_list.append('O')

        if len(dauto_list) == 1:
            if monster_1.health <= 0 and monster_2.health > 0:
                monster_2.health -= 1
                dauto_list.pop()
                dealer_auto = 10
                print(monster_1.health, monster_2.health)

            elif monster_1.health > 0 and monster_2.health <= 0:
                monster_1.health -= 1
                dauto_list.pop()
                dealer_auto = 10
                print(monster_1.health, monster_2.health)

            else:
                a = random.choice([monster_1, monster_2])
                a.health -= 1
                dauto_list.pop()
                dealer_auto = 10
                print(monster_1.health, monster_2.health)

        if len(hauto_list) == 1:
            if monster_1.health <= 0 and monster_2.health > 0:
                monster_2.health -= 1
                hauto_list.pop()
                healer_auto = 10
                print(monster_1.health, monster_2.health)

            elif monster_1.health > 0 and monster_2.health <= 0:
                monster_1.health -= 1
                hauto_list.pop()
                healer_auto = 10
                print(monster_1.health, monster_2.health)

            else:
                a = random.choice([monster_1, monster_2])
                a.health -= 1
                hauto_list.pop()
                healer_auto = 10
                print(monster_1.health, monster_2.health)

        if len(tauto_list) == 1:
            if monster_1.health <= 0 and monster_2.health > 0:
                monster_2.health -= 1
                tauto_list.pop()
                tanker_auto = 10
                print(monster_1.health, monster_2.health)

            elif monster_1.health > 0 and monster_2.health <= 0:
                monster_1.health -= 1
                tauto_list.pop()
                tanker_auto = 10
                print(monster_1.health, monster_2.health)

            else:
                a = random.choice([monster_1, monster_2])
                a.health -= 1
                tauto_list.pop()
                tanker_auto = 10
                print(monster_1.health, monster_2.health)

        if len(mauto_list) == 1:
            if monster_1.health <= 0 and monster_2.health > 0:
                monster_2.health -= 1
                mauto_list.pop()
                magician_auto = 10
                print(monster_1.health, monster_2.health)

            elif monster_1.health > 0 and monster_2.health <= 0:
                monster_1.health -= 1
                mauto_list.pop()
                magician_auto = 10
                print(monster_1.health, monster_2.health)

            else:
                a = random.choice([monster_1, monster_2])
                a.health -= 1
                mauto_list.pop()
                magician_auto = 10
                print(monster_1.health, monster_2.health)
        
        dealer_ctime -= 1
        healer_ctime -= 1
        tanker_ctime -= 1
        magician_ctime -= 1
        
        if dealer_ctime == 0:
            dealer_skill.append('O')
            print('딜러스킬 쿨타임 종료')
        if healer_ctime == 0:
            healer_skill.append('O')
            print('힐러스킬 쿨타임 종료')
        if tanker_ctime == 0:
            tanker_skill.append('O')
            print('탱커스킬 쿨타임 종료')
        if magician_ctime == 0:
            magician_skill.append('O')
            print('마법사 스킬 쿨타임 종료')
        
        if monster_1.health <= 0 and monster_2.health <= 0:
            pygame.quit()            #You win! 화면 나오게 고치기(retry/exit)
            sys.exit

        if dealer1.health <= 0 and healer1.health <= 0 and tanker1.health <= 0 and magician1.health <= 0:
            pygame.quit()            #You lose! 화면 나오게 고치기(retry/exit)
            sys.exit


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if e.type == pygame.KEYUP:
                if e.key == ord('q') and len(dealer_skill) == 1:                  #딜러가 스킬쓸 때 몬스터 체력 닳게
                    dealer1.draw(star)
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= dealer1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= dealer1.amount_of_attack
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= dealer1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    dealer_skill.pop()
                    dealer_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if e.key == ord('w') and len(healer_skill) == 1:                
                    healer1.draw(star)                                  #힐러가 스킬 쓸 때 몬스터 체력 닳게
                    healer1.draw(star)
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= healer1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= healer1.amount_of_attack
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= healer1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    healer_skill.pop()
                    healer_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if e.key == ord('e') and len(tanker_skill) == 1:
                    tanker1.draw(star)                                     #탱커가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= tanker1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= tanker1.amount_of_attack
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= tanker1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    tanker_skill.pop()
                    tanker_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if e.key == ord('r') and len(magician_skill) == 1:
                    magician1.draw(star)                                #마법사가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= magician1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= magician1.amount_of_attack
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= magician1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    magician_skill.pop()
                    magician_ctime = 100
                    print('스킬 쿨타임 시작')

    if option_screen is True:
        screen.blit(white, (0, 0))
        screen.blit(black, (op_exit.x, op_exit.y))
        screen.blit(black, (op_button.x, op_button.y))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_exit.isOver(pos):
                    start_screen = True
                    game_screen = False
                    option_screen = False
                

def main():
    while True:
        game()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()