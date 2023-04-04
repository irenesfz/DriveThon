import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Road:
    def __init__(self):
        self.image = pygame.image.load("road.png").convert()
        self.y = 0
        self.speed = 5

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - SCREEN_HEIGHT))
