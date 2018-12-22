#Testing changing direction (like in snake)

import pygame
import sys
import numpy as np

class block(pygame.Rect):
    
    def __init__(self,x,y,width,height):
        pygame.Rect.__init__(self,x,y,width,height)
    
        
### MAIN GAME ###            
                    
background = (255,255,255)

pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))

pygame.display.set_caption("Moving block test")

run = True

velocity = 1
direction = np.array((0,0))
position = np.array((0,0))

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-1,0)
                
            elif event.key == pygame.K_RIGHT:
                direction = (1,0)
                
            elif event.key == pygame.K_DOWN:
                direction = (0,1)
                
            elif event.key == pygame.K_UP:
                direction = (0,-1)



    position += direction * velocity
    
    screen.fill(background)
    pygame.draw.rect(screen, (255,0,0), block(position[0],position[1],20,20))
    pygame.display.update()