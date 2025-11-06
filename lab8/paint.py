import pygame  
import math  
pygame.init() 

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Shapes")

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

LMBpressed = False  
THICKNESS = 5 
current_shape = "pen"  
start_pos = None  

screen.fill(colorWHITE)  
running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True  
            start_pos = event.pos  

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False  
            end_pos = event.pos  

            if current_shape == "square":
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, colorBLUE, (start_pos[0], start_pos[1], side, side), THICKNESS)

            elif current_shape == "right_triangle":
                points = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                pygame.draw.polygon(screen, colorRED, points, THICKNESS)

            elif current_shape == "equilateral_triangle":
                x1, y1 = start_pos
                x2, y2 = end_pos
                side = math.dist(start_pos, end_pos)
                height = (math.sqrt(3) / 2) * side
                top = (x1, y1)
                left = (x1 - side / 2, y1 + height)
                right = (x1 + side / 2, y1 + height)
                pygame.draw.polygon(screen, colorRED, [top, left, right], THICKNESS)

            elif current_shape == "rhombus":
                x1, y1 = start_pos
                x2, y2 = end_pos
                dx = (x2 - x1) / 2
                dy = (y2 - y1) / 2
                points = [(x1, y1 - dy), (x1 + dx, y1), (x1, y1 + dy), (x1 - dx, y1)]
                pygame.draw.polygon(screen, colorBLUE, points, THICKNESS)

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed and current_shape == "pen":
                pygame.draw.rect(screen, colorBLACK, (event.pos[0], event.pos[1], THICKNESS, THICKNESS))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS and THICKNESS > 1:
                THICKNESS -= 1
            if event.key == pygame.K_1:
                current_shape = "pen"
            if event.key == pygame.K_2:
                current_shape = "square"
            if event.key == pygame.K_3:
                current_shape = "right_triangle"
            if event.key == pygame.K_4:
                current_shape = "equilateral_triangle"
            if event.key == pygame.K_5:
                current_shape = "rhombus"
            if event.key == pygame.K_c:
                screen.fill(colorWHITE)

    pygame.display.flip()

pygame.quit()
