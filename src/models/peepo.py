import pygame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Peepo:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.image.load("car.gif").convert_alpha()

        self.move_up_pressed = False
        self.move_down_pressed = False
        self.move_left_pressed = False
        self.move_right_pressed = False

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def stop_x(self):
        self.move_left_pressed = False
        self.move_right_pressed = False

    def stop_y(self):
        self.move_up_pressed = False
        self.move_down_pressed = False

    def update(self):
        if self.move_up_pressed:
            self.move_up()
        elif self.move_down_pressed:
            self.move_down()

        if self.move_left_pressed:
            self.move_left()
        elif self.move_right_pressed:
            self.move_right()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides_with(self, obstacle):
        self.image = pygame.image.load("peepo2.png").convert_alpha()
        peepo_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
        return peepo_rect.colliderect(obstacle_rect)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def stop_x(self):
        self.speed = 0

    def stop_y(self):
        self.acceleration = 0

        