class Settings():
    def __init__(self):     
        '''存储游戏所有设置的类'''
        
        #设置背景色
        self.screen_width = 1200
        self.screen_height = 800        
        self.bg_color = (230,230,230)   
        
        #飞船的设置
        self.ship_speed_factor = 1.5
        

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向左，为-1表示向右
        self.fleet_direction = 1
       
        
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
