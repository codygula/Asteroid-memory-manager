import pygame
import random


pygame.init()

screen = pygame.display.set_mode((800,600))


# Window title and icon
pygame.display.set_caption("Memory Manager")
# icon = pygame.image.load("imageName.png")
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("asteroid.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40



def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))



running = True

while running:

    # Background color
    screen.fill((255,0,0))



    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # keystroke control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
         
    # Boundary
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.5
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


# https://www.youtube.com/watch?v=FfWpgLFMI7w   12:39