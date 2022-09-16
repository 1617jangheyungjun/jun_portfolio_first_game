from tkinter import Y
import pygame,os,math,random,time,sys
from pygame.locals import *
#os 오류 해결용
current_path1 = os.getcwd()
#아이콘 그림 가져오기
game_icon = pygame.image.load("icon\\icon.png")
#배경 그림 가져오기
background = pygame.image.load("bg_image\\test.png")
sub_background = pygame.image.load("bg_image\\2test.png")
# 게임구성
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
pygame.display.set_caption("** day dream **")
pygame.display.update()
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

class Player:
    playerpos = [0, height / 2] #주인공 초기 위치
    move_x = 0
    move_y = 0
    
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path1 + "\\character_image\\dummy.png")) #주인공 그림을 받아옴
        self.rect = pygame.Rect(self.image.get_rect())      #주인공을 사각형으로 받음
        self.mentality = 0      #주인공 정신도 수준

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if self.move_x == 5:
                        self.move_x = 0
                    self.move_x -= 5
                elif event.key == pygame.K_d:
                    if self.move_x == -5:
                        self.move_x = 0
                    self.move_x += 5
                elif event.key == pygame.K_w:
                    if self.move_y == 5:
                        self.move_y = 0
                    self.move_y -= 5
                elif event.key == pygame.K_s:
                    if self.move_y == -5:
                        self.move_y = 0
                    self.move_y += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    if self.move_x == 5:
                        continue
                    self.move_x = 0
                
                elif event.key == pygame.K_d:
                    if self.move_x == -5:
                        continue
                    self.move_x = 0
                elif event.key == pygame.K_w:
                    if self.move_y == 5:
                        continue
                    self.move_y = 0
                elif event.key == pygame.K_s:
                    if self.move_y == -5:
                        continue
                    self.move_y = 0
        self.playerpos = [self.playerpos[0] + self.move_x, self.playerpos[1] + self.move_y]
        screen.blit(self.image, self.playerpos)

class Doctor:
    doctorpos = [1800, height / 2] #의사 초기 위치
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path,current_path1 + '\\character_image\\sub_dummy.png')) #의사의 이미지를 불러옴
        self.rect = pygame.Rect(self.image.get_rect()) #의사 이미지를 사각형으로 받음
    def draw(self):      
        screen.blit(self.image, self.doctorpos)      #의사를 초기위치에 그림

class Timer:
    def __init__(self):
        self.elapsed = 0.0 #경과시간 저장
        self.running = False   #진행중인가를 나타냄
        self.last_start_time = None #현재시간 받는 변수(초기화 하기위해서 None타입이로둠)

    def start(self):
        if not self.running:  
            self.running = True
            self.last_start_time = time.time()   #게임이 실행중이라면 현재의 시간을 받음

    def get_elapsed(self):
        elapsed = self.elapsed
        if self.running:
            elapsed += time.time() - self.last_start_time #현재 새로운 시간을 받고 그 시간에서 마지막 시간을 뺴서 몇초가 남았는지 elapsed에 저장 경과됨 시간 반환

        return elapsed

def main():
    running = 1
    doctor = Doctor()
    user = Player()
    map_lotate = 0


    timer = Timer()
    timer.start()

    while running:
        #게임 종료
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if map_lotate == 0:

            screen.blit(background, (0,0))

            doctor.draw()
            user.draw()
        pygame.display.update()
main()