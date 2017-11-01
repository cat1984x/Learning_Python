import sys
import pygame

from time import sleep
from random import randint

from ball import Ball

def check_keydown_events(event,ai_settings,screen,wukong):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        #向右移动悟空
        wukong.moving_right = True
    elif event.key == pygame.K_LEFT:
        #向右移动悟空
        wukong.moving_left = True 

    elif event.key == pygame.K_q:
        sys.exit()
        


def check_keyup_events(event,wukong):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        #向右移动悟空
        wukong.moving_right = False           
    if event.key == pygame.K_LEFT:
        #向右移动悟空
        wukong.moving_left = False


def check_events(ai_settings,screen,wukong):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,wukong)             
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,wukong)  



def create_ball(ai_settings,screen,balls):
    '''创建一个龙珠并放在首行'''
    ball = Ball(ai_settings,screen)    
    ball.rect.x = randint(0,(ball.screen_rect.width - ball.rect.width))
    ball.rect.y = ball.rect.height      
    balls.add(ball)

            
def create_fleet(ai_settings,screen,wukong,balls):
    '''创建一个龙珠群'''
    create_ball(ai_settings,screen,balls)

            
def update_screen(ai_settings,screen,wukong,balls):
    '''更新屏幕图像，并切换到新屏幕'''
    
    #每次循环都会重绘屏幕
    screen.fill(ai_settings.bg_color)    
    wukong.blitme()
    balls.draw(screen)            
    #让最近绘制的屏幕可见
    pygame.display.flip()
 

def wukong_hit(ai_settings,stats,screen,wukong,balls):
    '''龙珠没有被抓到'''
    if stats.wukongs_left >0:
        #将所剩悟空减少1
        stats.wukongs_left -= 1
        
        #清空龙珠
        balls.empty()
        
        #创建一群新的龙珠，并将悟空放到屏幕底端中央
        create_fleet(ai_settings,screen,wukong,balls)
        wukong.center_wukong()
        
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_balls_bottom(ai_settings,stats,screen,wukong,balls):
     for ball in balls.sprites(): 
        if ball.rect.bottom >= wukong.screen_rect.bottom:
            wukong_hit(ai_settings,stats,screen,wukong,balls)
            break

  
def update_balls(ai_settings,stats,screen,wukong,wukongs,balls):
    '''检测是否有龙珠到达边缘，然后更新龙珠群中所有龙珠位置'''
    balls.update(ai_settings)
    #检测是否有龙珠到达底部
    check_balls_bottom(ai_settings,stats,screen,wukong,balls)
    #检测是否抓到龙珠
    if pygame.sprite.groupcollide(wukongs,balls,False,True):
        stats.ball_catched += 1
        print(stats.ball_catched)
        create_fleet(ai_settings,screen,wukong,balls)
        
 
