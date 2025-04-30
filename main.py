import os
os.environ['DISPLAY'] = ':0'  # Try this before pygame.init()
import pygame
from constants import *

def main():
    print("Initializing pygame...")
    pygame.init()
    print("Creating window...")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Window created!")
    
    # Game loop
    print("Starting game loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected!")
                return
                
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()