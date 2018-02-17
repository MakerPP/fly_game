import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
        
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """当玩家单击play时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """刷新游戏窗口显示"""
    screen.fill(ai_settings.bg_color)
    """更新绘制每一个子弹对象的位置"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    """更新绘制飞船位置"""
    ship.blitme()
    """更新绘制外星人的图像"""
    aliens.draw(screen)
    """显示得分"""
    sb.show_score()
    """如果游戏处于非活动状态，绘制play按钮"""
    if not stats.game_active:
        play_button.draw_button()
    """将最近绘制的图形刷新到屏幕上"""
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹位置"""
    bullets.update()
    """遍历子弹编组的副本，若子弹对象超出屏幕边界则从编组中删除该子弹对象"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)

    """检查是否产生了最高分"""
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

    """消灭所有外星人之创建另外一群外星人"""
def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level += 1
        sb.prep_level()

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

    """飞船被撞击之后"""
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #更新记分牌
        sb.prep_ships()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    """清空外星人列表和子弹列表"""
    aliens.empty()
    bullets.empty()
    """创建一群新的外星人，并将飞船放置到屏幕低端中央"""
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    """暂停"""
    sleep(0.5)

    """检测是否有外星人撞到屏幕低端"""
def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

    """更新外星人参数"""
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    """更新外星人显示位置"""
    aliens.update()
    """检测是否有外星人撞到屏幕低端"""
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
    """检测是否有外星人和飞船发生碰撞"""
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
        #print("ship hit!!")










    

    
