import pygame
pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Madina Game')
icon = pygame.image.load("C:/Users/kalab/Downloads/icon.png")
pygame.display.set_icon(icon)

cart = pygame.image.load("C:/Users/kalab/Downloads/icon.png")
running = True
while running:
    
    screen.fill('White')
    
    pygame.draw.circle(screen, 'Blue', (50, 50), 21)
    
    screen.blit(cart, (100, 70))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()      