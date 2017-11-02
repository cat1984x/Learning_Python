import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self, ai_settings,screen): #参数顺序要正确
        '''初始化外星人并计算位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        
        #加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人最初都在屏幕右侧中央
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        
        #存储每个外星人准确位置
        self.y = float(self.rect.y)
        

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)        
   
    def update(self):
        '''向下移动外星人'''
        self.y += (self.ai_settings.alien_speed_factor*
            self.ai_settings.fleet_direction)
        self.rect.y = self.y
        
    def check_edges(self):
        '''如果在边缘就返回True'''
        if self.rect.top <= self.screen_rect.top:
            return True
        elif self.rect.bottom >= self.screen_rect.bottom:
            return True

    
