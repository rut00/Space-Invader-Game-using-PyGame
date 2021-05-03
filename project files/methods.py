import pygame
import math

from declarations import *

# Initialize pygame
pygame.init()

# Function for home screen
def home_page():
    mouse_position = pygame.mouse.get_pos()
    home_font = pygame.font.Font('college.ttf', 140)
    play_font = pygame.font.Font('college.ttf', 50)
    screen.blit(home_font.render("-----------", True, (255, 255, 255)), (25, 20))
    screen.blit(home_font.render("SPACE", True, (255, 255, 255)), (210, 130))
    screen.blit(home_font.render("INVADERS", True, (255, 255, 255)), (100, 270))
    screen.blit(home_font.render("-----------", True, (255, 255, 255)), (25, 390))
    screen.blit(play_font.render("PLAY", True, (0, 255, 0)), (335, 490))
    if mouse_position[0]>=332 and mouse_position[0]<=450 and mouse_position[1]>=488 and mouse_position[1]<=540:
        screen.blit(play_font.render("PLAY", True, (255, 255, 0)), (335, 490))

# Function to check whether the position of cursor is within the specified range (on the 'Play' option)
def play():
    mouse_position = pygame.mouse.get_pos()
    if mouse_position[0]>=332 and mouse_position[0]<=450 and mouse_position[1]>=488 and mouse_position[1]<=540:
        return True
    else:
        return False

# Function to show time left
def time_left(timeLeft):
    font = pygame.font.Font('college.ttf',35)
    time_text = font.render("TIME LEFT: " + str(timeLeft), True, (255, 255, 255))
    screen.blit(time_text, (535, 10))

# Function to display the player has won the game
def won():
    winner = pygame.image.load('winner.png')
    screen.blit(winner,(355,100))
    mouse_position = pygame.mouse.get_pos()
    g_font = pygame.font.Font('college.ttf', 75)
    g = g_font.render("YOU WON THE GAME", True, (0, 255, 255))
    screen.blit(g, (70, 260))
    p_font = pygame.font.Font('college.ttf', 50)
    p = p_font.render("PLAY AGAIN", True, (255, 0, 0))
    screen.blit(p, (280, 370))
    if mouse_position[0] >= 275 and mouse_position[0] <= 540 and mouse_position[1] >= 370 and mouse_position[1] <= 415:
        p = p_font.render("PLAY AGAIN", True, (0, 255, 0))
        screen.blit(p, (280, 370))

# Function to display Game over
def game_over():
    mouse_position = pygame.mouse.get_pos()
    g_font = pygame.font.Font('college.ttf',100)
    g = g_font.render("GAME OVER",True,(255,255,255))
    screen.blit(g, (155,200))
    p_font = pygame.font.Font('college.ttf',50)
    p = p_font.render("PLAY AGAIN",True,(255,0,0))
    screen.blit(p, (280,370))
    if mouse_position[0] >= 275 and mouse_position[0] <= 540 and mouse_position[1] >= 370 and mouse_position[1] <= 415:
        p = p_font.render("PLAY AGAIN", True, (0, 255, 0))
        screen.blit(p, (280, 370))

# Function to check whether the position of cursor is within the specified range (on the 'Play Again' option)
def play_again():
    mouse_position = pygame.mouse.get_pos()
    if mouse_position[0] >= 275 and mouse_position[0] <= 540 and mouse_position[1] >= 370 and mouse_position[1] <= 415:
        return True
    else:
        return False

# Function for the position of the player
def player(x,y):
    screen.blit(player_image,(x,y))

# Function for the position of enemy1
def enemy1(x,y,i):
    screen.blit(enemy1_image[i],(x,y))

# Function for the position of enemy2
def enemy2(x,y,i):
    screen.blit(enemy2_image[i],(x,y))

# Function for the position of enemy3
def enemy3(x,y,i):
    screen.blit(enemy3_image[i],(x,y))

# Function for the position of enemy4
def enemy4(x,y,i):
    screen.blit(enemy4_image[i],(x,y))

# Function for the position of enemy5
def enemy5(x,y):
    screen.blit(enemy5_image,(x,y))

# Function to check the collision of bullet with enemy or the collision of enemy bullet with the player
def isCollision(x1,y1,x2,y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
    if distance < 27:
        return True
    else:
        return False

# Function to check the collision of bullet with enemy or the collision of enemy bullet with the player in level 5
def isCollision5(x1,y1,x2,y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) + (math.pow(y1 - y2,2)))
    if distance < 45:
        return True
    else:
        return False
