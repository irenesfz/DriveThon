import pygame
import random
from src.models.car import Car
from src.models.obstacle import Obstacle
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT

class MainGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.car = Car()
        self.obstacles = []
        self.game_over = False
    
    def start(self):
        clock = pygame.time.Clock()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break

            self.screen.fill((255, 255, 255))

            self.car.update()
            self.car.draw(self.screen)

            # Generate new obstacle
            if random.random() < 0.01:
                new_obstacle = Obstacle(random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH), -OBSTACLE_HEIGHT)
                self.obstacles.append(new_obstacle)

            # Update obstacles
            for obstacle in self.obstacles:
                obstacle.update()
                obstacle.draw(self.screen)

                if self.car.collides_with(obstacle):
                    self.game_over = True
                    break

            # Remove obstacles that have gone off screen
            self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.y < SCREEN_HEIGHT]

            pygame.display.flip()
            clock.tick(60)

        # Quit the game
        pygame.quit()
