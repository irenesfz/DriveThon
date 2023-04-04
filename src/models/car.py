import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CAR_WIDTH, CAR_HEIGHT, CAR_START_X, CAR_START_Y

class Car:
    def __init__(self):
        self.image = pygame.image.load("car.png")
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.x = CAR_START_X
        self.y = CAR_START_Y
        self.vel = 0
        self.max_vel = 10
        self.acceleration = 0.2
        self.friction = 0.1

    def update(self):
        self.handle_keys()
        self.move()

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel -= self.acceleration
        elif keys[pygame.K_RIGHT]:
            self.vel += self.acceleration
        else:
            if self.vel > 0:
                self.vel -= self.friction
            elif self.vel < 0:
                self.vel += self.friction
        if self.vel > self.max_vel:
            self.vel = self.max_vel
        elif self.vel < -self.max_vel:
            self.vel = -self.max_vel

    def move(self):
        self.x += self.vel
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.vel = 0
        elif self.x < 0:
            self.x = 0
            self.vel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
