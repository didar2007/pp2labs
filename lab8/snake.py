import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake with Timed Food")
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED   = (255,   0, 0)
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

snake = [(WIDTH // 2, HEIGHT // 2)]   
dx, dy = BLOCK, 0                     
length = 1                            

food_x = random.randrange(0, WIDTH, BLOCK)
food_y = random.randrange(0, HEIGHT, BLOCK)
food_value = random.choice([1, 2, 3])     

FOOD_LIFETIME_MS = 5000                    
food_spawn_time = pygame.time.get_ticks()  



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -BLOCK
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, BLOCK
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -BLOCK, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = BLOCK, 0

    x, y = snake[-1]
    x += dx
    y += dy

    if x < 0: x = WIDTH - BLOCK
    elif x >= WIDTH: x = 0
    if y < 0: y = HEIGHT - BLOCK
    elif y >= HEIGHT: y = 0

    new_head = (x, y)
    snake.append(new_head)

    if x == food_x and y == food_y:
        length += food_value                      
        food_x = random.randrange(0, WIDTH, BLOCK)
        food_y = random.randrange(0, HEIGHT, BLOCK)
        food_value = random.choice([1, 2, 3])
        food_spawn_time = pygame.time.get_ticks()  
    else:
        snake.pop(0)

    current_time = pygame.time.get_ticks()

    if current_time - food_spawn_time >= FOOD_LIFETIME_MS:
        food_x = random.randrange(0, WIDTH, BLOCK)
        food_y = random.randrange(0, HEIGHT, BLOCK)
        food_value = random.choice([1, 2, 3])
        food_spawn_time = pygame.time.get_ticks()  

    if len(snake) != len(set(snake)):
        running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK, BLOCK))

    font = pygame.font.SysFont("Verdana", 18)
    text = font.render(str(food_value), True, WHITE)
    screen.blit(text, (food_x + 4, food_y + 2))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
