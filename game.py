# Create the peepo
peepo = Peepo()

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
                peepo.move_left()
            if event.key == pygame.K_RIGHT:
                peepo.move_right()
    
    # Update the game state
    for obstacle in obstacles:
        obstacle.update()
        if obstacle.off_screen():
            obstacles.remove(obstacle)
        if obstacle.collision(peepo):
            running = False
    if len(obstacles) < 5:
        obstacles.append(Obstacle())
    
    # Draw the game
    screen.fill((255, 255, 255))
    peepo.draw()
    for obstacle in obstacles:
        obstacle.draw()
