import os
import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "player.png")
        self.walking_right_image = pygame.image.load(image_location).convert_alpha()
        self.walking_left_image = pygame.transform.flip(self.walking_right_image, True, False)
        self.image = self.walking_right_image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.move_speed = 5
        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.6
        
        self.can_jump = True

        self.direction = "right"

        self.bullets = pygame.sprite.Group()
        self.bullet_cooldown = 500
        self.last_bullet_time = -99999


    def update(self):
        # Move the player based on whatever the x_speed and y_speed are
        self.move(self.x_speed, self.y_speed)
        
        # Make the player fall due to gravity
        self.fall()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change 
        
        if x_change > 0:
            self.direction = "right"
            self.image = self.walking_right_image
        elif x_change < 0:
            self.direction = "left"
            self.image = self.walking_left_image

    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def fall(self):
        self.y_speed += self.gravity

    def jump(self):
        if not self.can_jump:
            return
        self.y_speed = -15

    def on_platform_collide(self, platform):
        # Need to set self.rect.y explicitly to avoid having the player clip through the floor
        # Note a new bug surfaces - players jumping from the underside will teleport to the top. This is left for students to solve if interested
        self.rect.y = platform.rect.y - self.rect.height
        
        self.y_speed = 0
        self.can_jump = True

    def create_new_bullet(self, level):
        # Check if the last time a bullet was shot was lesser than the bullet cooldown time
        time = pygame.time.get_ticks()
        if time - self.last_bullet_time < self.bullet_cooldown:
            return  # Not enough time has elapsed since the last bullet, escape early

        bullet_x = 0
        bullet_y = self.rect.y + self.rect.height / 2
        bullet_x_speed = 0
        
        if self.direction == "right":
            bullet_x = self.rect.x + self.rect.width
            bullet_x_speed = 5
        else:
            bullet_x = self.rect.x
            bullet_x_speed = -5

        # Create a bullet and add it to the player's bullet group
        self.bullets.add(Bullet(bullet_x, bullet_y, bullet_x_speed, level))

        # Set the last bullet time to the time the latest bullet was fired
        self.last_bullet_time = time
