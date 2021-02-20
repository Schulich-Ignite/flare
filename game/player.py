import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = (100, 100, 255)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y