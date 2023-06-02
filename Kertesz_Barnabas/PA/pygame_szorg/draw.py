import pygame

kek = (0, 0, 255)
zold = (0, 255, 0)
piros = (255, 0, 0)
feher = (255, 255, 255)
fekete = (0, 0, 0)
fut = True
background = feher

pygame.init()
kepernyo = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Rajzolás")

while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                background = zold
            elif event.key == pygame.K_r:
                background = piros
            elif event.key == pygame.K_k:
                background = kek
            elif event.key == pygame.K_w:
                background = feher
            elif event.key == pygame.K_b:
                background = fekete
                
    kepernyo.fill(background)
    pygame.draw.circle(kepernyo, fekete, (300, 150), 50, 2)
    pygame.draw.rect(kepernyo, zold, (10, 30, 100, 40), 4)
    pygame.draw.ellipse(kepernyo, piros, (150, 100, 100, 55))
    pygame.display.update()

pygame.quit()