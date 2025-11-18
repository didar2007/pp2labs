import pygame, random, sys, time

pygame.init()

W, H = 400, 600
FPS = 60
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simple Racing")
clock = pygame.time.Clock()

WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, GREEN, BLUE, GOLD = (255, 0, 0), (0, 200, 0), (0, 0, 255), (255, 215, 0)

speed = 5
score = 0
coins_collected = 0
level_up_every = 10

font = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)
game_over_text = font_big.render("Game Over", True, BLACK)


PLAYER_IMG_PATH = "C:/Users/kalab/OneDrive/Рабочий стол/car.png"
ENEMY_IMG_PATH  = "C:/Users/kalab/OneDrive/Рабочий стол/car_2.png"
COIN_IMG_PATH   = "C:/Users/kalab/OneDrive/Рабочий стол/free-icon-coin-217853.png"

PLAYER_IMG = pygame.image.load(PLAYER_IMG_PATH)
ENEMY_IMG  = pygame.image.load(ENEMY_IMG_PATH)
COIN_IMG   = pygame.image.load(COIN_IMG_PATH)

PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (40, 60))
ENEMY_IMG  = pygame.transform.scale(ENEMY_IMG, (40, 60))
COIN_IMG   = pygame.transform.scale(COIN_IMG,  (25, 25))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect(midbottom=(W // 2, H - 40))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.x += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY_IMG
        self.rect = self.image.get_rect(midtop=(random.randint(40, W - 40), -50))

    def update(self):
        global score
        self.rect.y += speed
        if self.rect.top > H:
            score += 1
            self.rect.midtop = (random.randint(40, W - 40), -50)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = COIN_IMG
        self.rect = self.image.get_rect(center=(random.randint(30, W - 30), -30))
        self.value = random.choice([1, 3, 5])

    def update(self):
        self.rect.y += speed
        if self.rect.top > H:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(30, W - 30), random.randint(-150, -20))
        self.value = random.choice([1, 3, 5])


player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)


running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.collide_rect(player, coin):
        coins_collected += coin.value
        coin.respawn()
        if coins_collected % level_up_every == 0:
            speed += 1

    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(game_over_text, game_over_text.get_rect(center=(W // 2, H // 2)))
        pygame.display.flip()
        time.sleep(2)
        break

    screen.fill(WHITE)
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Coins: {coins_collected}", True, BLACK), (W - 120, 10))

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
