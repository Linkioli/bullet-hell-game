import pygame
from sys import exit

# initilaization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet hell')

class Player(pygame.sprite.Sprite):
    '''The Main player class'''
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/player/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0, 0))

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# main game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.draw(screen)
    pygame.display.update()
