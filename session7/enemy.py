import os
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "enemy.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()

        # Set the x and y values of the image
        self.rect.x = 300
        self.rect.y = 700 - self.rect.height

        # Make the player start nice and slow
        self.x_speed = 1

        # Need to track so dead enemy doesn't kill the player (see main)
        self.alive = True

    def update(self, platform):

        self.rect.x += self.x_speed

        # Right edge of the platform || left edge of the platform
        if self.rect.x + self.rect.width >= platform[1] or self.rect.x <= platform[0]:
            # invert x direction
            self.x_speed = -self.x_speed
            # flip the direction the enemy is facing
            self.image = pygame.transform.flip(self.image, True, False)
