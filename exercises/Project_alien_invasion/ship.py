import pygame

class Ship():
    
    def __init__(self,ai_setting,screen):
        '''初始化飞船并设置初始位置'''
        self.screen=screen
        self.ai_seetings=ai_setting
        
        #加载飞船图片并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        #将飞船放在屏幕中央底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #将飞船属性center中存储小数值
        self.centerx = float(self.rect.centerx)

        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_seetings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_seetings.ship_speed_factor
        
        #更新rect对象   
        self.rect.centerx = self.centerx    
        
        
    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        '''让飞船在屏幕中央'''
        #self.rect.centerx = self.screen_rect.centerx 
        #无法放到中央，会在update中被self.centerx替换掉
        
        self.centerx = self.screen_rect.centerx


