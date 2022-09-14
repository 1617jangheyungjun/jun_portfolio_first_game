import pygame,os,math,random,time
from pygame.locals import *

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
pygame.display.set_caption("day dream")
pygame.display.update()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

class Player:
    playerpos = [0, height / 2]
    
    def __init__(self):
        self.image = pygame.image.load(os.path.join("character_image\\dummy.png"))
        self.rect = pygame.Rect(self.image.get_rect())
        self.mentality = 0

    def draw(self):
        self.mousepos = pygame.mouse.get_pos()
        self.angle = math.atan2(self.mousepos[1] - self.playerpos,self.mousepos[0]-self.playerpos[0])
        self.playerrot = pygame.transform.rotate(self.image, 360-self.angle*57.29)
        self.playerpos1 = (self.playerpos[0]-self.playerrot.get_rect().width/2, self.playerpos[1]-self.playerrot.get_rect().height/2)
        screen.blit(self.playerrot, self.playerpos1)