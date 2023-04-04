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

    def update(self):
        self.y += self.vel

    def off_screen(self):
        return self.y > SCREEN_HEIGHT

    def collision(self, car):
        return car.x < self.x + self.width and car.x + car.width > self.x and car.y < self.y + self.height and car.y + car.height > self.y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
