import pygame

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
enemyX = 370
enemyY = 480
enemyX_change = 0



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
         
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


# https://www.youtube.com/watch?v=FfWpgLFMI7w   12:39