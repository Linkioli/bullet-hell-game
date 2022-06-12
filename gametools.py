import pygame

def smoothscale2x(surf):
    size = pygame.Surface.get_size(surf)
    x = size[0] * 2
    y = size[1] * 2
    size = (x, y)
    surf = pygame.transform.scale(surf, size)
    return surf


