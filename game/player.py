import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_location = os.path.join("assets", "player.png")
        self.image = pygame.image.load(image_location).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.move_speed = 5
 
    def update(self):
        # Make the player slowly fall down over time
        self.move(0, 1)

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change 
        
    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y