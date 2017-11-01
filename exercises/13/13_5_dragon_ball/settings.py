class Settings():
    def __init__(self):     
        '''存储游戏所有设置的类'''
        
        #设置背景色
        self.screen_width = 1200
        self.screen_height = 800        
        self.bg_color = (255,255,255)   
        
        #悟空的设置
        self.wukong_speed_factor = 1.5
        self.wukong_limit = 2
        

        #龙珠设置
        self.ball_speed_factor = 1
        self.fleet_drop_speed = 1


