import pygame
import math
import datetime


pygame.init()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Mouse Clock")


clock_image = pygame.image.load("C:/Users/kalab/Downloads/base_micky.jpg")     
right_hand = pygame.image.load("C:/Users/kalab/Downloads/minute.png")          
left_hand = pygame.image.load("C:/Users/kalab/Downloads/second.png")          


clock_image = pygame.transform.scale(clock_image, (600, 600))


minute_scale = 0.5   
second_scale = 0.5   


right_hand = pygame.transform.rotozoom(right_hand, 0, minute_scale)
left_hand = pygame.transform.rotozoom(left_hand, 0, second_scale)


center = (300, 300)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    
    minute_angle = -(minute * 6)  
    second_angle = -(second * 6)

    
    rotated_right = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left = pygame.transform.rotate(left_hand, second_angle)

    
    right_rect = rotated_right.get_rect(center=center)
    left_rect = rotated_left.get_rect(center=center)

    
    screen.blit(clock_image, (0, 0))
    screen.blit(rotated_right, right_rect)
    screen.blit(rotated_left, left_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
