import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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


    screen.fill(background_color)
    pygame.draw.circle(screen, BLACK, (300, 150), 50, 3, )
    pygame.draw.rect(screen, RED, (10, 20, 100, 50),5 )
    pygame.draw.ellipse(screen, GREEN,(50, 50, 200, 75), 8)
    pygame.draw.polygon(screen, RED [(120, 90),(120,190), (200, 150 )])
    pygame.display.update()

pygame.quit()