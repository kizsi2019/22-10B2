import pygame

# Szín paletta
kek = (0, 0, 255)
zold = (0, 255, 0)
piros = (255, 0, 0)
feher = (255, 255, 255)
fekete = (0, 0, 0)
# Háttér szín
background = (127, 127, 185)
# Képernyő méret
width, height = 800, 400
# Változók 
fut = True
ido = pygame.time.Clock()
sebbeseg = 5
# Kordináták
bird_x = width / 2
bird_y = height / 2
bird = pygame.image.load('PA/pygame_szorg/kep/bird.png')

# Szövegek

pygame.init()
kepernyo = pygame.display.set_mode((width, height))
pygame.display.set_caption("PYGAME játék")
bird_rect = bird.get_rect(midleft=(0, height / 2))
bird_for = True

while fut:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              fut = False
  
     keys = pygame.key.get_pressed()
     if keys[pygame.K_d] and bird_rect.right <= width:
          bird = pygame.image.load('PA/pygame_szorg/kep/bird.png')
          bird_x += sebbeseg
     elif keys[pygame.K_a] and bird_rect.left >= 0:
          bird = pygame.image.load('PA/pygame_szorg/kep/bird2.png')
          bird_x -= sebbeseg
  
     if keys[pygame.K_w] and bird_rect.top >= 0:
          bird_y -= sebbeseg
     elif keys[pygame.K_s] and bird_rect.bottom <= height:
          bird_y += sebbeseg
  
     kepernyo.fill(background)
     bird_rect = bird.get_rect(center=(bird_x, bird_y))
     kepernyo.blit(bird, bird_rect)
  
     pygame.display.update()
     ido.tick(60)
  
pygame.quit()