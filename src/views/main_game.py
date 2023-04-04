import pygame
import random
from src.models.car import Car
from src.models.obstacle import Obstacle
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, ROAD_SPEED,CAR_START_X, CAR_START_Y, CAR_WIDTH, CAR_HEIGHT, CAR_SPEED


class MainGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.car = Car(CAR_START_X, CAR_START_Y, CAR_WIDTH, CAR_HEIGHT, CAR_SPEED)
        self.obstacles = []
        self.game_over = False
        self.road_image = pygame.image.load("road.png").convert()
        self.road_y = 0
        self.score = 0
        self.fails = 0
        self.score = 0
        self.lives = 3
        self.font = pygame.font.SysFont(None, 25)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_image = font.render(text, True, color)
        self.screen.blit(text_image, (x, y))


    def start(self):
        self.draw_text(f"Score: {self.score}", 24, (255, 255, 255), 10, 10)
        self.draw_text(f"Lives: {self.lives}", 24, (255, 255, 255), SCREEN_WIDTH - 100, 10)
        clock = pygame.time.Clock()
        car_speed_x = 0
        car_speed_y = 0
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                # Handle arrow key events to move the car
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        car_speed_y = -self.car.speed
                    elif event.key == pygame.K_DOWN:
                        car_speed_y = self.car.speed
                    elif event.key == pygame.K_LEFT:
                        car_speed_x = -self.car.speed
                    elif event.key == pygame.K_RIGHT:
                        car_speed_x = self.car.speed
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        car_speed_y = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        car_speed_x = 0

            self.screen.fill((255, 255, 255))

            # Update the position of the road
            self.road_y += ROAD_SPEED
            if self.road_y > ROAD_HEIGHT:
                self.road_y = 0

            # Draw the road
            self.screen.blit(self.road_image, (0, self.road_y - ROAD_HEIGHT))
            self.screen.blit(self.road_image, (0, self.road_y))

            self.car.move(car_speed_x, car_speed_y)
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
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over = True
                        break
                else:
                    if obstacle.y > CAR_START_Y and obstacle.y < CAR_START_Y + CAR_HEIGHT:
                        self.score += 1
            
            score_text = self.font.render("Score: {}".format(self.score), True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            fail_text = self.font.render("Fails: {}".format(self.fails), True, (0, 0, 0))
            self.screen.blit(fail_text, (10, 35))

            # Remove obstacles that have gone off screen
            self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.y < SCREEN_HEIGHT]

            pygame.display.flip()
            clock.tick(60)

        # Quit the game
        pygame.quit()