class Settings():

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 0.5
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_Allowed = 8

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        """1 向右移 -1向左移"""
        self.fleet_direction = 1
