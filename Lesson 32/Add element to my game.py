import pygame
import sys

# Initialize pygame
pygame.init()

# Window size
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Set caption
pygame.display.set_caption("My first game screen")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle settings
rect_width, rect_height = 100, 60
rect_x = (window_size[0] - rect_width) // 2
rect_y = (window_size[1] - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Font and text
font = pygame.font.SysFont(None, 48)
text = font.render("Hello Pygame!", True, (0, 0, 0))  # black text
text_rect = text.get_rect(center=(window_size[0]//2, window_size[1]//2 + 100))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rectangle)

    # Display text
    screen.blit(text, text_rect)

    # Update screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()