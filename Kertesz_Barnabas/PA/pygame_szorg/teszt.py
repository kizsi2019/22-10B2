import pygame
import random

# Kezdő értékek
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
OBSTACLE_SPEED = 5

# Inicializálás
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_image = pygame.image.load('PA/pygame_szorg/kep/bird.png')  # Játékos kép
obstacle_image = pygame.image.load('PA/pygame_szorg/kep/meteor0001.png')  # Akadály kép
d
player_rect = player_image.get_rect()
player_rect.x = WIDTH // 2 - PLAYER_SIZE // 2
player_rect.y = HEIGHT - PLAYER_SIZE

obstacles = []  # Akadályok listája

# Akadályok generálása
def generate_obstacle():
    x = random.randint(0, WIDTH - PLAYER_SIZE)
    y = random.randint(-HEIGHT, -PLAYER_SIZE)
    obstacles.append(pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE))

# Játék ciklus
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_w]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player_rect.y += PLAYER_SPEED

    window.fill((255, 255, 255))  # Háttér törlése

    # Akadályok mozgatása és kirajzolása
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED
        window.blit(obstacle_image, obstacle)

    # Játékos kirajzolása
    window.blit(player_image, player_rect)

    # Új akadályok generálása
    if random.random() < 0.01:
        generate_obstacle()

    # Ellenőrizd az ütközéseket
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            running = False

    pygame.display.flip()
    clock.tick(60)  # FPS korlátozása

pygame.quit()
