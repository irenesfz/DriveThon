import pygame
import random
from src.models.peepo import Peepo
from src.models.obstacle import Obstacle
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, ROAD_SPEED,CAR_START_X, CAR_START_Y, CAR_WIDTH, CAR_HEIGHT, CAR_SPEED

class MainGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.peepo = Peepo(CAR_START_X, CAR_START_Y, CAR_WIDTH, CAR_HEIGHT, CAR_SPEED)
        self.obstacles = []
        self.game_over = False
        self.background_image = pygame.image.load("background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.road_y = 0
        self.score = 0
        self.fails = 0
        self.score = 0
        self.lives = 3
        self.font = pygame.font.SysFont(None, 25)
        self.peepo_collided = False
        self.last_collision_time = None

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_image = font.render(text, True, color)
        self.screen.blit(text_image, (x, y))


    def start(self):
        peepo_speed_x = 0
        peepo_speed_y = 0
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    break
                # Handle arrow key events to move the peepo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        peepo_speed_y = -self.peepo.speed
                    elif event.key == pygame.K_DOWN:
                        peepo_speed_y = self.peepo.speed
                    elif event.key == pygame.K_LEFT:
                        peepo_speed_x = -self.peepo.speed
                    elif event.key == pygame.K_RIGHT:
                        peepo_speed_x = self.peepo.speed
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        peepo_speed_y = 0
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        peepo_speed_x = 0

            self.screen.blit(self.background_image, (0, 0)) # Dibujar el fondo primero

            # Update the position of the road
            self.road_y += ROAD_SPEED
            if self.road_y > ROAD_HEIGHT:
                self.road_y = 0

            # Draw the road
            # self.screen.blit(self.road_image, (0, self.road_y - ROAD_HEIGHT))
            # self.screen.blit(self.road_image, (0, self.road_y))

            self.peepo.move(peepo_speed_x, peepo_speed_y)
            self.peepo.update()
            self.peepo.draw(self.screen)

            # Generate new obstacle
            if random.random() < 0.01:
                new_obstacle = Obstacle(random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH), -OBSTACLE_HEIGHT)
                self.obstacles.append(new_obstacle)
            
            obstacles_to_remove = []
            # Update obstacles
            for obstacle in self.obstacles:
                obstacle.update()
                obstacle.draw(self.screen)

                if self.peepo.collides_with(obstacle):
                    obstacles_to_remove.append(obstacle)
                    self.fails += 1
                    fail_text = self.font.render("Fails: {}".format(self.fails), True, (255, 0, 0))
                    self.screen.blit(fail_text, (10, 35))
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over = True
                        break
                    
                else:
                    if obstacle.y > CAR_START_Y and obstacle.y < CAR_START_Y + CAR_HEIGHT:
                        self.score += 1

            # Remover obstáculos
            for obstacle in obstacles_to_remove:
                self.obstacles.remove(obstacle)
            
            score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255),pygame.Color('red'))
            self.screen.blit(score_text, (10, 10))

            fail_text = self.font.render("Fails: {}".format(self.fails), True, (255, 255, 255),pygame.Color('red'))
            self.screen.blit(fail_text, (10, 35))

            # Remove obstacles that have gone off screen
            self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.y < SCREEN_HEIGHT]

            # Actualizar la pantalla
            pygame.display.flip()

            # Limitar la velocidad de fotogramas
            self.clock.tick(60)

        # Quit the game
        pygame.quit()

