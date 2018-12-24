import pygame


class Setting():
    '''游戏的所有设置'''

    def __init__(self):
        self.window_position = (300, 300)
        self.window_size = (900, 600)
        self.caption = 'alien invasion'
        self.ship = pygame.image.load('images/ship.png')

        # self.back_ground = pygame.image.load('images/star1024x605.jpg').convert()#定义屏幕一定要在convert之前
        self.back_ground = pygame.image.load('images/star1024x605.jpg')
        # ship速度
        self.ship_speed = 6.0

        # 子弹宽高 速度 最多数量
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_speed = 1.5
        self.bullet_max = 8
