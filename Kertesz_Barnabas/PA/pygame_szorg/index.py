import pygame

pygame.init()
kepernyo = pygame.display.set_mode((600, 300))
pygame.display.set_caption("PYGAME teszt")

fut = True

while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
    pygame.display.update()

pygame.quit()