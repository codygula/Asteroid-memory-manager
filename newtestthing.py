import pygame
import random
import math
import psutil
import os

pygame.init()

screen = pygame.display.set_mode((800,600))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)



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



#######
# https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
explosion_anim = []

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(os.path.join("explosions", filename)).convert()
    #img = pygame.image.load("explosions".join("explosions")).convert()
    img.set_colorkey(black)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim.append(img_lg)

def explode(x,y):
    # for i in range(9):
    #     filename = 'regularExplosion0{}.png'.format(i)
    #     img = pygame.image.load(os.path.join("explosions", filename)).convert()
    #     img.set_colorkey(black)
    #     img_lg = pygame.transform.scale(img, (75, 75))
    #     explosion_anim.append(img_lg)
    screen.blit(explosion_anim[0], x, y)

    

class Explosion(pygame.sprite.Sprite):
    def __init__(self): #, center, size):
        pygame.sprite.Sprite.__init__(self)
        #self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        #self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
#########
running = True
ax = 100

startX = random.randint(5,790)
startY = random.randint(5, 590)

def create(name, size):
        ax = random.randint(5,790)
        ay = random.randint(5, 590)
        asteroids.append(Asteroid(ax,ay, name, size))

list1 = ["item1", "item2", "item3", "item4","item1", "item2", "item3", "item4"]
sizes = [(64,64),(64,64),(64,64),(64,64),(64,64),(64,64),(32,32),(32,32)]
speed = []
asteroids = []
#for i in list1:
i = 0
while i <= len(list1)-1:
    create(list1[i], sizes[i])
    i += 1



while running:

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
        # isCollision(enemyX, enemyY, bulletX, bulletY)
        if isCollision(i.asteroidX, i.asteroidY, bulletX, bulletY) == True:
            print("Collision", i.name)
            explode(i.asteroidX, i.asteroidY)
            #expl = Explosion # (hit.rect.center, 'lg')
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