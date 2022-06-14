import pygame
import gametools



class Bullet:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.velocity = 20
        self.image = gametools.smoothscale2x(pygame.image.load('sprites/player/player-bullet.png')).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))


    def update(self):
        self.y -= self.velocity


    def draw(self):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.image, self.rect)



class Player(pygame.sprite.Sprite):
    '''The Main player class'''
    def __init__(self):
        super().__init__()
        self.player_image_center = gametools.smoothscale2x(pygame.image.load('sprites/player/player.png')).convert_alpha()
        self.player_image_left = gametools.smoothscale2x(pygame.image.load('sprites/player/player-left.png')).convert_alpha()
        self.player_image_right = gametools.smoothscale2x(pygame.image.load('sprites/player/player-right.png')).convert_alpha()
        self.player_image = [self.player_image_left, self.player_image_center, self.player_image_right]
        self.player_index = 1
        self.bullets = []
        self.image = self.player_image[self.player_index]
        self.rect = self.image.get_rect(center = (400, 500))

        self.vector = pygame.math.Vector2()
        self.velocity = 5

        self.bullet_buffer = 0


    def attack(self, type, screen):

        # normal attack
        if type == 'normal':
            bullet_freq = 1
            self.bullet_buffer += 1
            if self.bullet_buffer == bullet_freq:
                self.bullets.append(Bullet(self.rect.centerx, self.rect.top, screen))
            if self.bullet_buffer > bullet_freq:
                self.bullet_buffer = 0


    def player_input(self, screen):
        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_UP]:
            self.vector.y = -1
        elif keys[pygame.K_DOWN]:
            self.vector.y = 1
        else:
            self.vector.y = 0

        if keys[pygame.K_LEFT]:
            self.vector.x = -1
        elif keys[pygame.K_RIGHT]:
            self.vector.x = 1
        else:
            self.vector.x = 0

        if keys[pygame.K_x]:
            self.attack('normal', screen)


    def fire(self):
        for i in self.bullets:
            i.update()
            if i.y < -50:
                self.bullets.remove(i)

        for i in self.bullets:
            i.draw()


    def animation_state(self):
        if self.vector.x == -1:
            self.player_index -= 0.1
        elif self.vector.x == 1:
            self.player_index += 0.1
        else:
            self.player_index = 1

        if self.player_index < 0: self.player_index = 0
        elif self.player_index >= len(self.player_image): self.player_index = 2
        self.image = self.player_image[int(self.player_index)]


    def move(self, velocity):
        if self.vector.magnitude() != 0:
            self.vector = self.vector.normalize()
        self.rect.center += self.vector * velocity

        # screen border collision
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.right > 800: self.rect.right = 800
        if self.rect.bottom > 600: self.rect.bottom = 600


    def update(self, screen):
        self.player_input(screen)
        self.animation_state()
        self.move(self.velocity)
        self.fire()

