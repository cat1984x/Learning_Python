import pygame

class Ship():
	
	def __init__(self,sceen):
		'''初始化飞船位置'''
		self.sceen=sceen
		
		#加载飞船图片并获取外接矩形
		self.image = pygame.image.load('images/loli.jpg')
		self.rect = self.image.get_rect()
		self.sceen_rect = self.sceen.get_rect()
		
		#将飞船放在屏幕中央底部
		self.rect.centerx=self.sceen_rect.centerx
		self.rect.centery=self.sceen_rect.centery
		
	def blitme(self):
		'''指定位置绘制飞船'''
		self.sceen.blit(self.image,self.rect)


