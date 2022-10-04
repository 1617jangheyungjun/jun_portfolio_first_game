from importlib.resources import path
from tkinter import Y
import pygame,os,math,random,time,sys
from pygame.locals import *
#os 오류 해결용
current_path1 = os.getcwd()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

#아이콘 그림 가져오기
game_icon = pygame.image.load(os.path.join(current_path1 + "\\icon\\icon.png"))
#배경 그림 가져오기
background = pygame.image.load(os.path.join(current_path1 + "\\bg_image\\test.png"))

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
pygame.display.set_caption("day dream")
pygame.display.update()


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
    right_walk = [pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_right_move.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_right_move2.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_right_move3.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_right_move4.png'))]

    left_walk = [pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_left_move1.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_left_move2.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_left_move3.png')),
    pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character_left_move4.png'))]
    player_left = False
    player_right = False
    walkcount = 0
    current_time = 0
    mt = clock.tick(60) / 1000
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path1 + '\\character_image\\main_character.png')) #주인공 그림을 받아옴
        self.character_size = self.image.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.image = pygame.transform.scale(self.image, (self.character_width, self.character_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.character_x_pos
        self.rect.centery = self.character_y_pos
        self.mentality = 0      #주인공 정신도 수준
        self.forin = 0
        self.animation_time = 100/(4.9 * 100)

    
    def draw(self, event_list, map_locate):
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.character_x_pos
        self.rect.centery = self.character_y_pos
        self.current_time += self.mt
        print(self.current_time, self.animation_time)
        for event in event_list:


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.character_to_x_LEFT -= 0.4 # 바뀐 부분
                    self.player_left = True
                elif event.key == pygame.K_d:
                    self.character_to_x_RIGHT += 0.4 # 바뀐 부분
                    self.player_right = True
                    
                elif event.key == pygame.K_s:
                    self.character_to_y_up += 0.4 # 바뀐 부분
                elif event.key == pygame.K_w:
                    self.character_to_y_down -= 0.4 # 바뀐 부분



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a: # 이 부분은 모두 다 바뀜
                    self.character_to_x_LEFT = 0
                    self.player_left = False
                elif event.key == pygame.K_d:
                    self.character_to_x_RIGHT = 0
                    self.player_right = False
                elif event.key == pygame.K_s:
                    self.character_to_y_up = 0
                elif event.key == pygame.K_w:
                    self.character_to_y_down = 0
        if self.player_right == True:
            if self.current_time > self.animation_time:
                self.walkcount += 1
                self.current_time = 0
            if self.walkcount > 3:
                self.walkcount = 0
            screen.blit(self.right_walk[self.walkcount], (self.character_x_pos, self.character_y_pos))
        elif self.player_left == True:
            if self.current_time > self.animation_time:
                self.walkcount += 1
                self.current_time = 0
            if self.walkcount > 3:
                self.walkcount = 0
            screen.blit(self.left_walk[self.walkcount], (self.character_x_pos, self.character_y_pos))
        else:
            screen.blit(self.image, (self.character_x_pos, self.character_y_pos))

        dt = self.clock.tick(60)
        # 수정4 : 두 변수의 값을 모두 더함
        self.character_x_pos += self.character_to_x_LEFT * dt + self.character_to_x_RIGHT * dt
        self.character_y_pos += self.character_to_y_up * dt + self.character_to_y_down * dt
        if map_locate == 'in':
            if self.character_x_pos < 0:
                self.character_x_pos = 0
            elif self.character_x_pos > width - self.character_width:
                self.character_x_pos = width - self.character_width

            if self.character_y_pos < 0:
                self.character_y_pos = 0
            elif self.character_y_pos > height - self.character_height:
                self.character_y_pos = height - self.character_height
        elif map_locate == 'main':
            if self.character_x_pos < 0:
                self.character_x_pos = 0
            elif self.character_x_pos > 1251:
                self.character_x_pos = 1251


            if self.character_y_pos < 0:
                self.character_y_pos = 0
            elif self.character_y_pos > height - self.character_height:
                self.character_y_pos = height - self.character_height

#의사 클래스 작성
class Doctor:
    doctorpos = [1600, height / 2] 
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path,current_path1 + '\\character_image\\doctor.png')) 
        self.doctor_size = self.image.get_rect().size
        self.doctor_width = self.doctor_size[0]
        self.doctor_height = self.doctor_size[1]
        self.image = pygame.transform.scale(self.image, (self.doctor_width, self.doctor_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.doctorpos[0]
        self.rect.centery = self.doctorpos[1]
    def draw(self):      
        screen.blit(self.image, self.doctorpos)      

#의자 클래스 작성
class Chair:
    chairpos = [1180, height / 2] 
    def __init__(self):
        self.image = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\chair.png')) 
        self.chair_size = self.image.get_rect().size
        self.chair_width = self.chair_size[0]
        self.chair_height = self.chair_size[1]
        self.image = pygame.transform.scale(self.image, (self.chair_width, self.chair_height))
        self.rect = pygame.Rect(self.image.get_rect())  
        self.rect.centerx = self.chairpos[0]
        self.rect.centery = self.chairpos[1]
    def draw(self):      
        screen.blit(self.image, self.chairpos) 

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


class mental_icon:
    def __init__(self):
        self.image1 = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental1.png'))
        self.image2 = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental3.png'))
        self.image3 = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\mental2.png'))
    def draw(self, mental_level):
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
                        elif action == "startmenu":
                            start_text()
                        elif action == "quitmenu":
                            
                            pygame.quit()
                            sys.exit()
        else:
            screen.blit(image_in, (x,y))



def start_text():
    text_color = (255, 255, 255)
    upper_color = (255, 0 , 0)
    paper = pygame.mixer.Sound(os.path.join(image_path,current_path1 + '\\BGM\\Paper_2.7.mp3'))
    caraccident = pygame.mixer.Sound(os.path.join(image_path,current_path1 + '\\BGM\\car.mp3'))
    font1 = pygame.font.SysFont('hy목각파임b',30, True)
    img1 = font1.render('2년전...',True,text_color)
    img2 = font1.render('안녕하십니까! 신입사원 000 입니다! 잘부탁드립니다!',True,text_color)
    img3 = font1.render('.',True,upper_color)
    img4 = font1.render('..',True,upper_color)
    img5 = font1.render('...',True,upper_color)
    img6 = font1.render('저.. 혹시 뭐부터 시작하면 될까요..?',True,text_color)
    img7 = font1.render('가만히있어',True,upper_color)
    img8 = font1.render('죄송합니다...',True,text_color)
    img9 = font1.render('신입이면 신입답게 춤한번 춰봐',True,upper_color)
    img10 = font1.render('네..? 춤을요..?',True,text_color)
    img11 = font1.render('며',True,text_color)
    img12 = font1.render('며칠',True,text_color)
    img13 = font1.render('며칠뒤',True,text_color)
    img14 = font1.render('엄마~ 응 거기로 갈게',True,text_color)
    img15 = font1.render('엄마...',True,text_color)
    img16 = font1.render('엄마... 안돼!!!',True,text_color)
    community_box = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\comunity_company.png'))
    text_index = 0

    upindex = 1
    while True:
        screen.blit(community_box, (0, 0))
        event_list = pygame.event.get()
        #게임 종료
        if text_index != 3 and text_index != 4:
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            #대화 넘김
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame. K_RETURN and upindex == 1:
                        screen.blit(community_box, (0, 0))
                        text_index += 1
        if text_index == 1:
            screen.blit(img1, (50, 850))
        elif text_index == 2:
            screen.blit(img2, (50, 850))
        elif text_index == 3:
            screen.blit(img3, (50, 850))
            pygame.mixer.Sound.play(paper)
            upindex = 0
            time.sleep(0.8)
            text_index += 1
        elif text_index == 4:
            screen.blit(img4, (50, 850))
            time.sleep(0.8)
            text_index += 1
        elif text_index == 5:
            screen.blit(img5, (50, 850))
            time.sleep(0.8)
            upindex = 1
        elif text_index == 6:
            screen.blit(img6, (50, 850))
        elif text_index == 7:
            screen.blit(img7, (50, 850))
        elif text_index == 8:
            screen.blit(img8, (50, 850))
        elif text_index == 9:
            screen.blit(img9, (50, 850))
        elif text_index == 10:
            screen.blit(img10, (50, 850))
        elif text_index == 7:
            screen.blit(img11, (50, 850))
        elif text_index == 11:
            screen.blit(img11, (50, 850))
            upindex = 0
            time.sleep(0.8)
            text_index += 1
        elif text_index == 12:
            screen.blit(img12, (50, 850))
            time.sleep(0.8)
            text_index += 1
        elif text_index == 13:
            screen.blit(img13, (50, 850))
            time.sleep(0.8)
            upindex = 1
        elif text_index == 14:
            screen.blit(img14, (50, 850))
        elif text_index == 15:
            screen.blit(img15, (50, 850))
        elif text_index == 16:
            screen.blit(img16, (50, 850))
            pygame.mixer.Sound.play(caraccident)
            text_index += 1
        elif text_index == 17:
            screen.blit(img16, (50, 850))
        elif text_index == 18:
            main(0)
        
        
        
        
        pygame.display.update()
# 버튼 이벤트 작성

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
                    bathroom()
        pygame.display.update()
class music():
    def sound_play(self, music_path, music_volum):
        pygame.mixer.music.load(os.path.join(image_path,current_path1 + music_path))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(music_volum)
        
#화장실맵
def bathroom():
    running = 1
    user = Player()
    event_list = pygame.event.get()
    washstand1 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda.png'))
    washstand1_size = washstand1.get_rect().size
    washstand21 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda2.png'))
    washstand21_size = washstand1.get_rect().size
    washstand22 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda2-1.png'))
    washstand22_size = washstand1.get_rect().size
    washstand23 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda2-2.png'))
    washstand23_size = washstand1.get_rect().size
    washstand31 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda3.png'))
    washstand31_size = washstand1.get_rect().size
    washstand32 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda3-1.png'))
    washstand32_size = washstand1.get_rect().size
    washstand33 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\sameionda3-2.png'))
    washstand33_size = washstand1.get_rect().size


    toilet1 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet.png'))
    toilet1_size = toilet1.get_rect().size
    toilet21 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet1-1.png'))
    toilet21_size = toilet1.get_rect().size
    toilet22 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet1-2.png'))
    toilet22_size = toilet1.get_rect().size
    toilet23 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet1-3.png'))
    toilet23_size = toilet1.get_rect().size
    toilet24 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet1-4.png'))
    toilet24_size = toilet1.get_rect().size
    toilet31 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet2-1.png'))
    toilet31_size = toilet1.get_rect().size
    toilet32 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet2-2.png'))
    toilet32_size = toilet1.get_rect().size
    toilet33 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet2-3.png'))
    toilet33_size = toilet1.get_rect().size
    toilet34 = pygame.image.load(os.path.join(image_path,current_path1 + '\\object\\toilet2-4.png'))
    toilet34_size = toilet1.get_rect().size



    ingame_background =  pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil.png'))
    ingame_background2 = pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil1.png'))
    ingame_background3 = pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\hwajangsil2.png'))


    map_locate = "in"

    #오브젝트 생성 정신도 따른 세면대
    washstand11_object = Objecter(washstand1,washstand1_size ,87, 0, event_list)
    washstand12_object = Objecter(washstand1,washstand1_size ,275, 0, event_list)
    washstand13_object = Objecter(washstand1,washstand1_size ,462, 0, event_list)
    washstand21_object = Objecter(washstand21,washstand21_size ,87, 0, event_list)
    washstand22_object = Objecter(washstand22,washstand22_size ,275, 0, event_list)
    washstand23_object = Objecter(washstand23,washstand23_size ,462, 0, event_list)
    washstand31_object = Objecter(washstand31,washstand31_size ,87, 0, event_list)
    washstand32_object = Objecter(washstand32,washstand32_size ,275, 0, event_list)
    washstand33_object = Objecter(washstand33,washstand33_size ,462, 0, event_list)


    #오브젝트 생성 정신도 따른 변기칸
    toilet11_object = Objecter(toilet1, toilet1_size, 912, 0, event_list)
    toilet12_object = Objecter(toilet1, toilet1_size, 1164, 0, event_list)
    toilet13_object = Objecter(toilet1, toilet1_size, 1416, 0, event_list)
    toilet14_object = Objecter(toilet1, toilet1_size, 1668, 0, event_list)
    toilet21_object = Objecter(toilet21, toilet21_size, 912, 0, event_list)
    toilet22_object = Objecter(toilet22, toilet22_size, 1164, 0, event_list)
    toilet23_object = Objecter(toilet23, toilet23_size, 1416, 0, event_list)
    toilet24_object = Objecter(toilet24, toilet24_size, 1668, 0, event_list)
    toilet31_object = Objecter(toilet31, toilet31_size, 912, 0, event_list)
    toilet32_object = Objecter(toilet32, toilet32_size, 1164, 0, event_list)
    toilet33_object = Objecter(toilet33, toilet33_size, 1416, 0, event_list)
    toilet34_object = Objecter(toilet34, toilet34_size, 1668, 0, event_list)

    
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
            washstand11_object.draw()
            washstand12_object.draw()
            washstand13_object.draw()
            toilet11_object.draw()
            toilet12_object.draw()
            toilet13_object.draw()
            toilet14_object.draw()
        elif mental_level == 2:
            screen.blit(ingame_background2, (0, 0))
            washstand21_object.draw()
            washstand22_object.draw()
            washstand23_object.draw()
            toilet21_object.draw()
            toilet22_object.draw()
            toilet23_object.draw()
            toilet24_object.draw()
        elif mental_level == 3:
            screen.blit(ingame_background3, (0, 0))
            washstand31_object.draw()
            washstand32_object.draw()
            washstand33_object.draw()
            toilet31_object.draw()
            toilet32_object.draw()
            toilet33_object.draw()
            toilet34_object.draw()
        user.draw(event_list, map_locate)

        mental_icon().draw(mental_level)
        pygame.display.update()

    
#메인화면
        
def main(map_lotate):
    


    event_list = pygame.event.get()
    running = 1
    doctor = Doctor()
    user = Player()
    chair = Chair()
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
    map_locate = 'main'
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
            chair.draw()
            user.draw(event_list, map_locate)
            desk_objecter.draw()
            flower_pot_objecter.draw()
            flower_pot_objecter2.draw()
            
            mental_icon().draw(mental_level)


            
            if pygame.sprite.collide_rect(user, chair):
                    doctor_meat = 1
            else:
                doctor_meat = 0

            if doctor_meat == 1:
                community = Button(event_list, comu_image,1664, height / 2 - 128, comu_width, comu_height, click_comu_image,1664,height / 2 - 128, click_tocomu_image, "Comu")

        pygame.display.update()
                
 

def main_menu():
    bgimage = pygame.image.load(os.path.join(image_path,current_path1 + '\\bg_image\\main_menu.png'))

    white_text_color = (255, 255, 255)
    black_text_color = (0, 0, 0)
    font1 = pygame.font.SysFont('휴먼명조',60, False)
    gametext = font1.render('게임',True,black_text_color)
    starttext = font1.render('시작',True,white_text_color)
    quittext = font1.render("종료", True, white_text_color)
    click_gamestart = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\game start_button.png'))
    click_start_button_size = click_gamestart.get_rect().size
    click_start_width = click_start_button_size[0]
    click_start_height = click_start_button_size[1]
    click_gamestart_uppoint = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\game start_button_uppoint.png'))
    
    click_gamequit = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\game quit_button.png'))
    click_gamequit_size = click_gamequit.get_rect().size
    click_quit_width = click_gamequit_size[0]
    click_quit_height = click_gamequit_size[1]
    click_gamequit_uppoint = pygame.image.load(os.path.join(image_path,current_path1 + '\\interface\\game quit_button_uppoint.png'))
    pygame.mixer.music.load(os.path.join(image_path,current_path1 + '\\BGM\\main_bgm.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    while True:
        event_list = pygame.event.get()
        screen.blit(bgimage, (0, 0))
        start_image = Button(event_list, click_gamestart,753, 413, click_start_width, click_start_height, click_gamestart_uppoint,753, 413, click_gamestart_uppoint, "startmenu")
        quit_image = Button(event_list, click_gamequit,753, 597, click_quit_width, click_quit_height, click_gamequit_uppoint,753, 597, click_gamequit_uppoint, "quitmenu")
        screen.blit(gametext, (840, 420))
        screen.blit(starttext, (960, 420))
        screen.blit(quittext, (960, 605))
        screen.blit(gametext, (840, 605))
        pygame.display.update()
main_menu()