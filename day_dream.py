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

#주인공 클래스 작성
class Player:
    playerpos = [0, height / 2] #주인공 초기 위치
    character_x_pos = 0
    character_y_pos = height / 2
    character_to_x_LEFT=0
    character_to_x_RIGHT=0
    character_to_y_up = 0
    character_to_y_down = 0
    width, height = 1920, 1080
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path1 + '\\character_image\\dummy.png')) #주인공 그림을 받아옴
        self.character_size = self.image.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.image = pygame.transform.scale(self.image, (self.character_width, self.character_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.character_x_pos
        self.rect.centery = self.character_y_pos
        self.mentality = 0      #주인공 정신도 수준

    def draw(self, event_list):
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.character_x_pos
        self.rect.centery = self.character_y_pos
        # 수정1 : 기존의 character_to_x 를 왼쪽 방향, 오른쪽 방향 변수 2개로 나눔
        for event in event_list:

            # 수정2 : 키를 누를 때 LEFT, RIGHT 에 따라 서로 다른 변수의 값 조정
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.character_to_x_LEFT -= 2 # 바뀐 부분
                elif event.key == pygame.K_d:
                    self.character_to_x_RIGHT += 2 # 바뀐 부분

                elif event.key == pygame.K_s:
                    self.character_to_y_up += 2 # 바뀐 부분
                elif event.key == pygame.K_w:
                    self.character_to_y_down -= 2 # 바뀐 부분

            # 수정3 : 키에서 손을 뗄 때 LEFT, RIGHT 를 각각 처리
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a: # 이 부분은 모두 다 바뀜
                    self.character_to_x_LEFT = 0
                elif event.key == pygame.K_d:
                    self.character_to_x_RIGHT = 0
                elif event.key == pygame.K_s:
                    self.character_to_y_up = 0
                elif event.key == pygame.K_w:
                    self.character_to_y_down = 0
  

        # 수정4 : 두 변수의 값을 모두 더함
        self.character_x_pos += self.character_to_x_LEFT + self.character_to_x_RIGHT
        self.character_y_pos += self.character_to_y_up + self.character_to_y_down
        screen.blit(self.image, (self.character_x_pos, self.character_y_pos))

        if self.character_x_pos < 0:
            self.character_x_pos = 0
        elif self.character_x_pos > width - self.character_width:
            self.character_x_pos = width - self.character_width

        if self.character_y_pos < 0:
            self.character_y_pos = 0
        elif self.character_y_pos > height - self.character_height:
            self.character_y_pos = height - self.character_height


#의사 클래스 작성
class Doctor:
    doctorpos = [1600, height / 2] #의사 초기 위치
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path,current_path1 + '\\character_image\\sub_dummy.png')) #의사의 이미지를 불러옴
        self.doctor_size = self.image.get_rect().size
        self.doctor_width = self.doctor_size[0]
        self.doctor_height = self.doctor_size[1]
        self.image = pygame.transform.scale(self.image, (self.doctor_width, self.doctor_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.doctorpos[0]
        self.rect.centery = self.doctorpos[1]
    def draw(self):      
        screen.blit(self.image, self.doctorpos)      #의사를 초기위치에 그림

#오브젝트클래스 작성
class Objecter:
    def draw(self,image ,image_size, objecter_xpos, objecter_ypos, event_list):
        if image_size == False:
            screen.blit(image,(objecter_xpos, objecter_ypos))
        
        else:
            objecter_width = image_size[0]
            objecter_height = image_size[1]
            image = pygame.transform.scale(image, (objecter_width, objecter_height))
            rect = image.get_rect()  
            rect.centerx = objecter_xpos
            rect.centery = objecter_ypos
            if pygame.sprite.collide_rect(Player(), Objecter()):
                for event in event_list:

                    # 수정2 : 키를 누를 때 LEFT, RIGHT 에 따라 서로 다른 변수의 값 조정
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            Player().character_x_pos = objecter_xpos - 64 # 바뀐 부분
                        elif event.key == pygame.K_d:
                            Player().character_x_pos = objecter_xpos + 64 # 바뀐 부분

                        elif event.key == pygame.K_s:
                            Player().character_y_pos = objecter_ypos - 64 # 바뀐 부분
                        elif event.key == pygame.K_w:
                            Player().character_y_pos = objecter_ypos + 64
            screen.blit(image,(objecter_xpos, objecter_ypos))


#타이머 클래스 작성
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

#버튼 클래스 작성
class Button:
    def __init__(self,event_list,image_in,x,y,width,height,image_act,x_act,y_act,click):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(image_act,(x_act, y_act))
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        screen.blit(click,(x_act, y_act))
                        pygame.display.update()
                        time.sleep(0.2)
                        Comu(1)
        else:
            screen.blit(image_in, (x,y))
#버튼 이벤트 작성

def Comu(map_lotate):
    community_box = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\comunity.png'))
    end23 = False
    while map_lotate == 1:
        screen.blit(community_box, (0, 0))
        event_list = pygame.event.get()
        
        #게임 종료
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        #대화 넘김
        for event in event_list:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP_ENTER:
                    break
        pygame.display.update()

        
        

    
    
        
def main(map_lotate):
    running = 1
    doctor = Doctor()
    user = Player()
    timer = Timer()
    objecter = Objecter()
    timer.start()
    doctor_meat = 0
    comu_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\community_box.png'))
    comu_button_size = comu_image.get_rect().size
    comu_width = comu_button_size[0]
    comu_height = comu_button_size[1]
    click_comu_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\click_community_box.png'))
    click_tocomu_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\community_box_click.png'))
    desk_image =  pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\desk.png'))
    flower_pot = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\flowerpot.png'))
    desk_image_size = desk_image.get_rect().size
    flower_pot_size = flower_pot.get_rect().size
    while running:
        #게임 종료
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if map_lotate == 0:

            screen.blit(background, (0,0))

            objecter.draw(desk_image,desk_image_size, 1320, 340, event_list)
            objecter.draw(flower_pot,flower_pot_size, 5, 1013, event_list)
            objecter.draw(flower_pot ,flower_pot_size, 5, 8, event_list)
            doctor.draw()
            user.draw(event_list)

            if pygame.sprite.collide_rect(user, doctor):
                    doctor_meat = 1
            else:
                doctor_meat = 0

            if doctor_meat == 1:
                community = Button(event_list, comu_image,1664, height / 2 - 128, comu_width, comu_height, click_comu_image,1664,height / 2 - 128, click_tocomu_image)

        pygame.display.update()
                
main(0) 