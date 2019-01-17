import pygame
import sys
import numpy as np
import time

class snake:
    #Model as a linked list

    def __init__(self,block):
        self.head = block
        
    def appendtoTail(self,Block):
        #Append block to the end of the tail
        x = self.head
        
        while x.nextBlock != None:
            x = x.nextBlock
            
            
        x.nextNode = Block
        Block.prevBlock = x
        
        return
        
    def appendAfterHead(self,block):
        
        x = self.head        
        temp = x.nextBlock
                
        x.nextBlock = block
        block.nextBlock = temp
        

class block(pygame.Rect):
    
    def __init__(self,x,y,block_size):
        self.size = block_size
        self.position = [x,y]
        self.nextBlock = None
        self.prevBlock = None
        pygame.Rect.__init__(self,self.position[0],position[1],block_size,block_size)
        
   