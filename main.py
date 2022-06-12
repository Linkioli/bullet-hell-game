import pygame
import gametools
import players
from sys import exit



# initilaization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet hell')
clock = pygame.time.Clock()

# Player
player = pygame.sprite.GroupSingle()
player.add(players.Player())

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
