import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf 


def run_game():
	#初始化游戏
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode(
		(ai_setting.screen_width,ai_setting.screen_height))		
	pygame.display.set_caption("Alien Invasion")
	
	#创建飞船
	ship = Ship(ai_setting,screen)	
	
	#开始游戏主循环
	while True:		
		gf.check_events(ship)
		ship.update()
		gf.update_sceen(ai_setting,screen,ship)		

		
		
run_game()
