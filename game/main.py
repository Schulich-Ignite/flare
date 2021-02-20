# Created by Schulich Ignite Flare and students of Schulich Ignite

import sys
import os
import pygame
from platform import Platform
from player import Player

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

player = Player(400, 500)
player_speed = 5

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.move(0, -player_speed)
    elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player_speed, 0)
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        player.move(0, player_speed)
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player_speed, 0)

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Left button pressed
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player.teleport(mouse_x, mouse_y)
    elif mouse_buttons[1]:  # Scroll wheel pressed
        pass
    elif mouse_buttons[2]:  # Right button pressed
        pass

    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    for platform in platforms:
        pygame.draw.rect(screen, platform.color, platform.rect)

    pygame.draw.rect(screen, player.color, player.rect)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    