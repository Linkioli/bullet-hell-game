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


    def player_input(self):
        keys = pygame.key.get_pressed()
        # player movement
        if keys[pygame.K_UP]: self.rect.y -= 5
        if keys[pygame.K_DOWN]: self.rect.y += 5
        if keys[pygame.K_LEFT]: self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5

    def update(self):
        self.player_input()



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
