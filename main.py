import pygame
from pygame.locals import *
import keyboard
import os
import time

def drawing_block():
    surface.fill((0,0,0))
    surface.blit(block, (blockX, blockY))

if __name__ == "___main__":
    pygame.init()
    
    surface = pygame.display.set_mode(size=(640,640))   #initialize and set window size
    surface.fill((0,0,0))  #background(rgb)
    
    block = pygame.image.load("res\block.png").convert()
    blockX = 320
    blockY = 320
    surface.blit(block, (blockX, blockY))
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            elif event.type == K_ESCAPE:    #quitting the game
                running = False