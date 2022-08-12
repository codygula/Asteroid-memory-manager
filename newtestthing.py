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
        self.direction = "left"
        
    def display(self):    
        screen.blit((Asteroid.asteroidImg), (self.asteroidX, self.asteroidY))
    
    def move(self):
        pass



running = True
ax = 100

startX = random.randint(5,790)
startY = random.randint(5, 590)

def create():
        ax = random.randint(5,790)
        ay = random.randint(5, 590)
        asteroids.append(Asteroid(ax,ay))

list1 = ["item1", "item2", "item3", "item4"]
asteroids = []
for i in list1:
    i = create()


    


while running:

    # Background color
    screen.fill((255,0,0))
    

    
    for i in asteroids:
        
        if i.asteroidX < 0:
            i.direction = "right"
        elif i.asteroidX > 300:
            i.direction = "left"
        
        xchange = 1
        if i.direction == "right":
            xchange = 1
            i.asteroidX += xchange
            i.display()
            print(i.asteroidX)

        if i.direction == "left":
            xchange = -1
            i.asteroidX += xchange
            i.display()
            print(i.asteroidX)

   
        
        Asteroid.display(i)



    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


    
    pygame.display.update()