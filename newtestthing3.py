import pygame
import random
import math
import psutil
import subprocess
import os

pygame.init()

testMode = True

screenX = 800
screenY = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

score = 0

screen = pygame.display.set_mode((screenX,screenY))
clock = pygame.time.Clock()

# Display score and high score
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.


    


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

def destroyed(name, size):
    global score
    score = score + size
    print("killall ", name, size)
    if testMode == False:
        subprocess.run(f"killall -q -I {name}", shell=True)
        print(f"killall -q -I {name}")
    elif testMode == True:
        print(f"TEST MODE killall {name}")



class Asteroid():
    asteroidImg = pygame.image.load("asteroid.png")
    def __init__(self, asteroidX, asteroidY, name, size, memory):
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY
        self.direction = "left"
        self.Ydirection = "up"
        self.randomNumber = round((random.randint(1,10)/50), 2)
        self.name = name
        self.speed = "speed here"
        self.size = size
        self.memory = memory
        font = pygame.font.SysFont(None, 16)
        self.img = font.render(self.name, True, white) 

        
    def display(self):  
        # image = pygame.transform.scale(Asteroid.asteroidImg, self.size)
        try:
            image = pygame.transform.scale(Asteroid.asteroidImg, self.size)  
            print(self.size)
        except:
            image = pygame.transform.scale(Asteroid.asteroidImg, (25,25))
            print("error", self.size)
        screen.blit(image, (self.asteroidX, self.asteroidY))
        screen.blit(self.img, (self.asteroidX, self.asteroidY))

class Explosion():
    def __init__(self,explosionX,explosionY):
        self.explosionX = explosionX
        self.explosionY = explosionY
        self.images = []
        self.images.append(pygame.image.load('explosions/regularExplosion00.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion01.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion02.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion03.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion04.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion05.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion06.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion07.png'))
        self.images.append(pygame.image.load('explosions/regularExplosion08.png'))
 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(5, 5, 150, 198)
 
    def update(self): #, explosionX, explosionY):
        i = 0
        while i <= len(self.images):
            screen.blit(self.image, (self.explosionX, self.explosionY))
            print("EXPLOSION!")
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            i += 1
        # screen.blit(self.image, (self.explosionX, self.explosionY))
        # print("EXPLOSION!")


########################################
# setup asteroids with current running processe

def getListOfProcessSortedByMemory():
    '''this function returns a list of dictionaries containing the name and memory usage.
    It is sorted largest to smallest. It deduplicates the items on the list, but it does not 
    yet combine total memory sizes. It just returns the memory usage of the first instance of
    an item on a list.'''
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
    bigdict = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    duplicates = []
    newNames = []
    i = 0
    while i <= len(bigdict)-1:
    
        if bigdict[i]['name'] in duplicates:
            #newNames.append({'name':bigdict[i]['name'], 'size':0})
            combinedSize = bigdict[i]['vms'] #newNames[i]['size'] #+ bigdict[i]['vms']
            #newNames.append({'name':bigdict[i]['name'], 'size':combinedSize}) # Update here
            print("!!!!!!!!!!!!!!!!!! DUPLICATE")

        elif bigdict[i]['name'] not in duplicates:
            duplicates.append(bigdict[i]['name'])
            combinedSize = bigdict[i]['vms']
            newNames.append({'name':bigdict[i]['name'], 'size':combinedSize})
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ORIGIONAL")
    
        i += 1
    return newNames





startX = random.randint(5,790)
startY = random.randint(5, 590)
asteroidNames = []
asteroidSizes = []
asteroids = [] # The list used in the main loop
numberOfAsteroids = 20
preadjustedSizes = []

def create(name, size, memory):
        ax = random.randint(5,790)
        ay = random.randint(5, 590)
        asteroids.append(Asteroid(ax,ay, name, size, memory))

def processSize(vms):
    return vms / screenX


listOfRunningProcess = getListOfProcessSortedByMemory()

for i in listOfRunningProcess[:numberOfAsteroids]:
    
    preadjustedSizes.append(processSize(i['size']))
    asteroidNames.append(i['name'])

# Thing to determine size of asteroids. This needs work
for i in preadjustedSizes:
    j = abs(math.log2(i) *  screenX /100) #/ difference
    
    asteroidSizes.append([j,j])


i = 0
while i <= len(asteroidNames)-1:
    create(asteroidNames[i], asteroidSizes[i], preadjustedSizes[i])
    i += 1









# Main loop
running = True
while running:
    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()
    

    # Background color
    screen.fill((0,0,0))
    changes = [1 , 3]
    negChanges = [-1 , -2]

    # Display score
    my_font = pygame.font.SysFont('Courier', 30)
    text_surface = my_font.render(f'SCORE: {score}', False, white)
    screen.blit(text_surface, (0,0))
    

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
            explode = Explosion(i.asteroidX, i.asteroidY)
            explode.update()
           

            asteroids.remove(i)
            
            destroyed(i.name, i.memory)
            print("SIZE", i.memory)
            print(type(i.size))
            print("score = ", score)



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
            
        if i.direction == "left":
            xchange = random.choice(negChanges)
            i.asteroidX += xchange 
            i.display()
            
        
        if i.Ydirection == "up":
            ychange = random.choice(changes)
            i.asteroidY += ychange
            i.display()
           

        if i.Ydirection == "down":
            ychange = random.choice(negChanges)
            i.asteroidY += ychange 
            i.display()
            
      
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
    
    fpsClock.tick(FPS)
    player(playerX, playerY)
    pygame.display.update()