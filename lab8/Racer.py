import pygame
import random
import sys
import time

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Racing")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE  = (0, 0, 255)

SPEED = 5
SCORE = 0
COINS = 0
N = 10  

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)
game_over_surf = font_big.render("Game Over", True, BLACK)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        w, h = 40, 60
        self.image = pygame.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        w, h = 40, 60
        self.image = pygame.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect(midtop=(random.randint(40, SCREEN_WIDTH - 40), -50))

    def update(self):
        global SCORE
        self.rect.y += SPEED
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.y = -random.randint(40, 120)
            self.rect.x = random.randint(20, SCREEN_WIDTH - 20)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = 20
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(random.randint(30, SCREEN_WIDTH - 30), -30))
        self.weight = random.choice([1, 3, 5])

    def update(self):
        self.rect.y += SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(30, SCREEN_WIDTH - 30), random.randint(-150, -20))
        self.weight = random.choice([1, 3, 5])


player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.collide_rect(player, coin):
        COINS += coin.weight
        coin.respawn()
        if COINS % N == 0:
            SPEED += 1

   
    if pygame.sprite.spritecollideany(player, enemies):
        
        screen.fill(RED)
        screen.blit(game_over_surf, game_over_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        pygame.display.flip()
        time.sleep(2)
        running = False
        break

    
    screen.fill(WHITE)
    
    screen.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Coins: {COINS}", True, BLACK), (SCREEN_WIDTH - 120, 10))

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

