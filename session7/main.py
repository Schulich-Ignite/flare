import sys
import pygame

from platform import Platform

from player import Player

from enemy import Enemy

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors
# Format is (R, G, B) where each value is 0-255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Create our platforms, passing in x, y, width, height
platform1 = Platform(300, 700, 200, 50)
platform2 = Platform(600, 600, 200, 50)

# Create a sprite group for the platforms
platforms = pygame.sprite.Group()
# Add the platforms to the sprite group
platforms.add(platform1, platform2)

# Initialize the player
player = Player()

# Create a sprite group for the player
players = pygame.sprite.Group()
# Add the player to the sprite group
player.add(players)

# Initialize the enemy
enemy = Enemy()
# Initialize the sprite group
enemies = pygame.sprite.Group()
# Add enemy to the sprite group
enemies.add(enemy)


while True:
    """
    EVENTS section - how the code reacts when users do things
    """

    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
        ):  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()

    # Examples of how to get key input
    if keys_pressed[pygame.K_a]:
        print("Letter pressed")
    if keys_pressed[pygame.K_1]:
        print("Number pressed")

    # Mouse events
    # Get position of mouse as a tuple representing the (x, y) coordinate
    mouse_pos = pygame.mouse.get_pos()

    mouse_buttons = pygame.mouse.get_pressed()

    """
    UPDATE section - manipulate everything on the screen
    """

    # Stop the player if they hit a platform!
    for platform in platforms:
        if pygame.sprite.collide_rect(player, platform):
            player.y_speed = 0  # Change their y speed to 0
            # player.grounded = True
            # player.rect.y = (
            #    platform.rect.y - player.rect.height
            # )  # Make sure they aren't "stuck" in a platform

    # If the player collides with the enemy
    if pygame.sprite.collide_rect(player, enemy):

        # from above, kill the enemy
        if player.rect.y + player.rect.height <= enemy.rect.y + 10:
            enemy.kill()
            enemy.alive = False
        # from the side (player / enemy walk into each other), kill the player
        elif enemy.alive:
            player.kill()

    # Update the player
    player.update(keys_pressed, mouse_buttons, mouse_pos)
    enemy.update((platform1.rect.x, platform1.rect.x + platform.rect.width))
    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    # Draw the sprite groups
    players.draw(screen)
    platforms.draw(screen)
    enemies.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(
        FRAME_RATE
    )  # Pause the clock to always maintain FRAME_RATE frames per second
