import pygame
import gametools



class Player(pygame.sprite.Sprite):
    '''The Main player class'''
    def __init__(self):
        super().__init__()
        self.player_image_center = gametools.smoothscale2x(pygame.image.load('sprites/player/player.png')).convert_alpha()
        self.player_image_left = gametools.smoothscale2x(pygame.image.load('sprites/player/player-left.png')).convert_alpha()
        self.player_image_right = gametools.smoothscale2x(pygame.image.load('sprites/player/player-right.png')).convert_alpha()
        self.player_image = [self.player_image_left, self.player_image_center, self.player_image_right]
        self.player_index = 1
        self.image = self.player_image[self.player_index]
        self.rect = self.image.get_rect(center = (400, 500))

        self.vector = pygame.math.Vector2()
        self.velocity = 5


    def player_input(self):
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


    def update(self):
        self.player_input()
        self.animation_state()
        self.move(self.velocity)

