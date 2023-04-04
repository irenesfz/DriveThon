import pygame
from src.views.main_game import MainGame
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the main game instance
game = MainGame(screen)

# Start the game loop
game.start()