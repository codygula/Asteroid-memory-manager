import pygame
import random
import math
import psutil
import os

pygame.init()
screenX = 800
screenY = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

screen = pygame.display.set_mode((screenX,screenY))
clock = pygame.time.Clock()


playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Bullet
bulletImg = pygame.image.load("circle.png")
bulletX = 0
bulletY = 480
bulletX_change = 0.5
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImg, (x,y))



def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16 , y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX , 2) + math.pow(enemyY - bulletY , 2))
    if distance < 27 and bullet_state == "fire":
        return True
    else:
        return False

class Asteroid():
    asteroidImg = pygame.image.load("asteroid.png")
    def __init__(self, asteroidX, asteroidY, name, size):
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY
        self.direction = "left"
        self.Ydirection = "up"
        self.randomNumber = round((random.randint(1,10)/50), 2)
        self.name = name
        self.speed = "speed here"
        self.size = size
        font = pygame.font.SysFont(None, 16)
        self.img = font.render(self.name, True, blue) 


        
    def display(self):  
        image = pygame.transform.scale(Asteroid.asteroidImg, self.size)  
        screen.blit(image, (self.asteroidX, self.asteroidY))
        screen.blit(self.img, (self.asteroidX, self.asteroidY))
    
    def move(self):
        pass


explosion = [pygame.image.load('numbers/one.png'), pygame.image.load('numbers/two.png'), pygame.image.load('numbers/three.png'), pygame.image.load('numbers/four.png'), pygame.image.load('numbers/five.png'), pygame.image.load('numbers/six.png')]

#running = True
#ax = 100

startX = random.randint(5,790)
startY = random.randint(5, 590)

def create(name, size):
        ax = random.randint(5,790)
        ay = random.randint(5, 590)
        asteroids.append(Asteroid(ax,ay, name, size))

########################################
# setup asteroids with current running processes

list1 = []
sizes = []
speed = []
asteroids = []



def getListOfProcessSortedByMemory():
    #Get list of running processes by memory
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects


def processSize(vms):
    return vms / screenX

## Code to create lists of runniung proccesses, thier sizes, and PIDs
listOfRunningProcess = getListOfProcessSortedByMemory()
adjustedSizes = []
#sizes = []
numberOfAsteroids = 20
for elem in listOfRunningProcess[:numberOfAsteroids]:
    print(elem['name'])
    
    #print(elem['pid'])
    adjustedSizes.append(processSize(elem['vms']))
    list1.append(elem['name'])

difference = max(adjustedSizes) - min(adjustedSizes)
print(difference)

# Thing to determine size of asteroids. This needs work
for i in adjustedSizes:
    j = math.log2(i) *  screenX /100#/ difference
    
    sizes.append([j,j])
print(sizes)
print(adjustedSizes)

i = 0
while i <= len(list1)-1:
    create(list1[i], sizes[i])
    i += 1


# Main loop
running = True
while running:
    clock.tick(30)

    # Background color
    screen.fill((255,0,0))
    changes = [1 , 3]
    negChanges = [-1 , -2]

    # keystroke control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    for i in asteroids:
        
        if isCollision(i.asteroidX, i.asteroidY, bulletX, bulletY) == True:
            print("Collision", i.name)

            # slowed mode explode code
            j=0
            while j <= len(explosion)-1:
                screen.blit(explosion[j], (i.asteroidX, i.asteroidY))
                j += 1
            asteroids.remove(i)

        if i.asteroidX < 0:
            i.direction = "right"
        elif i.asteroidX > 675:
            i.direction = "left"

        if i.asteroidY < 0:
            i.Ydirection = "up"
        elif i.asteroidY > 475:
            i.Ydirection = "down"
        
        
        if i.direction == "right":
            xchange = random.choice(changes)
            i.asteroidX += xchange
            i.display()
            #print(i.asteroidX)

        if i.direction == "left":
            xchange = random.choice(negChanges)
            i.asteroidX += xchange 
            i.display()
            #print(i.asteroidX)
        
        if i.Ydirection == "up":
            ychange = random.choice(changes)
            i.asteroidY += ychange
            i.display()
            #print(i.asteroidX)

        if i.Ydirection == "down":
            ychange = random.choice(negChanges)
            i.asteroidY += ychange 
            i.display()
            #print(i.asteroidX)

   
      
        Asteroid.display(i)

    # Boundary
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    
    player(playerX, playerY)
    pygame.display.update()