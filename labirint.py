from pygame import *
from time import sleep

#Main
windowwidth = 1920
windowheight = 1030
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
windows = display.set_mode((windowwidth, windowheight))
clock = time.Clock()
bg = transform.scale(image.load('bg.jpg'), (windowwidth, windowheight))

display.set_caption('MazeGame')

class GamesSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, pic):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(pic), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GamesSprite):
    def __init__(self, x, y, width, height, pic, xspd):
        super().__init__(x, y, width, height, pic)
        self.xspd = xspd
    def update(self):
        self.rect.x += self.xspd
        if self.rect.x >= windowwidth:
            self.kill()

class Player(GamesSprite):
    def __init__(self, x, y, width, height, pic, xspd, yspd):
        super().__init__(x, y, width, height, pic)
        self.xspd = xspd
        self.yspd = yspd
    def movement(self):
        if char.rect.x < windowwidth-75 and char.xspd > 0 or char.rect.x > 0 and char.xspd < 0:
            self.rect.x += self.xspd
            platformpatch = sprite.spritecollide(self, wallgroup, False)
            if self.xspd > 0:
                for p in platformpatch:
                    self.rect.right = min(self.rect.right, p.rect.left)
            else:
                for p in platformpatch:
                    self.rect.left = max(self.rect.left, p.rect.right)
        if char.rect.y < windowheight-250 and char.yspd > 0 or char.rect.y > 0 and char.yspd < 0:
            self.rect.y += self.yspd
            platformpatch = sprite.spritecollide(self, wallgroup, False)
            if self.yspd < 0:
                for p in platformpatch:
                    self.rect.top = max(self.rect.top, p.rect.bottom)
            else:
                for p in platformpatch:
                    self.rect.bottom = min(self.rect.bottom, p.rect.top)
    def fire(self):
        bullet = Bullet(self.rect.right, self.rect.centery, 45, 15, 'arrow.png', 20)
        bullets.add(bullet)

class Enemy(GamesSprite):
    direction = 'down'
    def __init__(self, x, y, width, height, pic, yspd):
        super().__init__(x, y, width, height, pic)
        self.yspd = yspd
        self.cooldown = 20
    def movement(self):
        if self.rect.y >= 800:
            self.direction = 'up'
        elif self.rect.y <= 215:
            self.direction = 'down'
        if self.direction == 'up':
            self.rect.y -= self.yspd
        else:
            self.rect.y += self.yspd
    def fire(self):
        bullet = Bullet(self.rect.right, self.rect.centery, 45, 15, 'arrow.png', 10)
        enemybullets.add(bullet)


#Characters
char = Player(100, 515, 75, 250, 'steve right.png', 0, 0)

bullets = sprite.Group()
enemybullets = sprite.Group()

enemy1 = Enemy(800, 515, 225, 175, 'Enemy1.png', 0)
enemy2 = Enemy(1200, 215, 225, 175, 'Enemy1.png', 5)
wallgroup = sprite.Group()
enemygroup = sprite.Group()
enemygroup.add(enemy1)
enemygroup.add(enemy2)

#Walls
walls1 = []
walls1a = 3
walls2 = []
walls2a = 3
walls3 = []
walls3a = 3
walls4 = []
walls4a = 3
walls5 = []
walls5a = 3
walls6 = []
walls6a = 3

wallsx = 500
wallsx2 = 700
wallsx3 = 700
wallsx4 = 700
wallsx5 = 1100
wallsx6 = 1000

wallsy = 200
wallsy2 = 600
wallsy3 = 30
wallsy4 = 400
wallsy5 = 100
wallsy6 = 700

#Finish
finishsprite = GamesSprite(1500, 500, 100, 100, 'Diamond.png')

for i in range(walls1a):
    wall = GamesSprite(wallsx, wallsy, 100, 100, 'Wall.png')
    walls1.append(wall)
    wallsy += 100
    wallgroup.add(wall)

for i in range(walls2a):
    wall = GamesSprite(wallsx2, wallsy2, 100, 100, 'Wall.png')
    walls2.append(wall)
    wallsy2 -= 100
    wallgroup.add(wall)

for i in range(walls3a):
    wall = GamesSprite(wallsx3, wallsy3, 100, 100, 'Wall.png')
    walls3.append(wall)
    wallsx3 += 100
    wallgroup.add(wall)

for i in range(walls4a):
    wall = GamesSprite(wallsx4, wallsy4, 100, 100, 'Wall.png')
    walls4.append(wall)
    wallsx4 += 100
    wallgroup.add(wall)

for i in range(walls5a):
    wall = GamesSprite(wallsx5, wallsy5, 100, 100, 'Wall.png')
    walls5.append(wall)
    wallsy5 += 100
    wallgroup.add(wall)

for i in range(walls6a):
    wall = GamesSprite(wallsx6, wallsy6, 100, 100, 'Wall.png')
    walls6.append(wall)
    wallsy6 += 100
    wallgroup.add(wall)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                char.yspd = -5
            if e.key == K_s:
                char.yspd = 5
            if e.key == K_a:
                char.xspd = -5
            if e.key == K_d:
                char.xspd = 5
        elif e.type == KEYUP:
            if e.key == K_w:
                char.yspd = 0
            if e.key == K_s:
                char.yspd = 0
            if e.key == K_a:
                char.xspd = 0
            if e.key == K_d:
                char.xspd = 0
            if e.key == K_SPACE:
                char.fire()
    if finish != True:
        windows.blit(bg, (0,0))
        # for wall in walls1:
        #     wall.reset()
        # for wall in walls2:
        #     wall.reset()
        # for wall in walls3:
        #     wall.reset()
        # for wall in walls4:
        #     wall.reset()
        # for wall in walls5:
        #     wall.reset()
        # for wall in walls6:
        #     wall.reset()
        enemy1.cooldown -= 1
        if enemy1.cooldown < 0:
            enemy1.cooldown = 100
            enemy1.fire()
        wallgroup.draw(windows)
        finishsprite.reset()
        enemy2.movement()
        enemygroup.draw(windows)
        char.reset()
        char.movement()
        bullets.update()
        bullets.draw(windows)
        enemybullets.update()
        enemybullets.draw(windows)
        sprite.groupcollide(bullets, wallgroup, True, False)
        sprite.groupcollide(bullets, enemygroup, True, True)
        if sprite.collide_rect(char, finishsprite):
            finish = True
            endingscreen = transform.scale(image.load('The End.webp'), (800, 160))
            windows.blit(endingscreen, (530, 450))
        if sprite.spritecollide(char, enemygroup, False):
            finish = True
            endingscreen = transform.scale(image.load('You Died.webp'), (windowwidth, windowheight))
            windows.blit(endingscreen, (0, 0))
        if sprite.spritecollide(char, enemybullets, True):
            finish = True
            endingscreen = transform.scale(image.load('You Died.webp'), (windowwidth, windowheight))
            windows.blit(endingscreen, (0, 0))
    clock.tick(60)
    display.update()
