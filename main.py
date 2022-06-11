import pygame
from sys import exit

# initilaization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet hell')

# main game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
