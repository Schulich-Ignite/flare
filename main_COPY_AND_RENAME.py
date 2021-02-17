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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Useful variables
rect_x = 20
rect_y = 20
rect_width = 20
rect_height = 20
rect_speed = 5
rect_color = WHITE
while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        # /--------------------------------/
        # The first way of interacting with events
        """"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < screen_width - width:
                rect_x += rect_speed
            elif event.key == pygame.K_LEFT and x > 0:
                rect_x -= rect_speed
            elif event.key == pygame.K_UP and y > 0:
                rect_y -= rect_speed
            elif event.key == pygame.K_DOWN and y < screen_height - height:
                rect_y += rect_speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("You pressed the left mouse botton!")
                color = RED # Change colour to red
            elif event.button == 3:
                print("You pressed the right mouse button!")
                color = GREEN # Change colour to green
            elif event.button == 2:
                # add your own code
                print("You pressed the mouse wheel button!")
            elif event.buttom == 4:
                # add your own code
                print("You used the mouse wheel scroll up!")
            elif event.buttom == 5:
                # add your own code
                print("You used the mouse wheel scroll down!")
            """

    # /--------------------------------/
    # The second way of interacting with events

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect_y > 0:
        # y > 0 so we can't go out of our screen, try getting
        # rid of it and see what happens if you go up
        rect_y -= rect_speed # Going up
    elif keys[pygame.K_LEFT] and rect_x > 0:
        # x > 0 so we can't go out of our screen
        rect_x -= rect_speed # Going left
    elif keys[pygame.K_RIGHT] and rect_x < SCREEN_WIDTH - rect_width:
        # x < screen_width - width so we can't go out of our screen
        rect_x += rect_speed # Going right
    elif keys[pygame.K_DOWN] and rect_y < SCREEN_HEIGHT - rect_height:
        # y < screen_height - height so we can't go out of our screen
        rect_y += rect_speed # Going down

    # /-----------------------------/
    # Mouse events
    mouses = pygame.mouse.get_pressed()
    # runs while you hold it
    if(mouses[0]): # If left mouse pressed
        mouse_pos = pygame.mouse.get_pos() # get position of mouse
        # (x, y) coordinates
        # move rectangle where the mouse is
        rect_x = mouse_pos[0]
        rect_y = mouse_pos[1]
    elif(mouses[2]): # If right mouse pressed
        color = GREEN # Change colour to green

    # /--------------------------------/
    # Could also do this example for getting mouse coordinates
    """
    used to get position of mouse
    mouse_pos = pygame.mouse.get_pos()
   
    if(mouse_pos[0] > (screen_width / 2)):
        colour = (255, 255, 255) # Change colour to white if mouse is
                                 # in the right half of the screen
    elif(mouse_pos[1] > (screen_height / 2)):
        colour = (100,100,100) # Change colour to gray if mouse is
                               # bottom half of the screen
    """


    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))


    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    