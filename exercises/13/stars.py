import sys
import pygame

from star import Star


pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Stars")
bg_color =(255,255,255) #白色


star = Star()

while True:
    
    
    
    #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(bg_color)
    
    #让最近绘制的屏幕可见
    pygame.display.flip()
