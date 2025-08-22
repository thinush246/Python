import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load('L35-36/background.png')

# Sound
mixer.music.load("L35-36/background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('L35-36/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('L35-36/player.png')
playerX = 370
playerY = 380
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemy Img.append(pygame.image.load('L35-36/enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4) #make the alien moving right automatically
    enemyY_change.append(40) #make the alien moving down automatically

# Bullet
# Ready You can't see the bullet on the screen
# Fire The bullet is currently moving
bulletImg = pygame.image.load('L35-36/bullet.png')
bulletx = 0
bulletY = 380
bulletX_change = 0
bullety_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
score = font.render("Score : " + str(score_value), True, (255, 255, 255))
screen.blit(score, (x, y))

def game_over_text():
over text = over_fon.render("GAME OVER", True, (255, 255, 255))
screen.blit(over_text, (200, 250))