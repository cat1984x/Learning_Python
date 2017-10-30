import sys
import pygame

def check_events():
	'''响应键盘和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		
			
def update_sceen(ai_setting,screen,ship):
	'''更新屏幕图像，并切换到新屏幕'''
	
	#每次循环都会重绘屏幕
	screen.fill(ai_setting.bg_color)
	ship.blitme()
			
	#让最近绘制的屏幕可见
	pygame.display.flip()

