import sys
import pygame


from settings import Settings
from wukong import WuKong
from ball import Ball
import game_functions as gf 
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    #初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))     
    pygame.display.set_caption("Gragon Ball")
    
    #创建悟空
    wukong = WuKong(ai_settings,screen)  
    wukongs = Group()
    wukongs.add(wukong)
    
    #创建龙珠
    balls = Group()
    gf.create_fleet(ai_settings,screen,wukong,balls)   

    
    #创建用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    
    #开始游戏主循环
    while True:     
        gf.check_events(ai_settings,screen,wukong)
        if stats.game_active:
            wukong.update()
            gf.update_balls(ai_settings,stats,screen,wukong,wukongs,balls)
            
        gf.update_screen(ai_settings,screen,wukong,balls)         
        
run_game()
