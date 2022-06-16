import pygame
import gametools

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/enemies/enemy.png'))
        self.rect = self.image.get_rect(center = (400, 100))
