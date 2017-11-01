import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf 
from pygame.sprite import Group


def run_game():
    #初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     
    pygame.display.set_caption("Alien Invasion")
    
    #创建飞船
    ship = Ship(ai_settings,screen)  
    
    #创建外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens) 
    
    #创建存储子弹的编组
    bullets = Group()
    
    #开始游戏主循环
    while True:     
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)      
<<<<<<< HEAD
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)        
=======
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)         
>>>>>>> parent of 98eac30... 13
        
run_game()
