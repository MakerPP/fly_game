import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        #self.rect = pygame.Rect(0,0,ai_settings.bullet_with,ai_settings.bullet_height)
        self.image = pygame.image.load("images/bullet1.bmp")#load image
        self.rect = self.image.get_rect()#get image massege
        self.screen_rect = screen.get_rect()#get screen massege
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        """子弹颜色"""
        self.color = ai_settings.bullet_color
        """子弹速度"""
        self.speed_factor = ai_settings.bullet_speed_factor
    """更新子弹坐标"""
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    """绘制子弹图像"""
    def draw_bullet(self):
        #pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image,self.rect)
