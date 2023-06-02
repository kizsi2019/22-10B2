import pygame
import random

WIDTH = 1280
HEIGHT = 620
BG_COLOR = (255, 255, 255)
FONT_COLOR = (27, 131, 142)



class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ninja_fw_1 = pygame.image.load('img/Run__001.png').convert_alpha()
        ninja_fw_2 = pygame.image.load('img/Run__002.png').convert_alpha()
        ninja_fw_3 = pygame.image.load('img/Run__005.png').convert_alpha()
        self.ninja_fw = [ninja_fw_1, ninja_fw_2, ninja_fw_3]
        ninja_b_1 = pygame.image.load('img/Run__001_b.png').convert_alpha()
        ninja_b_2 = pygame.image.load('img/Run__002_b.png').convert_alpha()
        ninja_b_3 = pygame.image.load('img/Run__005_b.png').convert_alpha()
        self.ninja_b = [ninja_b_1, ninja_b_2, ninja_b_3]
        ninja_attack_1 = pygame.image.load('img/Jump_Attack__002.png').convert_alpha()
        ninja_attack_2 = pygame.image.load('img/Jump_Attack__009.png').convert_alpha()
        ninja_attack_3 = pygame.image.load('img/Jump_Attack__007.png').convert_alpha()
        self.ninja_attack = [ninja_attack_1, ninja_attack_2, ninja_attack_3]
        self.attack_mode = False
        self.ninja_index = 0
        self.ninja_forward = True
        self.image = self.ninja_fw[self.ninja_index]
        self.rect = self.image.get_rect(midbottom=(WIDTH / 2, HEIGHT - 149))
        self.speed = 5
        self.on_ground = True
        self.gravity = 1
        self.jump_speed = -16
        self.dy = 0

    def ninja_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.attack_mode = True
            self.attack_animation()
        else:
            self.attack_mode = False
            self.image = pygame.image.load('img/Idle__000 1.png')
            rect_center = self.rect.center
            self.rect = self.image.get_rect(center=rect_center)

        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.x_movement(self.speed)
            self.ninja_forward = True
        if keys[pygame.K_a] and self.rect.left > 0:
            self.x_movement(-self.speed)
            self.ninja_forward = False
        if keys[pygame.K_w] and self.on_ground:
            self.jump()

    def apply_gravity(self):
        self.dy += self.gravity
        self.rect.y += self.dy

    def jump(self):
        self.on_ground = False
        self.dy = self.jump_speed

    def y_movement_collision(self):
        for pf_rect in platform_rects:
            if self.rect.colliderect(pf_rect):
                self.rect.bottom = pf_rect.top
                self.dy = 0
                self.on_ground = True

    def x_movement(self, dx):
        self.rect.x += dx
        self.x_movement_animation()

    def x_movement_animation(self):
        if self.ninja_index < len(self.ninja_fw) - 1:
            self.ninja_index += 0.2
        else:
            self.ninja_index = 0

        if self.ninja_forward:
            self.image = self.ninja_fw[int(self.ninja_index)]
        else:
            self.image = self.ninja_b[int(self.ninja_index)]

    def attack_animation(self):
        if self.ninja_index < len(self.ninja_fw) - 1:
            self.ninja_index += 0.2
        else:
            self.ninja_index = 0
        self.image = self.ninja_attack[int(self.ninja_index)]

    def update(self):
        self.ninja_input()
        self.apply_gravity()
        self.y_movement_collision()


class Fruit(pygame.sprite.Sprite):
    def __init__(self, fruit_type):
        super().__init__()
        if fruit_type == 'pear':
            self.image = pygame.image.load('img/pear.png').convert_alpha()
        elif fruit_type == 'banana':
            self.image = pygame.image.load('img/banana.png').convert_alpha()
        else:
            self.image = pygame.image.load('img/strawberry.png').convert_alpha()
        self.rect = self.image.get_rect(center=(random.randint(20, WIDTH - 20), -20))

    def destroy(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def update(self):
        self.rect.y += 5
        self.destroy()


def collision_sprite():
    # if ninja.sprite.__getattribute__('attack_mode'):
    if ninja.sprite.attack_mode:
        if pygame.sprite.spritecollide(ninja.sprite, fruit_group, True):
            return True
    else:
        return False


def display_score():
    score_surf = game_font.render('score: ' + str(score), True, FONT_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Ninja')
clock = pygame.time.Clock()

platform_surf = pygame.image.load('img/platform.png').convert_alpha()
platform_rects = [platform_surf.get_rect(midtop=(WIDTH / 2, HEIGHT - 150)),
                  platform_surf.get_rect(midtop=(WIDTH + 250, HEIGHT - 200)),
                  platform_surf.get_rect(midtop=(WIDTH -1500, HEIGHT - 220))]

ninja = pygame.sprite.GroupSingle()
ninja.add(Ninja())

fruit_group = pygame.sprite.Group()

fruit_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fruit_timer, 1000)

score = 0
game_font = pygame.font.SysFont('arial', 30, bold=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == fruit_timer:
            fruit_group.add(Fruit(random.choice(['pear', 'banana', 'strawberry'])))

    screen.fill(BG_COLOR)
    for platform_rect in platform_rects:
        screen.blit(platform_surf, platform_rect)

    ninja.draw(screen)
    ninja.update()
    pygame.draw.rect(screen, 'gray', ninja.sprite.rect, 2)

    fruit_group.draw(screen)
    fruit_group.update()

    if collision_sprite():
        score += 1.5
    display_score()

    pygame.display.update()
    clock.tick(60)



pygame.quit()
