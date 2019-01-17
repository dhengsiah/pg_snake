import pygame
import sys
import numpy as np
import time

def change_direction(key):
    
    #TODO: Make sure you can't go 'backwards'
    if key == pygame.K_LEFT:
        direction = (-1,0)
                
    elif key == pygame.K_RIGHT:
        direction = (1,0)
                
    elif key == pygame.K_DOWN:
        direction = (0,1)
                
    elif key == pygame.K_UP:
        direction = (0,-1)
        
def update_head(direction,snake):
    #Update the position of the head of the snake
    
    velocity
    
    position
    
def update_body():
    #Update the position of the rest of the snake
    
    pass
    
def draw_blocks():
    #Draws the snake onto the screen
    
    pass
    
def check_game_logic():
    #Checks the game logic:
    # 1: Check for game over - Hit wall/self
    # 2: Check whether a new segment needs to be added
    pass
