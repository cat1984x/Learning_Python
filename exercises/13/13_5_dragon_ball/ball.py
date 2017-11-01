import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    '''表示单个龙珠的类'''
    def __init__(self, ai_settings,screen): #参数顺序要正确
        '''初始化龙珠并计算位置'''
        super(Ball,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.screen_rect = self.screen.get_rect()
        
        #加载龙珠图像，并设置rect属性
        self.image = pygame.image.load('images/ball.jpg')
        self.rect = self.image.get_rect()
        
        #每个龙珠最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储每个龙珠准确位置
        self.x = float(self.rect.x)
        

    def blitme(self):
        '''在指定位置绘制龙珠'''
        self.screen.blit(self.image,self.rect)        
   
    def update(self,ai_settings):
        #固定速度下落
        self.rect.y += ai_settings.fleet_drop_speed
         
    def check_edges(self):
        '''如果在边缘就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    
