import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    
surface = pygame.display.set_mode((400, 400))
surfac.fill((255,255,255))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pass
        elif event.type == QUIT:
            running = False