import pygame
import random
from pygame import mixer

# Starting the mixer
mixer.init()

surf_color = (0, 142, 204)
color = (0, 0, 0)

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):  # fixed __init__
        super().__init__()  # fixed super()

        self.image = pygame.Surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))  # fixed pygame.Rect
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed / 10

    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10

bg = pygame.image.load("Lesson 34/bg.jpeg")
bg = pygame.transform.scale(bg, (500, 400))

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

all_sprites_list = pygame.sprite.Group()

# Add a sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

# Add one enemy
rad = 20
cxp = random.randint(0, 480)
cyp = random.randint(0, 370)
sp2 = Sprite((255, 0, 0), 20, 30)
sp2.rect.x = cxp
sp2.rect.y = cyp
all_sprites_list.add(sp2)

exit_game = True
clock = pygame.time.Clock()

while exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False  # fixed syntax error
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit_game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_DOWN]:
        sp1.moveForward(5)
    if keys[pygame.K_UP]:
        sp1.moveBack(5)

    all_sprites_list.update()
    screen.fill(surf_color)
    screen.blit(bg, (0, 0))
    all_sprites_list.draw(screen)

    if sp1.rect.colliderect(sp2.rect):
        all_sprites_list.remove(sp2)
        text = "You win!"

        # Load the font
        font = pygame.font.SysFont("Courier", 72)

        # Render the text in a new surface
        text_surface = font.render(text, True, (158, 16, 16))
        screen.blit(text_surface, (200 - text_surface.get_width() // 2, 140 - text_surface.get_height() // 2))  # fixed text placement

        # Load the audio
        mixer.music.load("Lesson 34/explosion.wav")
        mixer.music.set_volume(0.7)
        mixer.music.play()

    pygame.display.update()
    clock.tick(60)

pygame.quit()