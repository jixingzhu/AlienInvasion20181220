import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, ai_setting, ship):
        super(Bullet, self).__init__()
        self.ai_setting = ai_setting
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.color = (255, 255, 0)

    def update(self):
        # if self.rect.y > 0:
        self.rect.y -= self.ai_setting.bullet_speed

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
