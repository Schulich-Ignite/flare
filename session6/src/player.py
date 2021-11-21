import pygame
import os


GRAVITY = 0.25
JUMP_VELOCITY = -1 * 12


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_speed = 5  # speed in the x direction
        self.y_speed = 0  # speed in the y direction
        image_location = os.path.join("assets", "player.png")  # Find the path of the player image
        self.image = pygame.image.load(image_location).convert_alpha()  # load the image
        self.rect = self.image.get_rect()  # get the rect of the image
        self.rect.x = 400  # have the player start at 400 on x axis

        self.jump_cooldown = 0  # the player can jump right away!

    # how do we want to implement the other actions?

    def update(self, keys_pressed):

        # Setup

        # Events -> move these in from the main loop

        # Get input

        # reset direction so that the player stops moving when keys not pressed
        direction = [0, 0]
        if keys_pressed[pygame.K_UP]:
            direction[1] = -1  # y direction goes up
        if keys_pressed[pygame.K_DOWN]:
            direction[1] = 1  # y direction goes down
        if keys_pressed[pygame.K_LEFT]:
            direction[0] = -1  # x direction goes left
        if keys_pressed[pygame.K_RIGHT]:
            direction[0] = 1  # x direction goes right

        if keys_pressed[pygame.K_SPACE]:
            # this will run if space is pressed
            # JUMP LOGIC
            if self.jump_cooldown == 0:  # this will run if jump_cooldown is 0
                self.jump_cooldown = 30  # reset the cooldown to 30 frames
                self.y_speed += JUMP_VELOCITY  # add velocity for the jump (must be greater than gravity to work properly)
        # Updates

        self.rect.x += direction[0] * self.x_speed
        # self.rect.y += direction[1] * self.speed
        # remove gravity, jump code & uncomment the above line to remove platformer physics

        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position

        # if jump_cooldown is >= 1, subtract by 1 to lower the cooldown
        # this happens every frame, so jump_cooldown is
        # the number of frames between when the player is allowed to jump
        # when jump_cooldown is 0, we can jump again!
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1

    # teleport to mouse position
    def teleport(self, mousepos):
        x = mousepos[0]
        y = mousepos[1]
        self.rect.x = x
        self.rect.y = y
