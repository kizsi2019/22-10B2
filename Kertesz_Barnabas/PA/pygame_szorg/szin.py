import pygame

kek = (0, 0, 255)
zold = (0, 255, 0)
piros = (255, 0, 0)
feher = (255, 255, 255)
fut = True
background = feher

pygame.init()
kepernyo = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Szín tesztelés")

while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                background = zold
            elif event.key == pygame.K_p:
                background = piros
            elif event.key == pygame.K_k:
                background = kek
            elif event.key == pygame.K_f:
                background = feher
                
    kepernyo.fill(background)
    pygame.display.update()

pygame.quit()