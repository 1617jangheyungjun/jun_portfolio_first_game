from tkinter import Y
import pygame,os,math,random,time,sys
from pygame.locals import *
#os 오류 해결용
current_path1 = os.getcwd()
#아이콘 그림 가져오기
game_icon = pygame.image.load("icon\\icon.png")
#배경 그림 가져오기
background = pygame.image.load("bg_image\\test.png")

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
    clock = pygame.time.Clock()
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
        self.forin = 0
    def draw(self, event_list):
        dt = self.clock.tick(60)
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.character_x_pos
        self.rect.centery = self.character_y_pos
        # 수정1 : 기존의 character_to_x 를 왼쪽 방향, 오른쪽 방향 변수 2개로 나눔
        for event in event_list:

            # 수정2 : 키를 누를 때 LEFT, RIGHT 에 따라 서로 다른 변수의 값 조정
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.character_to_x_LEFT -= 0.4 # 바뀐 부분
                elif event.key == pygame.K_d:
                    self.character_to_x_RIGHT += 0.4 # 바뀐 부분

                elif event.key == pygame.K_s:
                    self.character_to_y_up += 0.4 # 바뀐 부분
                elif event.key == pygame.K_w:
                    self.character_to_y_down -= 0.4 # 바뀐 부분

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
        self.character_x_pos += self.character_to_x_LEFT * dt + self.character_to_x_RIGHT * dt
        self.character_y_pos += self.character_to_y_up * dt + self.character_to_y_down * dt
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
    def __init__(self,image ,image_size, objecter_xpos, objecter_ypos, event_list):
            
            self.objecter_width = image_size[0]
            self.objecter_height = image_size[1]
            self.image = pygame.transform.scale(image, (self.objecter_width, self.objecter_height))
            self.rect = self.image.get_rect()  
            self.objecter_xpos = objecter_xpos
            self.objecter_ypos = objecter_ypos
            self.rect.centerx = objecter_xpos
            self.rect.centery = objecter_ypos
            
    def draw(self):
        screen.blit(self.image,(self.objecter_xpos, self.objecter_ypos))

class Toilet:
    deskpos = [1408, 0] #책상 초기 위치
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet.png')) #의사의 이미지를 불러옴
        self.desk_size = self.image.get_rect().size
        self.desk_width = self.desk_size[0]
        self.desk_height = self.desk_size[1]
        self.image = pygame.transform.scale(self.image, (self.desk_width, self.desk_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.deskpos[0]
        self.rect.centery = self.deskpos[1]+20
    def draw(self):      
        screen.blit(self.image, self.deskpos)

class mental_icon:
    def draw(self, image1, image2, image3, mental_level):
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.mental_level = mental_level
        if mental_level == 1:
            screen.blit(self.image1, (1807, 64))
        elif mental_level == 2:
            screen.blit(self.image2, (1807, 64))
        elif mental_level == 3:
            screen.blit(self.image3, (1807, 64))

#버튼 클래스 작성
class Button:
    def __init__(self,event_list,image_in,x,y,width,height,image_act,x_act,y_act,click, action):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(image_act,(x_act, y_act))
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        screen.blit(click,(x_act, y_act))
                        pygame.display.update()
                        time.sleep(0.2)
                        if action == "Comu":
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame. K_RETURN:
                    ingame()
        pygame.display.update()

        
#인게임
def ingame():
    running = 1
    user = Player()
    event_list = pygame.event.get()
    washstand = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda.png'))
    washstand_size = washstand.get_rect().size
    toilet = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet.png'))
    toilet_size = toilet.get_rect().size
    ingame_background =  pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil.png'))
    ingame_background2 = pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil1.png'))
    ingame_background3 = pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil2.png'))
    washstand_object = Objecter(washstand,washstand_size ,87, 0, event_list)
    washstand2_object = Objecter(washstand,washstand_size ,275, 0, event_list)
    washstand3_object = Objecter(washstand,washstand_size ,462, 0, event_list)
    toilet_object = Objecter(toilet, toilet_size, 890, 0, event_list)
    toilet2_object = Objecter(toilet, toilet_size, 1149, 0, event_list)
    toilet3_object = Objecter(toilet, toilet_size, 1667, 0, event_list)
    mental1_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental1.png'))
    mental2_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental3.png'))
    mental3_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental2.png'))
    mental_level = 1
# 게임구성
    while running:
        #게임 종료
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_UP:
                    mental_level += 1
                elif event.key == pygame.K_DOWN:
                    mental_level -= 1
        
        if mental_level >= 3 or mental_level <= 0:
            if mental_level >= 3:
                mental_level = 3
            elif mental_level <= 0:
                mental_level = 1
        if mental_level == 1:
            screen.blit(ingame_background, (0,0))
        elif mental_level == 2:
            screen.blit(ingame_background2, (0, 0))
        elif mental_level == 3:
            screen.blit(ingame_background3, (0, 0))
        user.draw(event_list)
        washstand_object.draw()
        washstand2_object.draw()
        washstand3_object.draw()
        toilet_object.draw()
        toilet2_object.draw()
        toilet3_object.draw()
        mental_icon().draw(mental1_image, mental2_image, mental3_image, mental_level)
        Toilet().draw()
        pygame.display.update()
        if pygame.sprite.collide_rect(user, Toilet()):
            print("만남")

        else:
            print("안만남")

    
#메인화면
        
def main(map_lotate):
    event_list = pygame.event.get()
    running = 1
    doctor = Doctor()
    user = Player()
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
    desk_objecter = Objecter(desk_image,desk_image_size, 1320, 340, event_list)
    flower_pot_objecter = Objecter(flower_pot,flower_pot_size, 5, 1013, event_list)
    flower_pot_objecter2 = Objecter(flower_pot,flower_pot_size, 5, 0, event_list)
    mental1_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental1.png'))
    mental2_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental3.png'))
    mental3_image = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental2.png'))
    mental_level = 1
    while running:
        #게임 종료
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_UP:
                    mental_level += 1
                elif event.key == pygame.K_DOWN:
                    mental_level -= 1
        
        if mental_level >= 3 or mental_level <= 0:
            if mental_level >= 3:
                mental_level = 3
            elif mental_level <= 0:
                mental_level = 1
        if map_lotate == 0:
            screen.blit(background, (0,0))
            doctor.draw()
            user.draw(event_list)
            desk_objecter.draw()
            flower_pot_objecter.draw()
            flower_pot_objecter2.draw()
            
            mental_icon().draw(mental1_image, mental2_image, mental3_image, mental_level)


            for objecter in [desk_objecter, flower_pot_objecter, flower_pot_objecter2]:
                if pygame.sprite.collide_rect(user, objecter):
                    for event in event_list:
                        # 수정2 : 키를 누를 때 LEFT, RIGHT 에 따라 서로 다른 변수의 값 조정
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                user.character_x_pos = objecter.objecter_xpos + user.character_width # 바뀐 부분
                            elif event.key == pygame.K_d:
                                user.character_x_pos = objecter.objecter_xpos - user.character_width # 바뀐 부분

                            elif event.key == pygame.K_s:
                                user.character_y_pos = objecter.objecter_ypos - user.character_height # 바뀐 부분
                            elif event.key == pygame.K_w:
                                user.character_y_pos = objecter.objecter_ypos + user.character_height

            if pygame.sprite.collide_rect(user, doctor):
                    doctor_meat = 1
            else:
                doctor_meat = 0

            if doctor_meat == 1:
                community = Button(event_list, comu_image,1664, height / 2 - 128, comu_width, comu_height, click_comu_image,1664,height / 2 - 128, click_tocomu_image, "Comu")

        pygame.display.update()
                
main(0) 


        