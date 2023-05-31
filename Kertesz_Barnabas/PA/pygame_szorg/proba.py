import pygame
import random

# Inicializáljuk a Pygame-et
pygame.init()

# A képernyő mérete
screen_width = 800
screen_height = 600
# Színek
white = (255, 255, 255)
black = (0, 0, 0)

# A metró adatai
subway_width = 50
subway_height = 50
subway_x = (screen_width - subway_width) / 2
subway_y = screen_height - subway_height - 10
subway_speed = 1.5

# Az utasok adatai
passenger_size = 50
passenger_speed = 0.8

# A játék állapotai
game_over = False
score = 0
game_started = False

# Betűtípus és méret beállítása
font = pygame.font.Font(None, 36)

# A háttér betöltése
background_image = pygame.image.load("PA/pygame_szorg/kep/backgro.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Szövegek 
start_text = font.render("Nyomj SPACE-t a kezdéshez", True, white)
game_over_text = font.render("Játék vége! Pontszám: " + str(score), True, white)

# Az ablak beállítása
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Metrós játék")

# A kezdőszöveg kiírása
def draw_start_screen():
    start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(start_text, start_rect)

# A game over szöveg kiírása
def draw_game_over_screen():
    game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    window.blit(game_over_text, game_over_rect)

# Az utasok osztálya
class Passenger:
    def __init__(self):
        self.x = random.randint(0, screen_width - passenger_size)
        self.y = -100
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    
    def move(self):
        self.y += passenger_speed
    
    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, passenger_size, passenger_size))

# Az utasok listája
passengers = []

for _ in range(9):
    passengers.append(Passenger())

# Játék ciklus
draw_start_screen()  # Kezdőszöveg kirajzolása

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and subway_x > 0:
        subway_x -= subway_speed
    if keys[pygame.K_d] and subway_x < screen_width - subway_width:
        subway_x += subway_speed
    
    window.blit(background_image, (0, 0))
    
    if game_started:
        for passenger in passengers:
            passenger.move()
            passenger.draw()
            
            # Ha az utas eléri a földet, újraállítjuk a pozícióját és növeljük a pontszámot
            if passenger.y > screen_height:
                passengers.remove(passenger)
                passengers.append(Passenger())
                score += 1
        
            # Ütközésdetekció
            if (passenger.x + passenger_size > subway_x and passenger.x < subway_x + subway_width and
                passenger.y + passenger_size > subway_y and passenger.y < subway_y + subway_height):
                game_over = True
    
    pygame.draw.rect(window, white, (subway_x, subway_y, subway_width, subway_height))
    
    if not game_started:
        draw_start_screen()
    elif game_over:
        draw_game_over_screen()
    
    pygame.display.update()
print(score)
# Pygame leállítása
pygame.quit()
