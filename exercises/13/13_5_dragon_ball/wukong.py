import pygame
from pygame.sprite import Sprite

class WuKong(Sprite):
    
    def __init__(self,ai_setting,screen):
        super(WuKong,self).__init__()
        '''初始化龙珠并设置初始位置'''
        self.screen=screen
        self.ai_seetings=ai_setting
        
        #加载龙珠图片并获取外接矩形
        self.image = pygame.image.load('images/sungoku.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #将龙珠放在屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #将龙珠属性center中存储小数值
        self.centerx = float(self.rect.centerx)

        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_seetings.wukong_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_seetings.wukong_speed_factor
        
        #更新rect对象   
        self.rect.centerx = self.centerx    
        
        
    def blitme(self):
        '''指定位置绘制龙珠'''
        self.screen.blit(self.image,self.rect)
        
    def center_wukong(self):
        '''让龙珠在屏幕中央'''
        #self.rect.centerx = self.screen_rect.centerx 
        #无法放到中央，会在update中被self.centerx替换掉
        
        self.centerx = self.screen_rect.centerx


