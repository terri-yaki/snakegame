import pygame
from pygame.locals import *
import os
import time


def drawing_block():
    window.fill((255,255,255))
    window.blit(block, (blockX, blockY))
    pygame.display.flip()
    
    
if __name__ == "__main__":
    pygame.init()
        
    window = pygame.display.set_mode(size=(640,640))   #initialize and set window size
    window.fill((255,255,255))  #background(rgb)
        
    block = pygame.image.load("res/aaa.jpg").convert()
    blockX = 320
    blockY = 320
    window.blit(block, (blockX, blockY))
        
    running = True
        
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:       #when a key is pressed
                if event.key == K_ESCAPE:      #escape the window
                    running = False
                if event.key == K_UP:
                    blockY -= 10
                if event.key == K_DOWN:
                    blockY += 10
                if event.key == K_LEFT:
                    blockX -= 10
                if event.key == K_RIGHT:
                    blockX += 10
            elif event.type == QUIT:    #quitting the game
                    running = False
    pygame.quit()