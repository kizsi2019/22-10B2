import pygame
import random

pygame.init()
  

# Adatok
szeleseg = 1280
magassag = 620
bird_SPEED = 6
FONT_COLOR = (27, 131, 142)
GAME_TIME = 18000
screen = pygame.display.set_mode((szeleseg, magassag))
pygame.display.set_caption('Madar vadaszat')

# Források
bg_surf = pygame.image.load('PA/pygame_szorg/kep/sky.png').convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 1.3)
bg_rect = bg_surf.get_rect(bottomleft=(0, magassag))
  
bird_surf = pygame.image.load('PA/pygame_szorg/kep/bird2.png').convert_alpha()
birds_rect = []
birds_timer = pygame.USEREVENT + 1
pygame.time.set_timer(birds_timer, 2000)
  
crosshair_surf = pygame.image.load('PA/pygame_szorg/kep/crosshair.png').convert_alpha()
crosshair_surf = pygame.transform.rotozoom(crosshair_surf, 0, 0.7)
crosshair_rect = crosshair_surf.get_rect(center=(szeleseg / 2, magassag / 2))
  
game_font = pygame.font.SysFont('arial', 45, bold=True)
# nyitó- és záróképernyő feliratai
title_surf = game_font.render('Madar vadaszat', True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(szeleseg/2, 200))
run_surf = game_font.render('Nyomj egy E betut hogy elinduljon a jatek', True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(szeleseg/2, magassag-150))

# fügyvények

def display_score():
    score_surf = game_font.render('Pontszam: ' + str(score), True, FONT_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)
  
  
def display_final_score():
    final_score_surf = game_font.render('Ennyi pontod lett: ' + str(score), True, FONT_COLOR)
    final_score_rect = final_score_surf.get_rect(center=(szeleseg / 2, magassag - 220))
    screen.blit(final_score_surf, final_score_rect)
  
  
def display_time_left():
    time_left_surf = game_font.render('Ennyi ido van hatra: ' + str(time_left), True, FONT_COLOR)
    time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
    screen.blit(time_left_surf, time_left_rect)
  
    
clock = pygame.time.Clock()

# Szövegek
game_font = pygame.font.SysFont('arial', 45, bold=True)
title_surf = game_font.render('Madar vadaszat', True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(szeleseg/2, 200))
run_surf = game_font.render('Nyomj egy E betut hogy elinduljon a jatek', True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(szeleseg/2, magassag-150))


start_time = pygame.time.get_ticks()
score = 0
game_active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        # madár létrehozzás
        if event.type == birds_timer:
              birds_rect.append(bird_surf.get_rect(
                center=(random.randint(50, szeleseg-50), magassag-50)))
  
    screen.blit(bg_surf, bg_rect)
  
    if game_active:
        for index, bird_rect in enumerate(birds_rect):
            # madár mozgás  fel 
            birds_rect[index].top -= bird_SPEED
            # madár mozgás oldalra
            mov_y = random.randint(0, 3)
            if mov_y == 0:
                birds_rect[index].left -= 2
            else:
                birds_rect[index].left += 2
            # madár törlése 
            if birds_rect[index].bottom <= -10:
                del birds_rect[index]
            # találat viszgálata
            if bird_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del birds_rect[index]
                score += 1
  
            screen.blit(bird_surf, bird_rect)
        screen.blit(crosshair_surf, crosshair_rect)
  
        # pontszám megjelenítése
        display_score()
  
        # a hátralévő játékidő számítása és megjelenítése
        time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
        if time_left < 0:
            game_active = False
        display_time_left()
  
    #  Nyitó és záró képernyő
    else:
        screen.blit(title_surf, title_rect)
        screen.blit(bird_surf, bird_surf.get_rect(center=(szeleseg/2, magassag/2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(szeleseg/3, magassag/3)))
        screen.blit(run_surf, run_rect)
  
        if score:
            display_final_score()
  
        # játék indítása e betű lenyomásra
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            score = 0
            birds_rect = []
            start_time = pygame.time.get_ticks()
            game_active = True
  
    pygame.display.update()
    # FPS korlátozás
    clock.tick(60)
  
pygame.quit()    
  