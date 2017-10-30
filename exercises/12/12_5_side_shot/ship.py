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
		
		#将飞船放在屏幕左侧中央
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		
		#将飞船属性center中存储小数值
		self.centery = float(self.rect.centery)

		
		#移动标志
		self.moving_down = False
		self.moving_up = False
		
		
	def update(self):
		if self.moving_down and self.rect.bottom  < self.screen_rect.bottom:
			self.centery += self.ai_seetings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_seetings.ship_speed_factor
		
		#更新rect对象	
		self.rect.centery = self.centery
		
		
	def blitme(self):
		'''指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)


