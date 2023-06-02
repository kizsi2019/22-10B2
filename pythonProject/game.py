import pygame
import sys

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Szín és rajzolás példa")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, RED, (50, 50, 200, 100))
    pygame.draw.circle(screen, BLUE, (400, 300), 50)
    pygame.draw.line(screen, GREEN, (600, 100), (700, 200), 5)
    pygame.draw.polygon(screen, YELLOW, [(700, 400), (750, 450), (750, 350)])

    pygame.display.flip()


