import pygame
import gametools

class Enemy():
    def __init__(self):
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/enemies/enemy.png'))
        self.rect = self.image.get_rect(center = (400, 100))
        self.velocity = 5

    def move(self):
        # move back and forth
        if self.rect.right >= 800: self.velocity = -5
        if self.rect.left <= 0: self.velocity = 5
        self.rect.x += self.velocity

    def collision(self, sprite1, sprite2):
        # detect collions
        collide = sprite1.rect.colliderect(sprite2.rect)
        if collide: print("collision")

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.move()
