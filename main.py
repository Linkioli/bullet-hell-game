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

enemy_fire = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_fire, 500)

# main game loop
while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == enemy_fire:
            enemy.attack(screen)

    # display background
    screen.blit(back_surf, (0, 0))

    if player.collision(player.rect, enemy.bullets) != 0:
        player.draw(screen)
        player.update(screen)
    else:
        print("dead lol")
        exit()

    if enemy.collision(enemy.rect, player.bullets) != 0:
        enemy.draw(screen)
        enemy.update()

    pygame.display.update()
    clock.tick(60)
