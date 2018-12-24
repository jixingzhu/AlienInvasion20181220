import setting


class Ship():
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.ai_setting = ai_setting

        self.speed = ai_setting.ship_speed
        # 飞船矩形
        self.rect = ai_setting.ship.get_rect()
        # 屏幕矩形
        self.screen_rect = self.screen.get_rect()
        # 将飞船初始位置定在屏幕底部中央
        self.rect.x = float(self.rect.x)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 向左向右移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ai_setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.ai_setting.ship_speed

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.ai_setting.ship, self.rect)
