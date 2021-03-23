import os
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, x_speed, level):
        super().__init__()

        image_location = os.path.join("assets", "bullet.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x_speed = x_speed
        self.level = level

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

    def update(self):
        self.move(self.x_speed, 0)
        self.handle_collisions()
        self.kill_offscreen()

    def handle_collisions(self):
        hit_enemies = pygame.sprite.spritecollide(self, self.level.enemies, True)
        
        # Delete bullets that hit an enemy
        if len(hit_enemies) > 0:
            self.kill()

    def kill_offscreen(self):
        """
        Delete all bullets that are off the left or right edge of the screen.
        This is to save on computer resources after the player shoots a large number of bullets.
        """
        if self.rect.x + self.rect.width < 0 or self.rect.x > 1000:
            self.kill()
