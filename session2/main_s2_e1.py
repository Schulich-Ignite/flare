# Session 2 Exercise 1
# Main file
#
# There are some bare tree trunks in the DRAW section and a class called Leaves inside the file leaves.py
# Add some leaves objects to decorate the tree trunks
# Don't worry about getting your coordinates exactly right

import sys
import os
import pygame

from leaves import Leaves
# ------------------------------ Exercise 1 Comments ------------------------------
# Added the line above to import the Leaves class from leaves.py
# To create a leaves object, type the following inside the SETUP section:
#   leaves = Leaves()
# ---------------------------------------------------------------------------------

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
BROWN = (168, 119, 50)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# ------------------------------ Exercise 1 Comments ------------------------------
# Added some rects to draw some tree trunks here
# To create a leaves object, type the following:
#   leaves = Leaves()
# We created the first leaves object as an example, but you'll need to reposition it!
# ---------------------------------------------------------------------------------
tree_trunk_1 = pygame.Rect(200, 300, 20, 80)
tree_trunk_2 = pygame.Rect(400, 450, 20, 80)
tree_trunk_3 = pygame.Rect(600, 350, 20, 80)

leaves_1 = Leaves()
leaves_1.x = 0
leaves_1.y = 0
leaves_1.size = 100
leaves_1.color = (150, 255, 100)

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        pass  # Replace this line
    if keys_pressed[pygame.K_LEFT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_RIGHT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        pass  # Replace this line

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        pass  # Replace this line
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line



    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    # ------------------------------ Exercise 1 Comments ------------------------------
    # Added the tree trunks here
    # Draw the leaves on top - we have added the first leaves as an example
    # ---------------------------------------------------------------------------------
    pygame.draw.rect(screen, BROWN, tree_trunk_1)
    pygame.draw.rect(screen, BROWN, tree_trunk_2)
    pygame.draw.rect(screen, BROWN, tree_trunk_3)

    pygame.draw.rect(screen, leaves_1.color, (leaves_1.x, leaves_1.y, leaves_1.size, leaves_1.size))

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

