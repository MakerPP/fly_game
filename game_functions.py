import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_key_down_event(event,ai_settings,screen,ship,bullets):
    """按键按下事件处理"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit
    """按键按下之后创建新的子弹对象"""
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_Allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
    """按键弹起事件处理"""     
def check_key_up_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    """获取系统按键事件"""    
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """刷新游戏窗口显示"""
    screen.fill(ai_settings.bg_color)
    """更新绘制每一个子弹对象的位置"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """更新绘制飞船位置"""
    ship.blitme()
    """更新绘制外星人的图像"""
    aliens.draw(screen)
    """将最近绘制的图形刷新到屏幕上"""
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹位置"""
    bullets.update()
    """遍历子弹编组的副本，若子弹对象超出屏幕边界则从编组中删除该子弹对象"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)

    """消灭所有外星人之创建另外一群外星人"""
def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
    """计算每一行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

    """根据屏幕大小创建外星人"""
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    """获取一排能够容纳多少外星人最大数目"""
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    """添加一排外星人对象"""
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

    """检测飞船是否撞到边缘"""
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

    """改变飞船运行的方向"""
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

    """更新外星人参数"""
def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    """更新外星人显示位置"""
    aliens.update()











    

    
