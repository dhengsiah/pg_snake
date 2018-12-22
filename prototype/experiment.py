#Testing moving a block when an arrow key is held

import pygame
import sys

class block(pygame.Rect):
    
    def __init__(self,x,y,width,height):
        pygame.Rect.__init__(self,x,y,width,height)
    
    
background = (255,255,255)

pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption("Moving block test")

run = True

x = 0
y = 0

moving_left = False
moving_right = False
moving_down = False
moving_up = False

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
                
            elif event.key == pygame.K_RIGHT:
                moving_right = True
                
            elif event.key == pygame.K_DOWN:
                moving_down = True
                
            elif event.key == pygame.K_UP:
                moving_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
                
            elif event.key == pygame.K_RIGHT:
                moving_right = False
                
            elif event.key == pygame.K_DOWN:
                moving_down = False
                
            elif event.key == pygame.K_UP:
                moving_up = False





    if moving_up:
        y -= 1

    if moving_down:
        y += 1
            
    if moving_right:
        x += 1
        
    if moving_left:
        x -= 1
            
    screen.fill(background)
    pygame.draw.rect(screen, (255,0,0), block(x,y,20,20))
    pygame.display.update()
                 
pygame.quit()