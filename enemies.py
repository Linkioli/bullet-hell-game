import pygame
import gametools

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/enemies/enemy.png'))
        self.rect = self.image.get_rect(center = (400, 100))
        self.velocity = 5

    def move(self):
        # move back and forth
        if self.rect.right >= 800: self.velocity = -5
        if self.rect.left <= 0: self.velocity = 5
        self.rect.x += self.velocity

    def update(self):
        self.move()
