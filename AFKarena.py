import sys
import pygame
import random
from pygame.locals import QUIT
from button import *
from player import *
from bar import *
from monster import *
from image_load import *

pygame.init()
display_width = 1024
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("AFK arena")
background = pygame.image.load('startbg.png')
dungeon = pygame.image.load('bg1.png')

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

def main_view():
    global start_screen, game_screen, option_screen, d_button, t_button, h_button, m_button
    global dealer_ctime, healer_ctime, tanker_ctime, magician_ctime  #기술들 쿨타임
    global dealer_skill, healer_skill, tanker_skill, magician_skill  #쿨타임 만들 때 필요한 리스트
    global dealer_auto, healer_auto, tanker_auto, magician_auto      #캐릭터가 자동공격 만들때 필요
    global dauto_list, hauto_list, tauto_list, mauto_list            #캐릭터가 자동공격 만들때 필요
    global m1_auto, m2_auto, m1_list, m2_list, character_list        #몬스터가 자동공격 할 때 필요
    global CurrentImage

    if start_screen is True:
        screen.blit(background, (0, 0))
        screen.blit(play_button, (playButton.x, playButton.y))
        screen.blit(option_button, (optionButton.x, optionButton.y))
        screen.blit(exit_button, (exitButton.x, exitButton.y))
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
        screen.blit(charBar, (bar.x, bar.y, bar.width, bar.height))
        screen.blit(dealerBar_button, (dealerBarButton.x, dealerBarButton.y))
        screen.blit(tankerBar_button, (tankerBarButton.x, tankerBarButton.y))
        screen.blit(healerBar_button, (healerBarButton.x, healerBarButton.y))
        screen.blit(magicianBar_button, (magicianBarButton.x, magicianBarButton.y))
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
        
            

        if d_button == True:
            screen.blit(d_select_button, (d_selectButton.x, d_selectButton.y))
        if t_button == True:
            screen.blit(t_select_button, (t_selectButton.x, t_selectButton.y))    
        if h_button == True:
            screen.blit(h_select_button, (h_selectButton.x, h_selectButton.y))
        if m_button == True:
            screen.blit(m_select_button, (m_selectButton.x, m_selectButton.y))


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
            a = random.choice(character_list)
            a.health -= 3
            m1_list.pop()
            m1_auto = 10
            print(dealer1.health, healer1.health, tanker1.health, magician1.health)
        
        if len(m2_list) == 1 and monster_2.health > 0:             #몬스터2(피가 0보다클 때)가 캐릭터를 자동공격
            for i in character_list:
                if i.health <= 0:
                    character_list.remove(i)
            a = random.choice(character_list)
            a.health -= 3
            m2_list.pop()
            m2_auto = 10
            print(dealer1.health, healer1.health, tanker1.health, magician1.health)
        
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
        
        if dealer_ctime == 0:               #쿨타임이 0일 때 스킬 쿨타임종료                   
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
                if e.key == ord('q') and len(dealer_skill) == 1 and dealer1.health > 0: #딜러가 스킬쓸 때 몬스터 체력 닳게
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
                    else:
                        a_monster = random.choice([monster_1,monster_2])
                        a_monster.health -= dealer1.amount_of_attack
                    print(monster_1.health, monster_2.health)
                    dealer_skill.pop()
                    dealer_ctime = 100
                    print('스킬 쿨타임 시작')
                
                if e.key == ord('w') and len(healer_skill) == 1 and healer1.health > 0:                
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
                
                if e.key == ord('e') and len(tanker_skill) == 1 and tanker1.health > 0:
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
                
                if e.key == ord('r') and len(magician_skill) == 1 and magician1.health > 0:
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
            
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if playButton.isOver(pos):
                    start_screen = False
                    game_screen = True

                if dealerBarButton.isOver(pos):
                    d_button = True
                    t_button = False
                    h_button = False
                    m_button = False

                if tankerBarButton.isOver(pos):
                    t_button = True
                    d_button = False
                    h_button = False
                    m_button = False

                if healerBarButton.isOver(pos):
                    h_button = True
                    t_button = False
                    d_button = False 
                    m_button = False

                if magicianBarButton.isOver(pos):
                    m_button = True
                    h_button = False
                    t_button = False
                    d_button = False
                    
    if option_screen is True:                 #옵션스크린일때
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
        main_view()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
if __name__ == '__main__':
    main()