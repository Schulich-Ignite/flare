import sys
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
# format is (R,G,B) where each value is 0-255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (139, 7, 54)

# Initialized the rectangle
rectangle = pygame.Rect(50, 50, 100, 100)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Create our platforms, passing in x,y,width,height
platform = Platform(300, 700, 200, 50)
platform1 = Platform(600, 600, 200, 50)

# create a sprite group for the platforms
platforms = pygame.sprite.Group()
# add the platforms to the sprite group
platforms.add(platform, platform1)

# Initialize the player
player = Player()

# Create a sprite group for the player
players = pygame.sprite.Group()
# Add the player to the sprite group
player.add(players)

teleport = False

direction = [0, 0]

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

    direction = [0, 0]
    teleport = False

    if keys_pressed[pygame.K_a]:
        print("letter pressed")
    if keys_pressed[pygame.K_4]:
        print("number pressed")

    # Mouse events
    mouse_pos = (
        pygame.mouse.get_pos()
    )  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        teleport = True  # Replace this line
    if mouse_buttons[2]:  # If right mouse pressed
        teleport = True  # Replace this line

    """
    UPDATE section - manipulate everything on the screen
    """

    # stop the player if they hit a platform!
    for platform in platforms:
        if pygame.sprite.collide_rect(player, platform):
            player.y_speed = 0  # change their y speed to 0
            player.rect.y = platform.rect.y - (
                player.rect.height
            )  # make sure they aren't "stuck" in a platform

    # update the player!
    player.update(keys_pressed)

    # teleport to mouse click
    if teleport:
        player.teleport(mouse_pos)

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    # draw the sprite groups
    players.draw(screen)
    platforms.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(
        FRAME_RATE
    )  # Pause the clock to always maintain FRAME_RATE frames per second
