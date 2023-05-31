import pygame


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Színváltó')
background_color = WHITE

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                  background_color = RED
            elif event.key == pygame.K_g:
                  background_color = GREEN

    screen.fill(background_color)
    pygame.display.update()

pygame.quit()