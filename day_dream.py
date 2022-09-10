#불러오기
from http.cookiejar import CookieJar
import sys
from turtle import back
import pygame
#배경 그림 가져오기
background = pygame.image.load("C:\\Users\\plant\\Desktop\\한양대 대회\\git_programs\\bg_image\\test.png")

# 게임구성
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
pygame.display.set_caption("day dream")
pygame.display.update()

#주인공 캐릭터 가져오기
main_character = pygame.image.load("C:\\Users\\plant\\Desktop\\한양대 대회\\git_programs\\character_image\\dummy.png")
main_character_size = main_character.get_rect().size#캐릭터 이미지 크기 구해오기
main_character_width = main_character_size[0]
main_character_height = main_character_size[1]
main_x_pos = width / 2 - main_character_width
main_y_pos = height - main_character_height

#의사 캐릭터 가져오기
doctor_character = pygame.image.load("C:\\Users\\plant\\Desktop\\한양대 대회\\git_programs\\character_image\\sub_dummy.png")
doctor_character_size = doctor_character.get_rect().size
doctor_character_width = doctor_character_size[0]
doctor_character_height = doctor_character_size[1]
doctor_x_pos = width / 2 + width / 4
doctor_y_pos = height / 2

#의사와 주인공 상호작용
doctor_meet_main = False

#주인공 캐릭터 위치 이동
main_to_x = 0
main_to_y = 0

# 게임반복
while  True:
    
    screen.blit(background, (0, 0))  #배경 색
    
    screen.blit(main_character, (main_x_pos, main_y_pos))

    screen.blit(doctor_character, (doctor_x_pos, doctor_y_pos))
    for event in pygame.event.get():
        #게임 종료
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        #주인공 캐릭터 움직임
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if main_to_x == 5:
                    main_to_x = 0
                main_to_x -= 5
            elif event.key == pygame.K_d:
                if main_to_x == -5:
                    main_to_x = 0
                main_to_x += 5
            elif event.key == pygame.K_w:
                if main_to_y == 5:
                    main_to_y = 0
                main_to_y -= 5
            elif event.key == pygame.K_s:
                if main_to_y == -5:
                    main_to_y = 0
                main_to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if main_to_x == 5:
                    continue
                main_to_x = 0
            
            elif event.key == pygame.K_d:
                if main_to_x == -5:
                    continue
                main_to_x = 0
            elif event.key == pygame.K_w:
                if main_to_y == 5:
                    continue
                main_to_y = 0
            elif event.key == pygame.K_s:
                if main_to_y == -5:
                    continue
                main_to_y = 0
    main_x_pos += main_to_x
    main_y_pos += main_to_y
    #주인공 의사 충돌 확인
    if doctor_x_pos - main_x_pos < 64 and doctor_y_pos - main_y_pos < 64:
        print("의사 : 왔는가")
        doctor_meet_main = True

    if doctor_x_pos - main_x_pos > 64 and doctor_y_pos - main_y_pos > 64:
        doctor_meet_main = False

    if doctor_meet_main == False:
        print("의사와 대화해 보자")

    if doctor_meet_main == True:
        print("서사")
    
#게임반복 뒤

    pygame.display.flip()
    fpsClock.tick(fps)