import pygame
import random
import math


pygame.init()

screen = pygame.display.set_mode((800,600))

class Asteroid():
    asteroidImg = pygame.image.load("asteroid.png")
    def __init__(self, asteroidX, asteroidY, name):
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY
        self.direction = "left"
        self.Ydirection = "up"
        self.randomNumber = round((random.randint(1,10)/50), 2)
        self.name = name
        self.speed = "speed here"
        self.size = "size here"

        
    def display(self):    
        screen.blit((Asteroid.asteroidImg), (self.asteroidX, self.asteroidY))
        #self.name = name
    
    def move(self):
        pass



running = True
ax = 100

startX = random.randint(5,790)
startY = random.randint(5, 590)

def create(name):
        ax = random.randint(5,790)
        ay = random.randint(5, 590)
        asteroids.append(Asteroid(ax,ay, name))

list1 = ["item1", "item2", "item3", "item4","item1", "item2", "item3", "item4"]
asteroids = []
for i in list1:
    i = create(i)


    


while running:

    # Background color
    screen.fill((255,0,0))
    changes = [1.1 , 1.3, 1.5]
    negChanges = [-1.35 , -1.55, -1.7]

    
    for i in asteroids:
        
        if i.asteroidX < 0:
            i.direction = "right"
        elif i.asteroidX > 800:
            i.direction = "left"

        if i.asteroidY < 0:
            i.Ydirection = "up"
        elif i.asteroidY > 500:
            i.Ydirection = "down"
        
        
        if i.direction == "right":
            xchange = random.choice(changes)
            i.asteroidX += xchange
            i.display()
            print(i.asteroidX)

        if i.direction == "left":
            xchange = random.choice(negChanges)
            i.asteroidX += xchange 
            i.display()
            print(i.asteroidX)
        
        if i.Ydirection == "up":
            ychange = random.choice(changes)
            i.asteroidY += ychange
            i.display()
            print(i.asteroidX)

        if i.Ydirection == "down":
            ychange = random.choice(negChanges)
            i.asteroidY += ychange 
            i.display()
            print(i.asteroidX)

   
        
        Asteroid.display(i)



    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


    
    pygame.display.update()