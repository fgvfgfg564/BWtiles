import pygame


class Button():
    def __init__(self, engine, x, y):
        self.color = 0
        self.engine = engine
        self.screen = self.engine.screen
        self.settings = self.engine.settings

        self.colors = [self.settings.color1, self.settings.color2]
        self.size = self.engine.settings.button_size
        self.radius = self.size/2
        self.rect = pygame.rect.Rect(x, y, self.size, self.size)
        self.center = self.rect.center

    def blit(self):
        pygame.draw.circle(self.screen, self.settings.frame_color,
                           self.center, self.radius)
        pygame.draw.circle(self.screen, self.colors[self.color],
                           self.center, self.radius - self.settings.frame_width)

    def reverse(self):
        self.color = 1 - self.color

    def check_inside(self, pos):
        return (self.rect.left <= pos.x <= self.rect.right and
                self.rect.top <= pos.y <= self.rect.bottom)
