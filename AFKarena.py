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
lose = pygame.image.load('lose.png')
win = pygame.image.load('win.png')
restart = pygame.image.load('restart.png')

BLACK = (0, 0, 0)         #체력바 색깔

pygame.mixer.music.load('bgmusic.mp3')               #배경음악
pygame.mixer.music.play(-1)                          #배경음악 끝나면 다시재생
clock = pygame.time.Clock()
start_screen = True
game_screen = False
option_screen = False
stage_screen = False
win_screen = False
lose_screen = False

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

m1_list = []                                         #몬스터가 자동공격 할 때 필요
m2_list = []

m1_auto = 1                                          #몬스터가 자동공격 할 때 필요
m2_auto = 1

dealer_level = 1
healer_level = 1
tanker_level = 1
magician_level = 1
stage_level = 1
coin = 0

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
op_button1 = button(90, 20, 207, 109)
op_button2 = button(90, 150, 207, 109)
op_button3 = button(90, 280, 207, 109)
op_button4 = button(90, 410, 207, 109)
stage_exit = button(670, 460, 273, 69)
stage_button = button(90, 460, 207, 109)
restart_button = button(90, 400, 287, 74)
reexitButton = button(670, 400, 273, 69)

class dealer():       #dealer class
    def __init__(self, x, y, width, height):   #캐릭터 좌표/가로세로길이/체력/스킬 딜량
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.level = dealer_level
        self.health = 130 + dealer_level * 10
        self.amount_of_attack = 20 + dealer_level * 5

    def draw(self, effect):                        #스킬 이펙트 그리는함수            
        screen.blit(effect, (self.x, self.y))    

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
        self.amount_of_attack = 30 + tanker_level * 3

class magician(dealer):       #magician class
    def __init__(self, x, y, width, height):
        dealer.__init__(self, x, y, width, height)
        self.health = 90 + magician_level * 10
        self.amount_of_attack = 10 + magician_level * 7
        self.level = magician_level

class com_monster(dealer):      #monster class
    def __init__(self, x, y, width, height):    #나중에 amount_of_attack쓰기
        dealer.__init__(self, x, y, width, height)
        self.health = 240 + stage_level * 30
        self.amount_of_attack = stage_level * 5
        self.level = stage_level

    def health_bar(self):
        if self.health <= 0:
            pygame.draw.rect(screen, BLACK, [self.x - 60, self.y + 130, 0, 0])  
        else:
            pygame.draw.rect(screen, BLACK, [self.x - 60, self.y + 130, self.health, 10])


dealer1 = dealer(60, 350, 70, 78)             #딜러
healer1 = healer(150, 380, 70, 78)            #힐러
tanker1 = tanker(230, 365, 70, 78)            #탱커
magician1 = magician(370, 395, 70, 78)        #마법사
character_list = [dealer1, dealer1, healer1, tanker1, tanker1, tanker1, magician1, magician1] #몬스터가 자동공격할때 필요(맞을확률)

monster_1 = com_monster(730, 310, 100, 129)   #몬스터1
monster_2 = com_monster(600, 350, 100, 116)   #몬스터2

def game():
    global start_screen, game_screen, option_screen, stage_screen, win_screen, lose_screen #game_over_screen 화면들
    global dealer_ctime, healer_ctime, tanker_ctime, magician_ctime    #기술들 쿨타임
    global dealer_skill, healer_skill, tanker_skill, magician_skill    #쿨타임 만들 때 필요한 리스트
    global dealer_auto, healer_auto, tanker_auto, magician_auto        #캐릭터가 자동공격 만들때 필요
    global dauto_list, hauto_list, tauto_list, mauto_list              #캐릭터가 자동공격 만들때 필요
    global m1_auto, m2_auto, m1_list, m2_list, character_list          #몬스터가 자동공격 할 때 필요
    global dealer_level, healer_level, tanker_level, magician_level, stage_level
    global dealer1, healer1, tanker1, magician1, monster_1, monster_2, coin, BLACK
    
    if start_screen is True:                         #시작화면일때
        screen.blit(background, (0, 0))              #배경
        screen.blit(play_button, (playButton.x, playButton.y))       #시작버튼
        screen.blit(option_button, (optionButton.x, optionButton.y))   #옵션버튼
        screen.blit(exit_button, (exitButton.x, exitButton.y))       #나가는버튼
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin : ' + str(int(coin)), True, BLACK)
        screen.blit(currentcoin, (15, 15))
        
        for event in pygame.event.get():                   
            pos = pygame.mouse.get_pos()                     #X버튼 누르면 나가짐
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:        #시작버튼 누르면 게임화면
                if playButton.isOver(pos):
                    start_screen = False
                    game_screen = False
                    stage_screen = True
                    option_screen = False
                    game_over_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:       #옵션버튼 누르면 옵션화면
                if optionButton.isOver(pos):
                    start_screen = False
                    game_screen = False
                    option_screen = True
                    stage_screen = False
                    game_over_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:       #exit버튼 누르면 나가기
                if exitButton.isOver(pos):
                    pygame.quit()
                    sys.exit()      

    if stage_screen is True:               #스테이지 정보알리기
        screen.blit(white, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentStage = largeFont.render('STAGE:' + str(stage_level), True, (0, 0, 0))
        screen.blit(currentStage, (850, 15))
        screen.blit(play_button, (stage_button.x, stage_button.y))
        screen.blit(exit_button, (stage_exit.x, stage_exit.y))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage_button.isOver(pos):
                    stage_screen = False
                    game_screen = True
                    option_screen = False
                    stage_screen = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage_exit.isOver(pos):
                    start_screen = True
                    game_screen = False
                    option_screen = False
                    stage_screen = False

    if game_screen is True:                                    #게임화면일때
        screen.blit(dungeon, (0, 0))                           #배경
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentStage = largeFont.render('STAGE :' + str(stage_level), True, (0, 0, 0))
        screen.blit(currentStage, (850, 15))
        screen.blit(character4, (dealer1.x, dealer1.y))        #캐릭터/몬스터
        screen.blit(character2, (healer1.x, healer1.y))
        screen.blit(character5, (tanker1.x, tanker1.y))
        screen.blit(character3, (magician1.x, magician1.y))
        screen.blit(monster1, (monster_1.x, monster_1.y))
        screen.blit(monster2, (monster_2.x, monster_2.y))
        dealer1.health_bar()
        healer1.health_bar()
        tanker1.health_bar()
        magician1.health_bar()
        monster_1.health_bar()
        monster_2.health_bar()
        
        clock.tick(10)                #쿨타임에필요

        m1_auto -= 1                 #몬스터 자동공격 할 떄필요
        m2_auto -= 1

        if m1_auto == 0:                 #몬스터 자동공격할 떄 필요
            m1_list.append('O')

        if m2_auto == 0:
            m2_list.append('O')

        if len(m1_list) == 1 and monster_1.health > 0:               #몬스터1(피가 0보다클 때)가 캐릭터를 자동공격
            for i in character_list:
                if i.health <= 0:
                    character_list.remove(i)
            if len(character_list) > 0:
                a = random.choice(character_list)
                a.health -= monster_1.amount_of_attack
                m1_list.pop()
                m1_auto = 10
                print(dealer1.health, healer1.health, tanker1.health, magician1.health)

            else:
                start_screen = False
                game_screen = False
                option_screen = False    
                lose_screen = True
        
        if len(m2_list) == 1 and monster_2.health > 0:             #몬스터2(피가 0보다클 때)가 캐릭터를 자동공격
            for i in character_list:
                if i.health <= 0:
                    character_list.remove(i)
            if len(character_list) > 0:
                a = random.choice(character_list)
                a.health -= monster_2.amount_of_attack
                m2_list.pop()
                m2_auto = 10
                print(dealer1.health, healer1.health, tanker1.health, magician1.health)

            else:
                    start_screen = False
                    game_screen = False
                    option_screen = False    
                    lose_screen = True
        
        dealer_auto -= 1          #캐릭터의 자동공격에필요
        healer_auto -= 1
        tanker_auto -= 1
        magician_auto -= 1

        if dealer_auto == 0:             #캐릭터의 자동공격에 필요
            dauto_list.append('O')

        if healer_auto == 0:
            hauto_list.append('O')

        if tanker_auto == 0:
            tauto_list.append('O')

        if magician_auto == 0:
            mauto_list.append('O')

        if len(dauto_list) == 1:                  #딜러(피가 0보다클때)가 몬스터를 자동공격
            if dealer1.health > 0:
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

                elif monster_1.health < 0 and monster_2.health < 0:
                    start_screen = False
                    game_screen = False
                    option_screen = False    
                    win_screen = True
                    coin += 12 * stage_level * 0.5

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    dauto_list.pop()
                    dealer_auto = 10
                    print(monster_1.health, monster_2.health)

        if len(hauto_list) == 1:                #힐러(피가 0보다클때)가 몬스터를 자동공격  
            if healer1.health > 0:
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

                elif monster_1.health < 0 and monster_2.health < 0:
                    start_screen = False
                    game_screen = False
                    option_screen = False    
                    win_screen = True
                    coin += 12 * stage_level * 0.5

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    hauto_list.pop()
                    healer_auto = 10
                    print(monster_1.health, monster_2.health)

        if len(tauto_list) == 1:                  #탱커(피가 0보다클때)가 몬스터를 자동공격
            if tanker1.health > 0:
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

                elif monster_1.health < 0 and monster_2.health < 0:
                    start_screen = False
                    game_screen = False
                    option_screen = False    
                    win_screen = True
                    coin += 12 * stage_level * 0.5

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    tauto_list.pop()
                    tanker_auto = 10
                    print(monster_1.health, monster_2.health)

        if len(mauto_list) == 1:                   #마법사(피가 0보다클때)가 몬스터를 자동공격
            if magician1.health > 0:
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

                elif monster_1.health < 0 and monster_2.health < 0:
                    start_screen = False
                    game_screen = False
                    option_screen = False    
                    win_screen = True
                    coin += 12 * stage_level * 0.5

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    mauto_list.pop()
                    magician_auto = 10
                    print(monster_1.health, monster_2.health)
        
        dealer_ctime -= 1                     #캐릭터 스킬('q', 'w', 'e', 'r') 쿨타임에필요
        healer_ctime -= 1
        tanker_ctime -= 1
        magician_ctime -= 1
        
        if dealer_ctime == 0:                   #쿨타임이 0일 때 스킬 쿨타임종료
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
        
        '''if dealer1.health <= 0 and healer1.health <= 0 and tanker1.health <= 0 and magician1.health <= 0:
            start_screen = False
            game_screen = False
            option_screen = False   
            lose_screen = True'''

        for event in pygame.event.get():                
            if event.type == pygame.QUIT:                
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == ord('q') and len(dealer_skill) == 1 and dealer1.health > 0: #딜러가 스킬쓸 때 몬스터 체력 닳게
                    dealer1.draw(star)
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= dealer1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= dealer1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        start_screen = False
                        game_screen = False
                        option_screen = False    
                        win_screen = True
                        # coin += 10 * stage_level
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= dealer1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    dealer_skill.pop()
                    dealer_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if event.key == ord('w') and len(healer_skill) == 1 and healer1.health > 0:                
                    healer1.draw(star)                                  #힐러가 스킬 쓸 때 캐릭터 체력 랜덤 회복
                    for i in character_list:
                        if i.health <= 0:
                            character_list.remove(i)
                    a = random.choice(character_list)
                    a.health += healer1.amount_of_attack
                    healer_skill.pop()
                    healer_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if event.key == ord('e') and len(tanker_skill) == 1 and tanker1.health > 0:
                    tanker1.draw(star)                                     #탱커가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= tanker1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= tanker1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        start_screen = False
                        game_screen = False
                        option_screen = False    
                        win_screen = True
                        # coin += 10 * stage_level
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= tanker1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    tanker_skill.pop()
                    tanker_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if event.key == ord('r') and len(magician_skill) == 1 and magician1.health > 0:
                    magician1.draw(star)                                #마법사가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= magician1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= magician1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        start_screen = False
                        game_screen = False
                        option_screen = False    
                        win_screen = True
                        # coin += 10 * stage_level
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= magician1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    magician_skill.pop()
                    magician_ctime = 100
                    print('스킬 쿨타임 시작')

    if option_screen is True:                 #옵션스크린일때
        screen.blit(white, (0, 0))
        screen.blit(black, (op_exit.x, op_exit.y))
        screen.blit(black, (op_button1.x, op_button1.y))
        screen.blit(black, (op_button2.x, op_button2.y))
        screen.blit(black, (op_button3.x, op_button3.y))
        screen.blit(black, (op_button4.x, op_button4.y))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, (255,255,255))
        screen.blit(currentcoin, (15, 15))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_button1.isOver(pos):
                    if coin >= dealer_level * 10:
                        coin -= dealer_level * 10
                        dealer_level += 1
                        dealer1 = dealer(60, 350, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_button2.isOver(pos):
                    if coin >= healer_level * 10:
                        coin -= healer_level * 10
                        healer_level += 1
                        healer1 = healer(150, 380, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_button3.isOver(pos):
                    if coin >= tanker_level * 10:
                        coin -= tanker_level * 10
                        tanker_level += 1
                        tanker1 = tanker(230, 365, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_button4.isOver(pos):
                    if coin >= magician_level * 10:
                        coin -= magician_level * 10
                        magician_level += 1
                        magician1 = magician(370, 395, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_exit.isOver(pos):
                    start_screen = True
                    game_screen = False
                    option_screen = False
                    stage_screen = False
                    character_list = [dealer1, healer1, tanker1, magician1]

    if win_screen == True:
        screen.blit(white, (0, 0))
        screen.blit(play_button, (stage_button.x, stage_button.y)) #retry
        screen.blit(exit_button, (stage_exit.x, stage_exit.y)) #exit
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, BLACK)
        screen.blit(currentcoin, (115, 115))
        dealer1 = dealer(60, 350, 70, 78)  # 딜러
        healer1 = healer(150, 380, 70, 78)  # 힐러
        tanker1 = tanker(230, 365, 70, 78)  # 탱커
        magician1 = magician(370, 395, 70, 78)  # 마법사
        dealer_ctime = 1 #쿨타임초기화
        healer_ctime = 1
        tanker_ctime = 1
        magician_ctime = 1
        character_list = [dealer1, healer1, tanker1, magician1]  # 몬스터가 자동공격할때 필요
        monster_1 = com_monster(730, 320, 100, 129)  # 몬스터1
        monster_2 = com_monster(600, 350, 100, 116)  # 몬스터2
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN: #다음스테이지 도전
                if stage_button.isOver(pos):
                    start_screen = False
                    game_screen = True
                    option_screen = False
                    stage_screen = False
                    win_screen = False
                    lose_screen = False
                    stage_level += 1

            if event.type == pygame.MOUSEBUTTONDOWN: #메인화면
                if stage_exit.isOver(pos):
                    start_screen = True
                    game_screen = False
                    option_screen = False
                    stage_screen = False
                    win_screen = False
                    lose_screen = False
                    stage_level += 1

    if lose_screen == True:
        screen.blit(white, (0, 0))
        screen.blit(play_button, (stage_button.x, stage_button.y))
        screen.blit(exit_button, (stage_exit.x, stage_exit.y))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, BLACK)
        screen.blit(currentcoin, (15, 15))
        dealer1 = dealer(60, 350, 70, 78)  # 딜러
        healer1 = healer(150, 380, 70, 78)  # 힐러
        tanker1 = tanker(230, 365, 70, 78)  # 탱커
        magician1 = magician(370, 395, 70, 78)  # 마법사
        dealer_ctime = 1 #쿨타임초기화
        healer_ctime = 1
        tanker_ctime = 1
        magician_ctime = 1
        character_list = [dealer1, healer1, tanker1, magician1]  # 몬스터가 자동공격할때 필요
        monster_1 = com_monster(730, 320, 100, 129)  # 몬스터1
        monster_2 = com_monster(600, 350, 100, 116)  # 몬스터2
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 해당스테이지 재도전
                if stage_button.isOver(pos):
                    start_screen = False
                    game_screen = True
                    option_screen = False
                    stage_screen = False
                    win_screen = False
                    lose_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # 메인화면
                if stage_exit.isOver(pos):
                    start_screen = True
                    game_screen = False
                    option_screen = False
                    stage_screen = False
                    win_screen = False
                    lose_screen = False

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