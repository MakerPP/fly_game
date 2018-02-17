class Settings():

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 0.5
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_Allowed = 8

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        """1 向右移 -1向左移"""
        self.fleet_direction = 1

        # 加快游戏节奏速度
        self.speedup_scale = 1.1
        # 外星人点速提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #1 向左移 -1 向右移
        self.fleet_direction = 1
        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)




