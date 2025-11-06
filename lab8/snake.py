import pygame
import random
import time
from Colors import *

pygame.init()

WIDTH = 900
HEIGHT = 900
CELL = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 30)

BORDER_COLOR = colorSILVER

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (j * CELL, i * CELL, CELL, CELL))
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, WIDTH, CELL))  
    pygame.draw.rect(screen, BORDER_COLOR, (0, HEIGHT - CELL, WIDTH, CELL)) 
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, CELL, HEIGHT))  
    pygame.draw.rect(screen, BORDER_COLOR, (WIDTH - CELL, 0, CELL, HEIGHT))  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def check_wall_collision(self):
        head = self.body[0]
        return head.x < 1 or head.x >= (WIDTH // CELL) - 1 or head.y < 1 or head.y >= (HEIGHT // CELL) - 1

    def check_collision(self, food):
        head = self.body[0]
        for point in food.points:
            if head.x == point.x and head.y == point.y:
                self.score += food.weight
                for _ in range(food.weight):
                    self.body.append(Point(head.x, head.y))
                food.respawn()
                break

class Food:
    def __init__(self):
        self.counter = 0
        self.respawn()

    def respawn(self):
        self.timer = 10
        self.appeared_time = time.time()
        self.counter += 1
        self.big = (self.counter % 5 == 0)
        self.weight = 10 if self.big else 1
        self.base_point = Point(
            random.randint(1, (WIDTH // CELL) - (2 if self.big else 1) - 1),
            random.randint(1, (HEIGHT // CELL) - (2 if self.big else 1) - 1)
        )
        self.generate_points()

    def generate_points(self):
        self.points = []
        if self.big:
            for dx in range(2):
                for dy in range(2):
                    self.points.append(Point(self.base_point.x + dx, self.base_point.y + dy))
        else:
            self.points = [self.base_point]

    def draw(self):
        now = time.time()
        if self.big:
            elapsed = now - self.appeared_time
            self.weight = max(1, 10 - int(elapsed))
            if elapsed > 10:
                self.respawn()
        color = colorGREEN if not self.big else (255, 215, 0)
        for point in self.points:
            pygame.draw.rect(screen, color, (point.x * CELL, point.y * CELL, CELL, CELL))

FPS = 10
clock = pygame.time.Clock()

snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    draw_grid_chess()
    snake.move()

    if snake.check_self_collision() or snake.check_wall_collision():
        print("Game Over!")
        running = False

    snake.check_collision(food)

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {snake.score}", True, colorBLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
