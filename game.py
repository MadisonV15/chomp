print("Hello World")
print("This is so cool!")

import pygame
import sys

screen_width = 500
screen_height = 300

blue = (0,0,255)
brown = (150,75,0)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)
    rectangle_height = 100
    pygame.draw.rect(screen, brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))

    pygame.display.flip()

pygame.quit()
sys.exit()