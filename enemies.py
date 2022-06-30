import pygame
import gametools

class Projectile():
    def __init__(self, x, y, velocity, damage, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.velocity = velocity
        self.damage = damage
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/enemies/projectile.png')).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        self.y += self.velocity

    def draw(self):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.image, self.rect)



class Enemy():
    def __init__(self):
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/enemies/enemy.png'))
        self.rect = self.image.get_rect(center = (400, 100))
        self.velocity = 3
        self.bullets = []
        self.health = 50

    def move(self):
        # move back and forth
        if self.rect.right >= 800: self.velocity = -5
        if self.rect.left <= 0: self.velocity = 5
        self.rect.x += self.velocity


    def collision(self, sprite1, sprite2):
        # detect collions
        index = sprite1.collidelist(sprite2)
        if index != -1:
            self.health -= sprite2[index].damage
            print(f'Enemy Health: {self.health}')
        if self.health <= 0:
            return 0


    def attack(self, screen):
        # time when bullets are loaded into list
        self.bullets.append(Projectile(x = self.rect.centerx, y = self.rect.bottom, velocity = 10, damage = 10, screen = screen))


    def fire(self):
        for i in self.bullets:
            i.update()
            if i.y > 650:
                self.bullets.remove(i)

        for i in self.bullets:
            i.draw()


    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def update(self):
        self.move()
        self.fire()

