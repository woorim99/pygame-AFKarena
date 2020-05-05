import sys
import pygame
import random
from pygame.locals import QUIT
from button import *
from player import *
from monster import *
from image_load import *

pygame.init()
display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("AFK arena")
background = pygame.image.load('startbg.png')
dungeon = pygame.image.load('bg1.png')

black_display = pygame.image.load('black_whole.png')              #win screen, lose screen 배경
q_key = pygame.image.load('key_q.png')                            #q 키보드
e_key = pygame.image.load('key_e.png')                            #e 키보드
w_key = pygame.image.load('key_w.png')                            #w 키보드
r_key = pygame.image.load('key_r.png')                            #r 키보드
black_key = pygame.image.load('black_key.png')                    #키보드 크기 까만네모(쓰는데 필요없을듯)
option_background = pygame.image.load('option_bg.png')            #option screen배경
level_up = pygame.image.load('levelup.png')                       #level up 버튼
stage_background = pygame.image.load('stage_bg.png')              #stage screen 배경
back = pygame.image.load('back.png')                              #빨간색 back버튼
play = pygame.image.load('red_play.png')                          #빨간색 play 버튼


q_skill = pygame.image.load('q_skill.png')
white = pygame.image.load('white.png')
black = pygame.image.load('black.png')
lose = pygame.image.load('lose.png')
win = pygame.image.load('win.png')

s1 = pygame.image.load('ch1_moving1.png')
s2 = pygame.image.load('ch1_moving2.png')
s3 = pygame.image.load('ch1_moving1.png')
character5=[pygame.image.load('mehira_skill/mehira_skill'+str(i)+'.png') for i in range(55)]

BLACK = (0, 0, 0)         #체력바 만들 때필요

pygame.mixer.music.load('bgmusic.mp3')       #배경음악
pygame.mixer.music.play(-1)                  #배경음악 끝나면 다시재생
clock = pygame.time.Clock()

dealer_skill = []                       #스킬 쿨타임 만들때 필요한 리스트
healer_skill = []
tanker_skill = []
magician_skill = []

dealer_ctime = 1                        #스킬 쿨타임 초기값                                          
healer_ctime = 1
tanker_ctime = 1
magician_ctime = 1

dauto_list = []                         #캐릭터가 자동공격 할 때 필요
hauto_list = []
tauto_list = []
mauto_list = []

dealer_auto = 1                         #캐릭터가 자동공격 할 때 필요
healer_auto = 1
tanker_auto = 1
magician_auto = 1

m1_list = []                             #몬스터가 자동공격 할 때 필요
m2_list = []

m1_auto = 1                              #몬스터가 자동공격 할 때 필요
m2_auto = 1

CurrentImage = 1


def game():
    global start_screen, game_screen, option_screen, stage_screen, win_screen, lose_screen
    global dealer_ctime, healer_ctime, tanker_ctime, magician_ctime  #기술들 쿨타임
    global dealer_skill, healer_skill, tanker_skill, magician_skill  #쿨타임 만들 때 필요한 리스트
    global dealer_auto, healer_auto, tanker_auto, magician_auto      #캐릭터가 자동공격 만들때 필요
    global dauto_list, hauto_list, tauto_list, mauto_list            #캐릭터가 자동공격 만들때 필요
    global m1_auto, m2_auto, m1_list, m2_list, character_list       #몬스터가 자동공격 할 때 필요
    global dealer_level, healer_level, tanker_level, magician_level, stage_level
    global dealer1, healer1, tanker1, magician1, monster_1, monster_2, coin, BLACK
    global CurrentImage

    if start_screen is True:
        screen.blit(background, (0, 0))
        screen.blit(play_button, (playButton.x, playButton.y))
        screen.blit(option_button, (optionButton.x, optionButton.y))
        screen.blit(exit_button, (exitButton.x, exitButton.y))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin : ' + str(int(coin)), True, (255, 255, 255))
        screen.blit(currentcoin, (15, 15))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.isOver(pos):
                    start_screen = False
                    stage_screen = True
                    
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionButton.isOver(pos):
                    start_screen = False
                    option_screen = True  
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitButton.isOver(pos):
                    pygame.quit()
                    sys.exit()

    if stage_screen is True:               #스테이지 정보알리기
        screen.blit(stage_background, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentStage = largeFont.render('STAGE:' + str(stage_level), True, (255, 255, 255))
        screen.blit(currentStage, (850, 15))
        screen.blit(play, (stage_play.x, stage_play.y))
        screen.blit(back, (stage_back.x, stage_back.y))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage_play.isOver(pos):
                    stage_screen = False
                    game_screen = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if stage_back.isOver(pos):
                    stage_screen = False
                    start_screen = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

                        
    if game_screen is True:
        screen.blit(dungeon, (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentStage = largeFont.render('STAGE :' + str(stage_level), True, (255, 255, 255))
        screen.blit(currentStage, (850, 15))
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, (255, 255, 255))
        screen.blit(currentcoin, (15, 15))
        dealer1.health_bar()
        healer1.health_bar()
        tanker1.health_bar()
        magician1.health_bar()
        monster_1.health_bar()
        monster_2.health_bar()

        if (CurrentImage==1):
            screen.blit(s1, (dealer1.x, dealer1.y))
            screen.blit(s1, (healer1.x, healer1.y))
            screen.blit(s1, (tanker1.x, tanker1.y))
            screen.blit(s1, (magician1.x, magician1.y))
            screen.blit(s1, (monster_1.x, monster_1.y))
            screen.blit(s1, (monster_2.x, monster_2.y))
        if (CurrentImage==2):
            screen.blit(s2, (dealer1.x, dealer1.y))
            screen.blit(s2, (healer1.x, healer1.y))
            screen.blit(s2, (tanker1.x, tanker1.y))
            screen.blit(s2, (magician1.x, magician1.y))
            screen.blit(s2, (monster_1.x, monster_1.y))
            screen.blit(s2, (monster_2.x, monster_2.y))            

        if (CurrentImage==3):
            screen.blit(s3, (dealer1.x, dealer1.y))
            screen.blit(s3, (healer1.x, healer1.y))
            screen.blit(s3, (tanker1.x, tanker1.y))
            screen.blit(s3, (magician1.x, magician1.y))
            screen.blit(s3, (monster_1.x, monster_1.y))
            screen.blit(s3, (monster_2.x, monster_2.y))            
            CurrentImage=1
        else:
            CurrentImage+=1
        
            


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
                print('딜러체력 :',dealer1.health, '힐러체력 :', healer1.health, '탱커체력 :', tanker1.health, '마법사체력 :',magician1.health)

            else:
                game_screen = False   
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
                print('딜러체력 :',dealer1.health, '힐러체력 :', healer1.health, '탱커체력 :', tanker1.health, '마법사체력 :',magician1.health)

            else:
                game_screen = False  
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
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health > 0 and monster_2.health <= 0:
                    monster_1.health -= 1
                    dauto_list.pop()
                    dealer_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)
                
                elif monster_1.health < 0 and monster_2.health < 0:
                    game_screen = False 
                    win_screen = True

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    dauto_list.pop()
                    dealer_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

        if len(hauto_list) == 1:                #힐러(피가 0보다클때)가 몬스터를 자동공격  
            if healer1.health > 0:
                if monster_1.health <= 0 and monster_2.health > 0:
                    monster_2.health -= 1
                    hauto_list.pop()
                    healer_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health > 0 and monster_2.health <= 0:
                    monster_1.health -= 1
                    hauto_list.pop()
                    healer_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health < 0 and monster_2.health < 0:
                    game_screen = False
                    win_screen = True


                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    hauto_list.pop()
                    healer_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

        if len(tauto_list) == 1:                  #탱커(피가 0보다클때)가 몬스터를 자동공격
            if tanker1.health > 0:
                if monster_1.health <= 0 and monster_2.health > 0:
                    monster_2.health -= 1
                    tauto_list.pop()
                    tanker_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health > 0 and monster_2.health <= 0:
                    monster_1.health -= 1
                    tauto_list.pop()
                    tanker_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health < 0 and monster_2.health < 0:
                    game_screen = False
                    win_screen = True

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    tauto_list.pop()
                    tanker_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)


        if len(mauto_list) == 1:                   #마법사(피가 0보다클때)가 몬스터를 자동공격
            if magician1.health > 0:
                if monster_1.health <= 0 and monster_2.health > 0:
                    monster_2.health -= 1
                    mauto_list.pop()
                    magician_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health > 0 and monster_2.health <= 0:
                    monster_1.health -= 1
                    mauto_list.pop()
                    magician_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)

                elif monster_1.health < 0 and monster_2.health < 0:
                    game_screen = False
                    win_screen = True

                else:
                    a = random.choice([monster_1, monster_2])
                    a.health -= 1
                    mauto_list.pop()
                    magician_auto = 10
                    print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)
        
        dealer_ctime -= 1                     #캐릭터 스킬('q', 'w', 'e', 'r') 쿨타임에필요
        healer_ctime -= 1
        tanker_ctime -= 1
        magician_ctime -= 1
        
        if dealer_ctime == 0:               #쿨타임이 0일 때 스킬 쿨타임종료                   
            dealer_skill.append('O')
            print('딜러스킬 쿨타임 종료')
            screen.blit(q_key, (100, 530))
        if healer_ctime == 0:
            healer_skill.append('O')
            print('힐러스킬 쿨타임 종료')
            screen.blit(w_key, (170, 530))
        if tanker_ctime == 0:
            tanker_skill.append('O')
            print('탱커스킬 쿨타임 종료')
            screen.blit(e_key, (240, 530))
        if magician_ctime == 0:
            magician_skill.append('O')
            print('마법사 스킬 쿨타임 종료')
            screen.blit(r_key, (310, 530))

        for event in pygame.event.get():                
            if event.type == pygame.QUIT:                
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYUP:
                if event.key == ord('q') and len(dealer_skill) == 1 and dealer1.health > 0: #딜러가 스킬쓸 때 몬스터 체력 닳게
                    for i in character5:
                        screen.blit(i, (monster_1.x, monster_1.y))
                        pygame.display.update()
                        screen.blit(dungeon, (0,0))
                        screen.blit(character3, (dealer1.x, dealer1.y))
                        screen.blit(character1, (healer1.x, healer1.y))
                        screen.blit(character2, (magician1.x, magician1.y))
                        screen.blit(character4, (tanker1.x, tanker1.y))
                        screen.blit(monster1, (monster_1.x, monster_1.y))
                        screen.blit(monster2, (monster_2.x, monster_2.y))
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= dealer1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= dealer1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        game_screen = False
                        win_screen = True
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= dealer1.amount_of_attack
                        print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)
                    dealer_skill.pop()
                    dealer_ctime = 100
                    print('스킬 쿨타임 시작')
                    screen.blit(black_key, (100, 530))
                
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
                    screen.blit(black_key, (170, 530))
                
                if event.key == ord('e') and len(tanker_skill) == 1 and tanker1.health > 0:
                    tanker1.draw(star)                                     #탱커가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= tanker1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= tanker1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        game_screen = False
                        win_screen = True
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= tanker1.amount_of_attack
                        print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)
                    tanker_skill.pop()
                    tanker_ctime = 100
                    print('스킬 쿨타임 시작')
                    screen.blit(black_key, (240, 530))
                
                if event.key == ord('r') and len(magician_skill) == 1 and magician1.health > 0:
                    magician1.draw(star)                                #마법사가 스킬 쓸 때 몬스터 체력 닳게
                    if monster_1.health <= 0 and monster_2.health >= 0:
                        monster_2.health -= magician1.amount_of_attack
                    elif monster_1.health > 0 and monster_2.health <= 0:
                        monster_1.health -= magician1.amount_of_attack
                    elif monster_1.health < 0 and monster_2.health < 0:
                        game_screen = False
                        win_screen = True
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= magician1.amount_of_attack
                        print('몬스터1체력 :', monster_1.health, '몬스터2체력 :', monster_2.health)
                    magician_skill.pop()
                    magician_ctime = 100
                    print('스킬 쿨타임 시작')
                    screen.blit(black_key, (310, 530))
              
            
                    
    if option_screen is True:                 #옵션스크린일때
        screen.blit(option_background, (0, 0))
        screen.blit(back, (op_back.x, op_back.y))
        screen.blit(level_up, (dealer_levelup.x, dealer_levelup.y))
        screen.blit(level_up, (healer_levelup.x, healer_levelup.y))
        screen.blit(level_up, (tanker_levelup.x, tanker_levelup.y))
        screen.blit(level_up, (magician_levelup.x, magician_levelup.y))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, (255,255,255))
        screen.blit(currentcoin, (15, 15))
        d_level = largeFont.render('dealer level :' + str(int(dealer_level)), True, (255, 255, 255))
        h_level = largeFont.render('healer level :' + str(int(healer_level)), True, (255, 255, 255))
        t_level = largeFont.render('tanker level :' + str(int(tanker_level)), True, (255, 255, 255))
        m_level = largeFont.render('magician level :' + str(int(magician_level)), True, (255, 255, 255))
        screen.blit(d_level, (300, 90))
        screen.blit(h_level, (300, 210))
        screen.blit(t_level, (300, 330))
        screen.blit(m_level, (300, 450))
        d_coin = largeFont.render('You need ' + str(int(dealer_level * 10)) + ' coins', True, (255, 255, 255))
        h_coin = largeFont.render('You need ' + str(int(healer_level * 10)) + ' coins', True, (255, 255, 255))
        t_coin = largeFont.render('You need ' + str(int(tanker_level * 10)) + ' coins', True, (255, 255, 255))
        m_coin = largeFont.render('You need ' + str(int(magician_level * 10)) + ' coins', True, (255, 255, 255))
        screen.blit(d_coin, (300, 140))
        screen.blit(h_coin, (300, 260))
        screen.blit(t_coin, (300, 380))
        screen.blit(m_coin, (300, 500))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dealer_levelup.isOver(pos):
                    if coin >= dealer_level * 10:
                        coin -= dealer_level * 10
                        dealer_level += 1
                        dealer1 = dealer(60, 350, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if healer_levelup.isOver(pos):
                    if coin >= healer_level * 10:
                        coin -= healer_level * 10
                        healer_level += 1
                        healer1 = healer(150, 380, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tanker_levelup.isOver(pos):
                    if coin >= tanker_level * 10:
                        coin -= tanker_level * 10
                        tanker_level += 1
                        tanker1 = tanker(230, 365, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if magician_levelup.isOver(pos):
                    if coin >= magician_level * 10:
                        coin -= magician_level * 10
                        magician_level += 1
                        magician1 = magician(370, 395, 70, 78)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if op_back.isOver(pos):
                    character_list = [dealer1, healer1, tanker1, magician1]
                    option_screen = False
                    start_screen = True

    if win_screen == True:
        screen.blit(black_display, (0, 0))
        screen.blit(win, (100, 100))
        screen.blit(play, (stage_play.x, stage_play.y)) 
        screen.blit(back, (stage_back.x, stage_back.y)) #exit
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, (255, 255, 255))
        screen.blit(currentcoin, (15, 15))
        BigFont = pygame.font.SysFont('comicsans', 80)
        newcoin = BigFont.render('Coin += ' + str(int(25 * (stage_level ** 0.5))), True, (255, 255, 255))
        screen.blit(newcoin, (120, 210))
        for event in pygame.event.get(): 
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN: #다음스테이지 도전
                if stage_play.isOver(pos):
                    coin += int(25 * (stage_level ** 0.5))
                    stage_level += 1
                    pygame.time.delay(10)
                    dealer1 = dealer(60, 350, 70, 78)  # 딜러
                    healer1 = healer(150, 380, 70, 78)  # 힐러
                    tanker1 = tanker(230, 365, 70, 78)  # 탱커
                    magician1 = magician(370, 395, 70, 78)  # 마법사
                    dealer_ctime = 1 #쿨타임초기화
                    healer_ctime = 1
                    tanker_ctime = 1
                    magician_ctime = 1
                    character_list = [dealer1, dealer1, healer1, tanker1, tanker1, tanker1, magician1, magician1] #몬스터가 자동공격할때 필요(맞을확률)
                    monster_1 = com_monster(730, 320, 100, 129)  # 몬스터1
                    monster_2 = com_monster(600, 350, 100, 116)  # 몬스터2
                    win_screen = False
                    game_screen = True

            if event.type == pygame.MOUSEBUTTONDOWN: #메인화면
                if stage_back.isOver(pos):
                    coin += int(25 * (stage_level ** 0.5))
                    stage_level += 1
                    pygame.time.delay(10)
                    dealer1 = dealer(60, 350, 70, 78)  # 딜러
                    healer1 = healer(150, 380, 70, 78)  # 힐러
                    tanker1 = tanker(230, 365, 70, 78)  # 탱커
                    magician1 = magician(370, 395, 70, 78)  # 마법사
                    dealer_ctime = 1 #쿨타임초기화
                    healer_ctime = 1
                    tanker_ctime = 1
                    magician_ctime = 1
                    character_list = [dealer1, dealer1, healer1, tanker1, tanker1, tanker1, magician1, magician1] #몬스터가 자동공격할때 필요(맞을확률)
                    monster_1 = com_monster(730, 320, 100, 129)  # 몬스터1
                    monster_2 = com_monster(600, 350, 100, 116)  # 몬스터2
                    win_screen = False
                    start_screen = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    if lose_screen == True:
        screen.blit(black_display, (0, 0))
        screen.blit(lose, (100, 100))
        screen.blit(play, (stage_play.x, stage_play.y))
        screen.blit(back, (stage_back.x, stage_back.y))
        largeFont = pygame.font.SysFont('comicsans', 40)
        currentcoin = largeFont.render('Coin :' + str(int(coin)), True, (255, 255, 255))
        screen.blit(currentcoin, (15, 15))
        dealer1 = dealer(60, 350, 70, 78)  # 딜러
        healer1 = healer(150, 380, 70, 78)  # 힐러
        tanker1 = tanker(230, 365, 70, 78)  # 탱커
        magician1 = magician(370, 395, 70, 78)  # 마법사
        dealer_ctime = 1 #쿨타임초기화
        healer_ctime = 1
        tanker_ctime = 1
        magician_ctime = 1
        character_list = [dealer1, dealer1, healer1, tanker1, tanker1, tanker1, magician1, magician1] #몬스터가 자동공격할때 필요(맞을확률)
        monster_1 = com_monster(730, 320, 100, 129)  # 몬스터1
        monster_2 = com_monster(600, 350, 100, 116)  # 몬스터2
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 해당스테이지 재도전
                if stage_play.isOver(pos):
                    lose_screen = False 
                    game_screen = True   

            if event.type == pygame.MOUSEBUTTONDOWN:  # 메인화면
                if stage_back.isOver(pos):
                    lose_screen = False
                    start_screen = True

            if event.type == QUIT:
                pygame.quit()
                sys.exit()             

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


