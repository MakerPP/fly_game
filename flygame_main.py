import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    """根据设置配置飞船位置信息"""
    ship = Ship(ai_settings,screen)
    """子弹类继承精灵类"""
    bullets = Group()
    """外星人类继承精灵类"""
    aliens = Group()
    """绘制更新一排外星人位置"""
    gf.create_fleet(ai_settings,screen,ship,aliens)
    """创建一个用于统计存储游戏统计信息的实例""" 
    stats = GameStats(ai_settings)
    """创建play按钮"""
    play_botton = Button(ai_settings,screen,"Play")
    """创建统计信息实例，并创建记分牌"""
    sb = Scoreboard(ai_settings,screen,stats)

    while True:
        """获取按键事件"""
        gf.check_events(ai_settings,screen,stats,sb,play_botton,ship,aliens,bullets)
        if stats.game_active:
            """飞船位置更新"""
            ship.update()
            """子弹位置更新"""
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            """更新外星人显示"""
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        """更新屏幕显示"""
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_botton)

