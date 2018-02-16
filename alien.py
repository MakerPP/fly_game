import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        """读取外星人图像"""
        self.image = pygame.image.load("images/alien.bmp")
        """获取外星人矩形边界信息"""
        self.rect = self.image.get_rect()
        """示例外星人坐标"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        """将外星人纵坐标转换为浮点型"""
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image,self.rect)

        """向左或者向右移动外星人"""
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        """检测外星人是否碰撞到边缘"""
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    
