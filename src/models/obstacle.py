import pygame
import random
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, OBSTACLE_MIN_SPEED, OBSTACLE_MAX_SPEED

class Obstacle:
    def __init__(self, x, y):
        self.image = pygame.image.load("obstacle.png").convert_alpha()
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.x = x
        self.y = y
        self.vel = random.randint(OBSTACLE_MIN_SPEED, OBSTACLE_MAX_SPEED)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.vel
        self.rect.y = self.y

    def off_screen(self):
        return self.y > SCREEN_HEIGHT

    def collision(self, peepo):
        return self.rect.colliderect(peepo.rect)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
