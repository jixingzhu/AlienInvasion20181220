import pygame
import game_function as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group


def run_game():
    # pygame初始化
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(ai_setting.window_size)

    gf.game_init(screen, ai_setting)
    ship = Ship(screen, ai_setting)
    bullets = Group()
    while True:
        # 监测鼠标键盘操作
        gf.check_event(screen, ai_setting, ship, bullets)
        # 更新飞船位置
        ship.update()
        gf.bullets_update(bullets)
        # 重绘屏幕
        gf.screen_update(screen, ai_setting, ship, bullets)


run_game()
