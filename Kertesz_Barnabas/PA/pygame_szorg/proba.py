import pygame
import random

# Ablak mérete
WIDTH = 800
HEIGHT = 600

# Színek
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Játékos mérete
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Akadályok mérete
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50

# Inicializáljuk a Pygame-et
pygame.init()

# Ablak létrehozása
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surf")

clock = pygame.time.Clock()

# Játékos osztály létrehozása
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - PLAYER_HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x

        # Képernyőn belül tartás
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def move_left(self):
        self.speed_x = -5

    def move_right(self):
        self.speed_x = 5

    def stop_moving(self):
        self.speed_x = 0

# Akadály osztály létrehozása
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
