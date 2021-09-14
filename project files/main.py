import time
from methods import *
from declarations import *

# Initialize pygame
pygame.init()

# Function to display score
def display_score(x,y):
    s = font.render("SCORE : " + str(score),True,(255,255,255))
    screen.blit(s,(x,y))

# Function for the position of bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16,y+10))


# Game loop
while running:

    # Screen background image
    screen.blit(background,(0,0))

    # Initial game screen
    if flag == -1:
        home_page()
        score = 0
        level1_flag = 0
        level2_flag = 0
        level3_flag = 0
        level4_flag = 0
        level5_flag = 0
        level = 1
        bg_temp = 0

        # Timer initializations
        start_time = pygame.time.get_ticks()
        play_time1 = 60
        play_time2 = 90
        play_time3 = 120
        play_time4 = 150
        play_time5 = 200
        game_ended = False

        # Player coordinates initially
        playerX = 370
        playerY = 480

        # for loop to handle and execute the events e.g. key press / mouse click
        for event in pygame.event.get():
            # If the player clicks the quit (X) button
            if event.type == pygame.QUIT:
                running = False
            # If the player clicks Play button
            if event.type == pygame.MOUSEBUTTONUP and play():
                flag = 0

    # Game over screen
    elif flag == 1:
        game_over()

        # Reading the High Score and updating it if necessary
        file = open('high_score.txt', 'r')
        high_score = int(file.read())
        file.close()

        if score > high_score:
            file = open('high_score.txt', 'w')
            file.write(str(score))
            file.close()

        display_score(10, 10)
        # for loop to handle and execute the events e.g. key press / mouse click
        for event in pygame.event.get():
            # If the player clicks the quit (X) button
            if event.type == pygame.QUIT:
                running = False
            # If the player clicks Play Again button
            if event.type == pygame.MOUSEBUTTONUP and play_again():
                flag = -1

    # If the player has won the game
    elif flag == 2:
        won()
        file = open('high_score.txt', 'w')
        file.write(str(50))
        file.close()
        display_score(10, 10)
        # Play background music only once
        if bg_temp == 0:
            mixer.Sound('applause.wav').play()
            bg_temp = 1

        # for loop to handle and execute the events e.g. key press / mouse click
        for event in pygame.event.get():
            # If the player clicks the quit (X) button
            if event.type == pygame.QUIT:
                running = False
            # If the player clicks Play Again button
            if event.type == pygame.MOUSEBUTTONUP and play_again():
                flag = -1

    # Game play
    else:
        # for loop to handle and execute the events e.g. key press / mouse click
        for event in pygame.event.get():

            # If the player clicks the quit (X) button
            if event.type == pygame.QUIT:
                running = False

            # Check whether a key is pressed on the keyboard
            if event.type == pygame.KEYDOWN:
                # Check which arrow key is pressed
                if event.key == pygame.K_LEFT:
                    playerX_change = -2.75
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2.75
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX,bulletY)
                        mixer.Sound('bullet_shoot.wav').play()

            # Check whether a key is released from the keyboard
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0


        # Transfer the changes according to the keyboard inputs to the X coordinate of the player
        playerX += playerX_change

        # Checking and making changes to prevent the spaceship (player) from going out of the boundaries
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # player() function call
        player(playerX,playerY)

        ###############################################################################################################

        if level == 1:

            if level1_flag == 0:
                # Set new enemies once Game over
                enemy1_image.clear()
                enemy1X.clear()
                enemy1Y.clear()
                enemy1X_change.clear()
                enemy1Y_change.clear()
                num_of_enemies1 = 10

                # for loop to put data to enemy list
                for i in range(num_of_enemies1):
                    enemy1_image.append(pygame.image.load('alien_1.png'))
                    # enemy1 coordinates initially
                    enemy1X.append(random.randint(0, 735))
                    enemy1Y.append(random.randint(50, 270))
                    # Variables to hold changes in X and Y coordinates of enemy1
                    enemy1X_change.append(1)
                    enemy1Y_change.append(45)

            # Show user that level has changed
            if level1_flag == 0:
                x_font = pygame.font.Font('college.ttf', 100)
                x1 = x_font.render("LEVEL", True, (255, 255, 255))
                x2 = x_font.render("1", True, (255, 255, 255))
                screen.blit(x1, (260, 140))
                screen.blit(x2, (375, 250))
                pygame.display.update()
                level1_flag = 1
                time.sleep(3)
                start_time = pygame.time.get_ticks()

            # Changing the position of enemies
            for i in range(num_of_enemies1):
                enemy1X[i] += enemy1X_change[i]

                # Checking for game over (whether enemy1 has reached player spaceship)
                if enemy1X[i]>=playerX-5 and enemy1X[i]<=playerX+60 and enemy1Y[i]>=playerY-60:
                    for j in range(num_of_enemies1):
                        enemy1Y[j] = 1000
                    game_over()
                    mixer.Sound('gameover_low_level.wav').play()
                    flag = 1
                    break

                # Changing enemy1 coordinates when it reaches the boundaries
                if enemy1X[i] <= 0:
                    enemy1X_change[i] = 1
                    enemy1Y[i] += enemy1Y_change[i]
                elif enemy1X[i] >= 736:
                    enemy1X_change[i] = -1
                    enemy1Y[i] += enemy1Y_change[i]

                # Collision detection of bullet and enemy
                if isCollision(bulletX, bulletY, enemy1X[i], enemy1Y[i]):
                    mixer.Sound('bullet_hit.wav').play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score += 1
                    enemy1X[i] = random.randint(0, 735)
                    enemy1Y[i] = random.randint(50, 270)

                # enemy1() function call
                enemy1(enemy1X[i],enemy1Y[i],i)

            # Check if timer's up or not
            if start_time + (play_time1 * 1000) <= pygame.time.get_ticks():
                game_over()
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1
                for j in range(num_of_enemies1):
                    enemy1Y[j] = 1000
                game_ended = True

            if not game_ended:
                # Calculating time left
                timeLeft = pygame.time.get_ticks() - start_time
                timeLeft = timeLeft / 1000
                timeLeft = play_time1 - timeLeft
                timeLeft = int(timeLeft)
                # Function to display time remaining
                time_left(timeLeft)

        ###############################################################################################################

        elif level == 2:

            if level2_flag == 0:
                # Set new enemies once game over
                enemy2_image.clear()
                enemy2X.clear()
                enemy2Y.clear()
                enemy2X_change.clear()
                enemy2Y_change.clear()
                num_of_enemies2 = 25

                # for loop to put data to enemy list
                for i in range(num_of_enemies2):
                    enemy2_image.append(pygame.image.load('alien_2.png'))
                    # enemy2 coordinates initially
                    enemy2X.append(random.randint(0, 735))
                    enemy2Y.append(random.randint(50, 270))
                    # Variables to hold changes in X and Y coordinates of enemy2
                    enemy2X_change.append(1.90)
                    enemy2Y_change.append(45)

            # Show user that level has changed
            if level2_flag == 0:
                x_font = pygame.font.Font('college.ttf', 100)
                x1 = x_font.render("LEVEL", True, (255, 255, 255))
                x2 = x_font.render("2", True, (255, 255, 255))
                screen.blit(x1, (260, 140))
                screen.blit(x2, (375, 250))
                pygame.display.update()
                level2_flag = 1
                time.sleep(3)
                start_time = pygame.time.get_ticks()

            # Changing the position of enemies
            for i in range(num_of_enemies2):
                enemy2X[i] += enemy2X_change[i]

                # Checking for game over (whether enemy2 has reached player spaceship)
                if enemy2X[i]>=playerX-5 and enemy2X[i]<=playerX+60 and enemy2Y[i]>=playerY-60:
                    for j in range(num_of_enemies2):
                        enemy2Y[j] = 1000
                    game_over()
                    level = 1
                    mixer.Sound('gameover_low_level.wav').play()
                    flag = 1
                    break

                # Changing enemy2 coordinates when it reaches the boundaries
                if enemy2X[i] <= 0:
                    enemy2X_change[i] = 1.90
                    enemy2Y[i] += enemy2Y_change[i]
                elif enemy2X[i] >= 736:
                    enemy2X_change[i] = -1.90
                    enemy2Y[i] += enemy2Y_change[i]

                # Collision detection of bullet and enemy
                if isCollision(bulletX, bulletY, enemy2X[i], enemy2Y[i]):
                    mixer.Sound('bullet_hit.wav').play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score += 1
                    enemy2X[i] = random.randint(0, 735)
                    enemy2Y[i] = random.randint(50, 250)

                # enemy2() function call
                enemy2(enemy2X[i],enemy2Y[i],i)

            # Check if timer's up or not
            if start_time + (play_time2 * 1000) <= pygame.time.get_ticks():
                game_over()
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 1000
                game_ended = True

            if not game_ended:
                # Calculating time left
                timeLeft = pygame.time.get_ticks() - start_time
                timeLeft = timeLeft / 1000
                timeLeft = play_time2 - timeLeft
                timeLeft = int(timeLeft)
                # Function to display time remaining
                time_left(timeLeft)

        ###############################################################################################################

        elif level == 3:

            if level3_flag == 0:
                # Set new enemies once game over
                enemy3_image.clear()
                enemy3X.clear()
                enemy3Y.clear()
                enemy3X_change.clear()
                enemy3Y_change.clear()
                num_of_enemies3 = 20

                # for loop to put data to enemy list
                for i in range(num_of_enemies3):
                    enemy3_image.append(pygame.image.load('alien_3.png'))
                    # enemy3 coordinates initially
                    enemy3X.append(random.randint(0, 735))
                    enemy3Y.append(random.randint(50, 250))
                    # Variables to hold changes in X and Y coordinates of enemy3
                    enemy3X_change.append(1)
                    enemy3Y_change.append(45)

            # Show user that level has changed
            if level3_flag == 0:
                x_font = pygame.font.Font('college.ttf', 100)
                x1 = x_font.render("LEVEL", True, (255, 255, 255))
                x2 = x_font.render("3", True, (255, 255, 255))
                screen.blit(x1, (260, 140))
                screen.blit(x2, (375, 250))
                pygame.display.update()
                level3_flag = 1
                time.sleep(3)
                start_time = pygame.time.get_ticks()

            # Shooting bullet from enemy
            enemy_bulletY_change = 3
            if h%250 == 0:
                p = random.randint(1,19)
                enemy_bulletX = enemy3X[p] + 17
                enemy_bulletY = enemy3Y[p] + 20
            if enemy_bulletY <= 600:
                enemy_bulletY += enemy_bulletY_change
                screen.blit(enemy_bullet_image, (enemy_bulletX, enemy_bulletY))
            else:
                enemy_bulletY = 1000
            h += 1

            # Check whether enemy bullet has hit the player or not
            if isCollision(enemy_bulletX,enemy_bulletY,playerX,playerY):
                game_over()
                level = 1
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1

            # Changing the position of enemies
            for i in range(num_of_enemies3):
                enemy3X[i] += enemy3X_change[i]

                # Checking for game over (whether enemy3 has reached player spaceship)
                if enemy3X[i]>=playerX-5 and enemy3X[i]<=playerX+60 and enemy3Y[i]>=playerY-60:
                    for j in range(num_of_enemies3):
                        enemy3Y[j] = 1000
                    game_over()
                    level = 1
                    mixer.Sound('gameover_low_level.wav').play()
                    flag = 1
                    break

                # Changing enemy3 coordinates when it reaches the boundaries
                if enemy3X[i] <= 0:
                    enemy3X_change[i] = 1
                    enemy3Y[i] += enemy3Y_change[i]
                elif enemy3X[i] >= 736:
                    enemy3X_change[i] = -1
                    enemy3Y[i] += enemy3Y_change[i]

                # Collision detection of bullet and enemy
                if isCollision(bulletX, bulletY, enemy3X[i], enemy3Y[i]):
                    mixer.Sound('bullet_hit.wav').play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score += 1
                    enemy3X[i] = random.randint(0, 735)
                    enemy3Y[i] = random.randint(50, 250)

                # enemy3() function call
                enemy3(enemy3X[i],enemy3Y[i],i)

            # Check if timer's up or not
            if start_time + (play_time3 * 1000) <= pygame.time.get_ticks():
                game_over()
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 1000
                game_ended = True

            if not game_ended:
                # Calculating time left
                timeLeft = pygame.time.get_ticks() - start_time
                timeLeft = timeLeft / 1000
                timeLeft = play_time3 - timeLeft
                timeLeft = int(timeLeft)
                # Function to display time remaining
                time_left(timeLeft)

        ###############################################################################################################

        elif level == 4:

            if level4_flag == 0:
                # Set new enemies once game over
                enemy4_image.clear()
                enemy4X.clear()
                enemy4Y.clear()
                enemy4X_change.clear()
                enemy4Y_change.clear()
                num_of_enemies4 = 27

                # for loop to put data to enemy list
                for i in range(num_of_enemies4):
                    enemy4_image.append(pygame.image.load('alien_4.png'))
                    # enemy4 coordinates initially
                    enemy4X.append(random.randint(0, 735))
                    enemy4Y.append(random.randint(50, 250))
                    # Variables to hold changes in X and Y coordinates of enemy4
                    enemy4X_change.append(1.75)
                    enemy4Y_change.append(50)

            # Show user that level has changed
            if level4_flag == 0:
                x_font = pygame.font.Font('college.ttf', 100)
                x1 = x_font.render("LEVEL", True, (255, 255, 255))
                x2 = x_font.render("4", True, (255, 255, 255))
                screen.blit(x1, (260, 140))
                screen.blit(x2, (375, 250))
                pygame.display.update()
                level4_flag = 1
                time.sleep(3)
                start_time = pygame.time.get_ticks()

            # Shooting bullet from enemy
            enemy_bulletY_change = 4
            if h%125 == 0:
                p = random.randint(1,19)
                enemy_bulletX = enemy4X[p] + 17
                enemy_bulletY = enemy4Y[p] + 20
            if enemy_bulletY <= 600:
                enemy_bulletY += enemy_bulletY_change
                screen.blit(enemy_bullet_image, (enemy_bulletX, enemy_bulletY))
            else:
                enemy_bulletY = 1000
            h += 1

            # Check whether enemy bullet has hit the player or not
            if isCollision(enemy_bulletX,enemy_bulletY,playerX,playerY):
                game_over()
                level = 1
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1

            # Changing the position of enemies
            for i in range(num_of_enemies4):
                enemy4X[i] += enemy4X_change[i]

                # Checking for game over (whether enemy4 has reached player spaceship)
                if enemy4X[i]>=playerX-5 and enemy4X[i]<=playerX+60 and enemy4Y[i]>=playerY-60:
                    for j in range(num_of_enemies4):
                        enemy4Y[j] = 1000
                    game_over()
                    level = 1
                    mixer.Sound('gameover_low_level.wav').play()
                    flag = 1
                    break

                # Changing enemy4 coordinates when it reaches the boundaries
                if enemy4X[i] <= 0:
                    enemy4X_change[i] = 1.75
                    enemy4Y[i] += enemy4Y_change[i]
                elif enemy4X[i] >= 736:
                    enemy4X_change[i] = -1.75
                    enemy4Y[i] += enemy4Y_change[i]

                # Collision detection of bullet and enemy
                if isCollision(bulletX, bulletY, enemy4X[i], enemy4Y[i]):
                    mixer.Sound('bullet_hit.wav').play()
                    bulletY = playerY
                    bullet_state = "ready"
                    score += 1
                    enemy4X[i] = random.randint(0, 735)
                    enemy4Y[i] = random.randint(50, 250)

                # enemy4() function call
                enemy4(enemy4X[i],enemy4Y[i],i)

            # Check if timer's up or not
            if start_time + (play_time4 * 1000) <= pygame.time.get_ticks():
                game_over()
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 1000
                game_ended = True

            if not game_ended:
                # Calculating time left
                timeLeft = pygame.time.get_ticks() - start_time
                timeLeft = timeLeft / 1000
                timeLeft = play_time4 - timeLeft
                timeLeft = int(timeLeft)
                # Function to display time remaining
                time_left(timeLeft)

        ###############################################################################################################

        elif level == 5:

            if level5_flag == 0:
                enemy5_image = pygame.image.load('alien_5.png')
                # enemy5 coordinates initially
                enemy5X = random.randint(3, 670)
                enemy5Y = random.randint(10, 150)
                # Variables to hold changes in X and Y coordinates of enemy5
                enemy5X_change = 2.5
                enemy5Y_change = 2.5

            # Show user that level has changed
            if level5_flag == 0:
                x_font = pygame.font.Font('college.ttf', 100)
                x1 = x_font.render("LEVEL", True, (255, 255, 255))
                x2 = x_font.render("5", True, (255, 255, 255))
                screen.blit(x1, (260, 140))
                screen.blit(x2, (375, 250))
                pygame.display.update()
                level5_flag = 1
                time.sleep(3)
                start_time = pygame.time.get_ticks()

            # Shooting bullet from enemy
            enemy_bulletY_change = 5
            if h%100 == 0:
                enemy_bulletX = enemy5X + 17
                enemy_bulletY = enemy5Y + 20
            if enemy_bulletY <= 600:
                enemy_bulletY += enemy_bulletY_change
                screen.blit(enemy_bullet_image, (enemy_bulletX, enemy_bulletY))
            else:
                enemy_bulletY = 1000
            h += 1

            # Check whether enemy bullet has hit the player or not
            if isCollision(enemy_bulletX,enemy_bulletY,playerX,playerY):
                game_over()
                level = 1
                mixer.Sound('gameover_high_level.wav').play()
                flag = 1

            # Changing the position of enemy5
            if r%250 == 0:
                enemy5X = random.randint(3,670)
                enemy5Y = random.randint(10,300)
            r += 1

            enemy5X += enemy5X_change

            # Changing enemy5 coordinates when it reaches the boundaries
            if enemy5X <= 0:
                enemy5X_change = 2.5
                enemy5Y += enemy5Y_change
            elif enemy5X >= 680:
                enemy5X_change = -2.5
                enemy5Y += enemy5Y_change

            # Collision detection of bullet and enemy
            if isCollision5(bulletX, bulletY, enemy5X, enemy5Y):
                mixer.Sound('bullet_hit.wav').play()
                bulletY = playerY
                bullet_state = "ready"
                score += 1
                enemy5X = random.randint(3, 670)
                enemy5Y = random.randint(10, 300)

            # enemy5() function call
            enemy5(enemy5X, enemy5Y)

            # Check if timer's up or not
            if start_time + (play_time5 * 1000) <= pygame.time.get_ticks():
                game_over()
                mixer.Sound('gameover_low_level.wav').play()
                flag = 1
                enemy5Y = 1000
                game_ended = True

            if not game_ended:
                # Calculating time left
                timeLeft = pygame.time.get_ticks() - start_time
                timeLeft = timeLeft / 1000
                timeLeft = play_time5 - timeLeft
                timeLeft = int(timeLeft)
                # Function to display time remaining
                time_left(timeLeft)

        ###############################################################################################################

        # Bullet movement
        if bulletY <= 50:
            bulletY = playerY
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -= bulletY_change

        # Changing level depending upon the score
        display_score(10,10)
        if score == 10 and level == 1:
            level = 2
        if score == 20 and level == 2:
            level = 3
        if score == 30 and level == 3:
            level = 4
        if score == 40 and level == 4:
            level = 5
        if score == 50 and level == 5:
            flag = 2

    # Update the display after every change
    pygame.display.update()
