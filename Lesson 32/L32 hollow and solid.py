import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((400, 400))

# Fill the screen with white color
window.fill((255, 255, 255))

# Define colors
RED = (255, 0, 0)

# Draw solid circle
pygame.draw.circle(window, RED, (300, 300), 50)

# Draw outlined circle
pygame.draw.circle(window, RED, (100, 100), 50, 3)

# Draws the surface object to the screen.
pygame. display. update()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
# Ouit pygame
pygame.quit()
