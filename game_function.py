import pygame
import os
import setting
from bullet import Bullet


def game_init(screen, ai_setting):
    # 指定游戏窗口的初始默认位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % ai_setting.window_position
    # 创建游戏窗口,设置大小,返回一个surface
    pygame.display.set_caption(ai_setting.caption)

    screen.fill((230, 230, 230))


def creat_ship(ai_setting):
    # 加载飞船图像
    ship = pygame.image.load(ai_setting.ship_image_path)


def check_keydown_event(event, screen, ai_setting, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        '''添加子弹'''
        if len(bullets) < ai_setting.bullet_max:
            bullet = Bullet(screen, ai_setting, ship)
            bullets.add(bullet)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_event(screen, ai_setting, ship, bullets):
    '''监测事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, screen, ai_setting, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def screen_update(screen, ai_setting, ship, bullets):
    '''更新重绘屏幕并显示'''
    # update_ship(ai_setting,ship)
    screen.blit(ai_setting.back_ground, (0, 0))
    ship.blitme()

    for bullet in bullets:
        bullet.blitme()
    pygame.display.flip()


def bullets_update(bullets):
    '''更新子弹信息'''
    # 删除多余的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 会依次调用bullets中每个bullet对象的update函数,具体可help(Group)
    bullets.update()
