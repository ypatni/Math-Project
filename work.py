import pygame, random


black = (0, 0, 0)
white = (255,255,255)
pygame.init()


width = 480
height = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('yo')
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,50))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 10
        self.speedx = 0 


    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    
            
    def bullet(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img, (60,40))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

#class second(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(worse_img, (60,40))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    #def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (20,20))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


player_img  = pygame.image.load('hey.png')
bullet_img  = pygame.image.load('bullet.png')
enemy_img = pygame.image.load('book.jpg')
worse_img = pygame.image.load('acorn.jpg')

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
seconds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    
for i in range(8):
    s = second()
    all_sprites.add(s)
    seconds.add(s)


running  = True

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.bullet()

   

    
    all_sprites.update()

 

    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    hits = pygame.sprite.groupcollide(seconds,bullets,True,True)
    for hit in hits:
        s = second()
        all_sprites.add(s)
        seconds.add(s)
        
    hits = pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        running = False
        
    hits = pygame.sprite.spritecollide(player,seconds,False)
    if hits:
        running = False

    screen.fill(white)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
quit()
        

        

        

    

 



