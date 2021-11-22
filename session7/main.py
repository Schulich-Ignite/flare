# Created by Schulich Ignite Flare and students of Schulich Ignite

import sys
import os
import pygame
from platform import Platform
from player import Player
from enemy import Enemy
from level import Level

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

# List of all levels
# Each level has a list of platforms and a list of enemies
# Each level has an optional third parameter called player_spawn that sets where the player will first appear
levels = [
    # Level 0
    Level([
        Platform(300, 600, 350, 50),
        Platform(100, 500, 200, 50),
        Platform(650, 450, 250, 50),
        Platform(700, 650, 200, 25)
    ], [
        Enemy(750, 410)
    ], (400, 500)),
    # Level 1
    Level([
        Platform(250, 600, 400, 50),
        Platform(100, 700, 200, 50),
        Platform(650, 300, 250, 50),
        Platform(700, 650, 200, 25),
        Platform(500, 450, 100, 25)
    ], [
        Enemy(750, 260),
        Enemy(150, 660),
    ], (400, 500)),
    # Level 2
    Level([
        Platform(50, 750, 350, 25),
        Platform(500, 700, 200, 50),
        Platform(700, 600, 150, 25),
        Platform(425, 400, 200, 25),
        Platform(150, 350, 200, 50)
    ], [
        Enemy(600, 660),
        Enemy(750, 560),
        Enemy(500, 360),
        Enemy(200, 310)
    ], (100, 650))
]

# Set the current level to be the first level in the game
level = levels[0]

# Start the next level


def next_level(level, levels):
    """
    Start the next level from the list of levels
    """

    # Get the next level by getting the index of the current level and adding one
    # Note there's a new bug: When the last level is finished, the next level doesn't exist
    new_level_index = levels.index(level) + 1
    new_level = levels[new_level_index]
    return new_level


# Create the player sprite and add it to the players sprite group
player = Player(400, 500)
players = pygame.sprite.Group()
players.add(player)

level.start(player)

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
        # Now that we have platforms, there's no reason to make the player move down.
        pass

    if keys_pressed[pygame.K_SPACE]:
        player.create_new_bullet(level)

    # Mouse events
    # Get position of mouse as a tuple representing the
    mouse_pos = pygame.mouse.get_pos()
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
    level.enemies.update()
    player.bullets.update()

    # Handle collisions with platforms
    hit_platforms = pygame.sprite.spritecollide(player, level.platforms, False)
    for platform in hit_platforms:
        player.on_platform_collide(platform)

    if len(hit_platforms) == 0:
        player.can_jump = False

    # Handle collisions with enemies
    hit_enemies = pygame.sprite.spritecollide(player, level.enemies, False)
    for enemy in hit_enemies:
        # Check if collision is from "above", with 15 pixels margin of error
        if player.rect.y + player.rect.height < enemy.rect.y + 15:
            enemy.kill()
        else:
            player.kill()

    # When all the enemies are defeated in a level, start the next level
    if len(level.enemies) == 0:
        level = next_level(level, levels)

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    level.platforms.draw(screen)
    players.draw(screen)
    level.enemies.draw(screen)
    player.bullets.draw(screen)

    # Pygame uses a double-buffer, without this we see half-completed frames
    pygame.display.flip()
    # Pause the clock to always maintain FRAME_RATE frames per second
    clock.tick(FRAME_RATE)
