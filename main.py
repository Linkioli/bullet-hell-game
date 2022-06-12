import pygame
import gametools
from sys import exit

class Player(pygame.sprite.Sprite):
    '''The Main player class'''
    def __init__(self):
        super().__init__()
        self.player_image = pygame.image.load('sprites/player/player.png').convert_alpha()
        self.image = gametools.smoothscale2x(self.player_image)
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
            self.image = gametools.smoothscale2x(pygame.image.load('sprites/player/player-left.png').convert_alpha())
        elif self.vector.x == 1:
            self.image = gametools.smoothscale2x(pygame.image.load('sprites/player/player-right.png').convert_alpha())
        else:
            self.image = gametools.smoothscale2x(pygame.image.load('sprites/player/player.png').convert_alpha())

    def move(self, velocity):
        if self.vector.magnitude() != 0:
            self.vector = self.vector.normalize()
        self.rect.center += self.vector * velocity

    def update(self):
        self.player_input()
        self.animation_state()
        self.move(self.velocity)



# initilaization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet hell')
clock = pygame.time.Clock()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Background
back_surf = pygame.image.load('sprites/backgrounds/background.png').convert()

# main game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # display background
    screen.blit(back_surf, (0, 0))

    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)
