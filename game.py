# Create the car
car = Car()

# Create the obstacles
obstacles = []

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.move_left()
            if event.key == pygame.K_RIGHT:
                car.move_right()
    
    # Update the game state
    for obstacle in obstacles:
        obstacle.update()
        if obstacle.off_screen():
            obstacles.remove(obstacle)
        if obstacle.collision(car):
            running = False
    if len(obstacles) < 5:
        obstacles.append(Obstacle())
    
    # Draw the game
    screen.fill((255, 255, 255))
    car.draw()
    for obstacle in obstacles:
        obstacle.draw()
