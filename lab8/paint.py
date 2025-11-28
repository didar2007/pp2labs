import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Shapes")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_color = BLACK
filled = False 

running = True
drawing = False
shape = "pen"
start_pos = None
thickness = 5

screen.fill(WHITE)

def draw_square(surf, start, end, color, thick, fill):
    side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surf, color, (*start, side, side), 0 if fill else thick)

def draw_right_triangle(surf, start, end, color, thick, fill):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surf, color, points, 0 if fill else thick)

def draw_equilateral_triangle(surf, start, end, color, thick, fill):
    side = math.dist(start, end)
    height = side * math.sqrt(3) / 2
    x, y = start
    points = [(x, y), (x - side / 2, y + height), (x + side / 2, y + height)]
    pygame.draw.polygon(surf, color, points, 0 if fill else thick)

def draw_rhombus(surf, start, end, color, thick, fill):
    x1, y1 = start
    x2, y2 = end
    dx, dy = (x2 - x1) / 2, (y2 - y1) / 2
    points = [(x1, y1 - dy), (x1 + dx, y1), (x1, y1 + dy), (x1 - dx, y1)]
    pygame.draw.polygon(surf, color, points, 0 if fill else thick)

def draw_circle(surf, start, end, color, thick, fill):
    radius = int(math.dist(start, end))
    pygame.draw.circle(surf, color, start, radius, 0 if fill else thick)

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            drawing, start_pos = True, e.pos

        elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            drawing = False
            end_pos = e.pos

            if shape == "square":
                draw_square(screen, start_pos, end_pos, current_color, thickness, filled)
            elif shape == "right_triangle":
                draw_right_triangle(screen, start_pos, end_pos, current_color, thickness, filled)
            elif shape == "equilateral_triangle":
                draw_equilateral_triangle(screen, start_pos, end_pos, current_color, thickness, filled)
            elif shape == "rhombus":
                draw_rhombus(screen, start_pos, end_pos, current_color, thickness, filled)
            elif shape == "circle":
                draw_circle(screen, start_pos, end_pos, current_color, thickness, filled)

        elif e.type == pygame.MOUSEMOTION and drawing:
            if shape == "pen":
                pygame.draw.rect(screen, current_color, (*e.pos, thickness, thickness))
            elif shape == "eraser":
                pygame.draw.rect(screen, WHITE, (*e.pos, thickness, thickness))

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_EQUALS: thickness += 1
            if e.key == pygame.K_MINUS and thickness > 1: thickness -= 1

            if e.key == pygame.K_1: shape = "pen"
            if e.key == pygame.K_2: shape = "square"
            if e.key == pygame.K_3: shape = "right_triangle"
            if e.key == pygame.K_4: shape = "equilateral_triangle"
            if e.key == pygame.K_5: shape = "rhombus"
            if e.key == pygame.K_6: shape = "circle"
            if e.key == pygame.K_e: shape = "eraser"

            if e.key == pygame.K_c:
                screen.fill(WHITE)

            if e.key == pygame.K_f:
                filled = not filled  

            if e.key == pygame.K_r: current_color = RED
            if e.key == pygame.K_g: current_color = GREEN
            if e.key == pygame.K_b: current_color = BLUE
            if e.key == pygame.K_k: current_color = BLACK
            if e.key == pygame.K_w: current_color = WHITE

    pygame.display.flip()

pygame.quit()
