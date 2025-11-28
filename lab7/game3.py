import pygame
import sys

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Wrap Ball")
clock = pygame.time.Clock()

x, y = W // 2, H // 2
step = 25
radius = 25

WHITE = (255, 255, 255)
RED = (200, 20, 20)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                x -= step
            elif ev.key == pygame.K_RIGHT:
                x += step
            elif ev.key == pygame.K_UP:
                y -= step
            elif ev.key == pygame.K_DOWN:
                y += step
            elif ev.key == pygame.K_ESCAPE:
                running = False

    # ---- Телепортация за края ----
    if x < 0:
        x = W
    elif x > W:
        x = 0

    if y < 0:
        y = H
    elif y > H:
        y = 0

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
