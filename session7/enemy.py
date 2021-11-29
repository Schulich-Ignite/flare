import os
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # The default enemy.png image is the same as the walking_right_image
        # Make the image point to the walking_right_image and make walking_left_image a flipped copy of the walking_right_image
        image_location = os.path.join("assets", "enemy.png")
        self.walking_right_image = pygame.image.load(image_location).convert_alpha()
        self.walking_left_image = pygame.transform.flip(self.walking_right_image, True, False)
        self.image = self.walking_right_image

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x_speed = 3
        self.y_speed = 0

        self.walk_speed = 2
        self.walk_time = 2000

    def update(self):
        self.move(self.x_speed, self.y_speed)
        self.walk()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

    def walk(self):
        # Using the time mod walk_time, we can choose if the enemy walks right or left
        time = pygame.time.get_ticks()
        if time % self.walk_time < self.walk_time / 2:
            self.x_speed = self.walk_speed
            self.image = self.walking_right_image
        else:
            self.x_speed = -self.walk_speed
            self.image = self.walking_left_image
        