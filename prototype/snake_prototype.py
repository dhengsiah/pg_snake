#Prototype for Snake

import pygame
import sys
import numpy as np
import time
import game_helper as *
import game_classes as *
        
#GLOBAL VARIABLE DEFINITIONS                
snake = setup_game()                        
                                        
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            change_direction(event.key)
        
    update_head()
    check_game_logic()
    update_body()
    screen.fill(background)
    draw_blocks()
    pygame.display.update()
    time.sleep(1.0/1000)
    
    
pygame.quit()
            
            