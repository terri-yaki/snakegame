import pygame
from pygame.locals import *
import os
import time

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("res/block.png").convert()
        self.x = 250
        self.y = 250
        
    def draw(self):
        self.surface.fill((110,110,5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
        
    def move_left(self):
        self.x -= 10
        self.draw()
    
    def move_right(self):
        self.x += 10
        self.draw()
        
    def move_down(self):
        self.y -= 10
        self.draw()
        
    def move_up(self):
        self.y += 10
        self.draw()
        
class Game:
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.draw()
        
    def run(self):
        window = pygame.display.set_mode(size=(640,640))   #initialize and set window size
        window.fill((255,255,255))  #background(rgb)
            
        block = pygame.image.load("res/block.png").convert()
        blockX = 320
        blockY = 320
        window.blit(block, (blockX, blockY))
        
        pygame.display.flip();
            
        running = True
            
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:       #when a key is pressed
                    if event.key == K_ESCAPE:      #escape the window
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:    #quitting the game
                        running = False
                pygame.quit()
    
    
if __name__ == "__main__":
    game = Game()
    game.run()