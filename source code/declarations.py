import pygame
import random
# Import 'mixer' library for handling music
from pygame import mixer


# Initialize pygame
pygame.init()

# Create the screen
# First parameter is length, second parameter is height (x,y)
screen = pygame.display.set_mode((800,600))

# Creating background image
background = pygame.image.load('space.png')

# Background music
mixer.music.load('background_music.mp3')
mixer.music.play(-1)

# Adding title and icon
pygame.display.set_caption(" Guardians of the Galaxy")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('player_spaceship.png')
# Player coordinates initially
playerX = 370
playerY = 480
# A variable to hold changes in the positions of the player
playerX_change = 0

# Enemy (list to hold number of enemies)
# Level 1 enemy
enemy1_image = []
enemy1X = []
enemy1Y = []
enemy1X_change = []
enemy1Y_change = []
num_of_enemies1 = 10
level1_flag = 0

# for loop to put data to enemy list
for i in range(num_of_enemies1):
    enemy1_image.append(pygame.image.load('alien_1.png'))
    # enemy1 coordinates initially
    enemy1X.append(random.randint(0,735))
    enemy1Y.append(random.randint(50,270))
    # Variables to hold changes in X and Y coordinates of enemy1
    enemy1X_change.append(1)
    enemy1Y_change.append(45)

# Level 2 enemy
enemy2_image = []
enemy2X = []
enemy2Y = []
enemy2X_change = []
enemy2Y_change = []
num_of_enemies2 = 25
level2_flag = 0

# for loop to put data to enemy list
for i in range(num_of_enemies2):
    enemy2_image.append(pygame.image.load('alien_2.png'))
    # enemy2 coordinates initially
    enemy2X.append(random.randint(0,735))
    enemy2Y.append(random.randint(50,270))
    # Variables to hold changes in X and Y coordinates of enemy2
    enemy2X_change.append(1.90)
    enemy2Y_change.append(45)


# Level 3 enemy
enemy3_image = []
enemy3X = []
enemy3Y = []
enemy3X_change = []
enemy3Y_change = []
num_of_enemies3 = 20
level3_flag = 0

# for loop to put data to enemy list
for i in range(num_of_enemies3):
    enemy3_image.append(pygame.image.load('alien_3.png'))
    # enemy3 coordinates initially
    enemy3X.append(random.randint(0,735))
    enemy3Y.append(random.randint(50,250))
    # Variables to hold changes in X and Y coordinates of enemy3
    enemy3X_change.append(1)
    enemy3Y_change.append(45)


# Level 4 enemy
enemy4_image = []
enemy4X = []
enemy4Y = []
enemy4X_change = []
enemy4Y_change = []
num_of_enemies4 = 27
level4_flag = 0

# for loop to put data to enemy list
for i in range(num_of_enemies4):
    enemy4_image.append(pygame.image.load('alien_4.png'))
    # enemy4 coordinates initially
    enemy4X.append(random.randint(0,735))
    enemy4Y.append(random.randint(50,250))
    # Variables to hold changes in X and Y coordinates of enemy4
    enemy4X_change.append(1.75)
    enemy4Y_change.append(50)


# Level 5 enemy
enemy5_image = pygame.image.load('alien_5.png')
enemy5X = random.randint(3,670)
enemy5Y = random.randint(10,300)
enemy5X_change = 2.5
enemy5Y_change = 50
level5_flag = 0



# Bullet
bullet_image = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 3
# Ready state --> Currently the player can't see the bullet
# Fire state --> Bullet is moving
bullet_state = "ready"

# Enemy bullet
enemy_bullet_image = pygame.image.load('enemy_bullet.png')
enemy_bulletY_change = 3


# Timer
play_time1 = 60  # time in seconds
play_time2 = 90  # time in seconds
play_time3 = 120  # time in seconds
play_time4 = 150  # time in seconds
play_time5 = 200  # time in seconds

# A boolean variable that stores whether the game has ended if the time limit is crossed
game_ended = False

# A variable for game screens
flag = -1

# A variable to hold level number
level = 1

# A variable to indicate that the program/game is running
running = True

# Score variable
score = 0
# Score font style and size
font = pygame.font.Font('college.ttf',40)

# Variable to count time gaps at which enemy shoots the bullet
h = 0
# Variable to generate enemy at another random position in level 5
r = 0

# Temporary variable to play bgm only once
bg_temp = 0