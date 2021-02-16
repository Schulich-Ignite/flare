import sys
import os
import pygame
from platform import Platform

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# List of platforms
platforms = []

# Add a platform to the platforms list
def add_platform(x, y, width, height, color):
    p = Platform(x, y, width, height, color)
    platforms.append(p)

add_platform(300, 600, 350, 50, (100, 255, 100))
add_platform(100, 500, 200, 50, (50, 100, 255))
add_platform(650, 450, 200, 50, (50, 100, 255))


while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        


    """
    UPDATE section - manipulate everything on the screen
    """
    
    # SESSION 2 - One simple way to make platforms slowly travel left
    # Commented out for ease of game development
    # for platform in platforms:
    #     platform.rect.x -= 1


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    for platform in platforms:
        pygame.draw.rect(screen, platform.color, platform.rect)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    