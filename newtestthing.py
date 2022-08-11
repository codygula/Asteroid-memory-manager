import pygame
import random
import math


pygame.init()

screen = pygame.display.set_mode((800,600))

class Asteroid():
    asteroidImg = pygame.image.load("asteroid.png")
    def __init__(self, asteroidX, asteroidY):
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY
        self.asteroidChangeX = 1
        self.asteroidChangeY = 1

    
    def create(asteroidX, asteroidY):
        asteroidX = asteroidX
        asteroidY = asteroidY
        screen.blit(pygame.image.load("asteroid.png"), (asteroidX, asteroidY))




running = True

while running:

    # Background color
    screen.fill((255,0,0))


    asteroid = Asteroid.create(100,100)
    asteroid.asteroidX += asteroid.asteroidChangeX

    # if enemyX <= 0:
    #     enemyX_change = 0.3
    #     enemyY += enemyY_change
    # elif enemyX >= 736:
    #     enemyX_change = -0.5
    #     enemyY += enemyY_change

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


    
    pygame.display.update()