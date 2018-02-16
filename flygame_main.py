import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """根据设置配置飞船位置信息"""
    ship = Ship(screen,ai_settings)
    """子弹类继承精灵类"""
    bullets = Group()
    """外星人类继承精灵类"""
    aliens = Group()
    """绘制更新一排外星人位置"""
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    while True:
        """获取按键事件"""
        gf.check_events(ai_settings,screen,ship,bullets)
        """飞船位置更新"""
        ship.update()
        """子弹位置更新"""
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        """更新外星人显示"""
        gf.update_aliens(ai_settings,aliens)
        """更新屏幕显示"""
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

