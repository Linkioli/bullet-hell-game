import pygame
import gametools
import players
import enemies
from sys import exit



# initilaization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bullet hell')
clock = pygame.time.Clock()

# Player
player = players.Player()
enemy = enemies.Enemy()

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
    player.update(screen)

    enemy.draw(screen)
    enemy.update()

    try:
        enemy.collision(enemy, player.current_bullet)
    except:
        pass

    pygame.display.update()
    clock.tick(60)
