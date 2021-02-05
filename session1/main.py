import sys
import os
import pygame

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

# Create our 50 x 100 rectangle at x = 0, y = 0
rect = pygame.Rect(0, 0, 50, 100)
rect_speed_x = 7
rect_speed_y = 5

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
    
    # Move our rectangle's x and y position by its corresponding x and y speeds
    rect.x += rect_speed_x
    rect.y += rect_speed_y

    # Check if the rectangle has gone out of bounds horizontally
    if rect.x <= 0 or rect.x + rect.width >= SCREEN_WIDTH:
        rect_speed_x *= -1
    
    # Check if the rectangle has gone out of bounds vertically
    if rect.y <= 0 or rect.y + rect.height >= SCREEN_HEIGHT:
        rect_speed_y *= -1

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    pygame.draw.rect(screen, WHITE, rect)  # Draw our rectangle to the screen in white

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    