import pygame, random


black = (0, 0, 0)
white = (255,255,255)
pygame.init()


width = 480
height = 600
FPS = 60
score = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('yo')

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, 1, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    myfont = pygame.font.SysFont("monospace",40)
    textSurface = myfont.render(text, 1, (200, 200, 200))
    #largeText = pygame.font.Font('face.ttf',40)
    #TextSurf, TextRect = text_objects(text, largeText)
    #TextRect.center = (30,30)
    screen.blit(textSurface, (30, 30))

class Player(pygame.sprite.Sprite):
    def __init__(ship):
        pygame.sprite.Sprite.__init__(ship)
        ship.image = pygame.transform.scale(player_img, (50,50))
        ship.image.set_colorkey(black)
        ship.rect = ship.image.get_rect()
        ship.rect.centerx = width/2
        ship.rect.bottom = height - 10
        ship.speedx = 0 


    def update(ship):
        ship.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            ship.speedx = -8
        if keystate[pygame.K_RIGHT]:
            ship.speedx = 8
        ship.rect.x += ship.speedx
        if ship.rect.right > width:
            ship.rect.right = width
        if ship.rect.left < 0:
            ship.rect.left = 0

    
            
    def bullet(ship):
        bullet = Bullet(ship.rect.centerx, ship.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(ship):
        pygame.sprite.Sprite.__init__(ship)
        ship.image = pygame.transform.scale(enemy_img, (60,40))
        ship.image.set_colorkey(white)
        ship.rect = ship.image.get_rect()
        ship.rect.x = random.randrange(width - ship.rect.width)
        ship.rect.y = random.randrange(-100, -40)
        ship.speedy = random.randrange(1, 8)
        ship.speedx = random.randrange(-3, 3)

    def update(ship):
        ship.rect.x += ship.speedx
        ship.rect.y += ship.speedy
        if ship.rect.top > height + 10 or ship.rect.left < -25 or ship.rect.right > width + 20:
            ship.rect.x = random.randrange(width - ship.rect.width)
            ship.rect.y = random.randrange(-100, -40)
            ship.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    
    def __init__(ship, x,y):
        pygame.sprite.Sprite.__init__(ship)
        ship.image = pygame.transform.scale(bullet_img, (15,15))
        ship.image.set_colorkey(white)
        ship.rect = ship.image.get_rect()
        ship.rect.bottom = y
        ship.rect.centerx = x
        ship.speedy = -10
        
    def update(ship):
        ship.rect.y += ship.speedy
        if ship.rect.bottom < 0:
            ship.kill()


player_img  = pygame.image.load('hey.png')
bullet_img  = pygame.image.load('bullet.png')
enemy_img = pygame.image.load('book.jpg')
worse_img = pygame.image.load('acorn.png')

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


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
        score +=  10
        print(score) 
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        
    hits = pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        running = False

    screen.fill(white)
    all_sprites.draw(screen)
    output = str(score)
    message_display(output)
    pygame.display.flip()

    

pygame.quit()
quit()
        

        

        

    

 



