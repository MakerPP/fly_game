import pygame

class Ship():
    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        
        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        """更新飞船的位置"""
        if self.moving_left:
            if self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            else:
                self.center = self.rect.centerx
        if self.moving_right:
            if self.rect.right < self.ai_settings.screen_width:
                self.center += self.ai_settings.ship_speed_factor
            else:
                self.center == self.rect.centerx

        self.rect.centerx = self.center

    def blitme(self):
        """更新飞船显示"""
        self.screen.blit(self.image,self.rect)
