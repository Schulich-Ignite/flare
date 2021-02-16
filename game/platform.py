import pygame

class Platform:
    def __init__(self, x, y, width, height, color):
        #    self.x = x
        #    self.y = y
        #    self.width = width
        #    self.height = height

        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
