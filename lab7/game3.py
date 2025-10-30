import pygame
import sys


widght, height = 800, 600
radius = 25                
step = 20                  
bg_color = (255, 255, 255) 
ball_color = (200, 20, 20) 

pygame.init()
screen = pygame.display.set_mode((widght, height))
pygame.display.set_caption("Move the Red Ball (arrow keys)")
clock = pygame.time.Clock()


x = widght // 2
y = height // 2

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        elif ev.type == pygame.KEYDOWN:
            
            nx, ny = x, y
            if ev.key == pygame.K_LEFT:
                nx = x - step
            elif ev.key == pygame.K_RIGHT:
                nx = x + step
            elif ev.key == pygame.K_UP:
                ny = y - step
            elif ev.key == pygame.K_DOWN:
                ny = y + step
            elif ev.key == pygame.K_ESCAPE:
                running = False

            
            if radius <= nx <= widght - radius and radius <= ny <= height - radius:
                x, y = nx, ny
            

    
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
