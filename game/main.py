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

# Platforms sprite group
platforms = pygame.sprite.Group()

platforms.add(Platform(300, 600, 350, 50))
platforms.add(Platform(100, 500, 200, 50))
platforms.add(Platform(650, 450, 200, 50))
platforms.add(Platform(700, 650, 200, 25))

# Create the player sprite and add it to the players sprite group
player = Player(400, 500)
players = pygame.sprite.Group()
players.add(player)

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
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        player.jump()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        player.move(-player.move_speed, 0)
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        player.move(player.move_speed, 0)
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        pass  # Now that we have platforms, there's no reason to make the player move down.

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        player.teleport(mouse_pos[0], mouse_pos[1])
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line

    """
    UPDATE section - manipulate everything on the screen
    """
    
    players.update()

    hit_platforms = pygame.sprite.spritecollide(player, platforms, False)
    for platform in hit_platforms:
        player.on_platform_collide(platform)

    if len(hit_platforms) == 0:
        player.can_jump = False

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    
    platforms.draw(screen)
    players.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
    