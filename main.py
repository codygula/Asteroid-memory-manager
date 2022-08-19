import pygame
import random
import math
import psutil
import subprocess
import os

pygame.init()
pygame.display.set_caption('Linux Memory Use Utility')

# TODO  1. Fix explosion sequence.
#       2. Create new black and white assets (ship and explosions)
#       3. Add high score create/read from log file.
#       4. Add gradually fading text saying "killall " + name to explosion
#       5. Fix asteroid size issue
#       6. 
#       7. Make deduplicating function add up total memory use instead of just first item memory use.

# Changing this to False will cause it to killall in real life. True just prints to screen.
testMode = True

screenX = 800
screenY = 600

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

score = 0
my_font = pygame.font.SysFont('Courier', 30)

highScore = my_font.render(f'HIGH SCORE: {score}', False, white)

def getHighScore():
    # function to retrieve high score.
    pass






screen = pygame.display.set_mode((screenX,screenY))
clock = pygame.time.Clock()

# Display score and high score
pygame.font.init() 

playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

# Missle
missleImg = pygame.image.load("square.png")
missleX = 0
missleY = 480
missleX_change = 0.5
missleY_change = 40
missle_state = "ready"

def player(x,y):
    screen.blit(playerImg, (x,y))

def fire_missle(x,y):
    global missle_state
    missle_state = "fire"
    screen.blit(missleImg,(x + 30 , y + 10))

def isCollision(enemyX, enemyY, missleX, missleY):
    distance = math.sqrt(math.pow(enemyX - missleX , 2) + math.pow(enemyY - missleY , 2))
    if distance < 27 and missle_state == "fire":
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
        print(f"TEST MODE:~$ killall -q -I {name}")

class Asteroid():
    asteroidImg = pygame.image.load("asteroid.png")
    def __init__(self, asteroidX, asteroidY, name, size, memory):
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY
        self.direction = "left"
        self.Ydirection = "up"
        self.name = name
        self.speed = "speed here"
        self.size = size
        self.memory = memory
        font = pygame.font.SysFont(None, 16)
        self.img = font.render(self.name, True, white) 
        changes = [-0.4, -0.5, -1 , -1.9, -2.9]
        self.xchange = random.choice(changes)
        self.ychange = random.choice(changes) 
        
    def display(self):  
        try:
            image = pygame.transform.scale(Asteroid.asteroidImg, self.size)  
            
        except:
            image = pygame.transform.scale(Asteroid.asteroidImg, (25,25))
            print("error", self.name, self.size)
        screen.blit(image, (self.asteroidX, self.asteroidY))
        screen.blit(self.img, (self.asteroidX + self.size[0], self.asteroidY+ (self.size[1]/10)))

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
 
    def update(self): 
        i = 0
        while i <= len(self.images):
            screen.blit(self.image, (self.explosionX - 35, self.explosionY - 35))
            print("EXPLOSION!")
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            i += 1
        


########################################
# setup asteroids with current running processe

def getListOfProcessSortedByMemory():
    '''this function returns a list of dictionaries containing the name and memory usage.
    It is sorted largest to smallest. It deduplicates the items on the list, but it does not 
    yet combine total memory sizes. It just returns the memory usage of the first instance of
    an item on a list.'''
    # Get list of running processes by memory
    listOfProcObjects = []
    
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
            #print("!!!!!!!!!!!!!!!!!! DUPLICATE")

        elif bigdict[i]['name'] not in duplicates:
            duplicates.append(bigdict[i]['name'])
            combinedSize = bigdict[i]['vms']
            newNames.append({'name':bigdict[i]['name'], 'size':combinedSize})
            #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ORIGIONAL")
    
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
   
    # Display score
    text_surface = my_font.render(f'SCORE: {score}', False, white)
    screen.blit(text_surface, (0,0))
    
    #display high score
    screen.blit(highScore, (0,30))
    
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
                if missle_state is "ready":
                    missleX = playerX
                    fire_missle(playerX, missleY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    for i in asteroids:
        
        if isCollision(i.asteroidX, i.asteroidY, missleX, missleY) == True:
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
        elif i.asteroidY > 435:
            i.Ydirection = "down"
        
        
        if i.direction == "right":
            i.asteroidX += abs(i.xchange)
            i.display()
            
        if i.direction == "left":
            i.asteroidX += i.xchange 
            i.display()
            
        
        if i.Ydirection == "up":
            i.asteroidY += abs(i.ychange)
            i.display()
           

        if i.Ydirection == "down":
            i.asteroidY += i.ychange 
            i.display()
            
      
        Asteroid.display(i)

    # Boundary
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # missle movement
    if missleY <= 0:
        missleY = 480
        missle_state = "ready"

    if missle_state is "fire":
        fire_missle(missleX, missleY)
        missleY -= missleY_change
    
    fpsClock.tick(FPS)
    player(playerX, playerY)
    pygame.display.update()