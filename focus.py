import pygame, random
import time
import sys

black = (0, 0, 0)
white = (255,255,255)
cadetblue1 = (152,245,255)
cyan = (0,255,255)
gold = (255, 193, 37)
pygame.init()


width = 480
height = 600
FPS = 60
score = 0
start = time.time()
period = 15





pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('THE GREATEST GAME EVER')
clock = pygame.time.Clock()



    


font_name = 'font.ttf'



def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, gold)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

class Player(pygame.sprite.Sprite):
    def __init__(subject):
        pygame.sprite.Sprite.__init__(subject)
        subject.image = pygame.transform.scale(player_img, (50,50))
        subject.image.set_colorkey(black)
        subject.rect = subject.image.get_rect()
        subject.rect.centerx = width/2
        subject.rect.bottom = height - 10
        subject.speedx = 0
        subject.shoot_delay = 200
        subject.last_shot = pygame.time.get_ticks()
        



    def update(subject):
        subject.speedx = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            subject.speedx = -9
        if keystate[pygame.K_RIGHT]:
            subject.speedx = 9
        if keystate [pygame.K_SPACE]:
            subject.shoot()
        subject.rect.x += subject.speedx
        if subject.rect.right > width:
            subject.rect.right = width
        if subject.rect.left < 0:
            subject.rect.left = 0



    
    def shoot(subject):
        now = pygame.time.get_ticks()
        if now - subject.last_shot > subject.shoot_delay:
            subject.last_shot = now
            bullet = Bullet(subject.rect.centerx, subject.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            

class Mob(pygame.sprite.Sprite):
    def __init__(subject):
        pygame.sprite.Sprite.__init__(subject)
        subject.image = pygame.transform.scale(worse_img, (90,79))
        subject.image.set_colorkey(white)
        subject.rect = subject.image.get_rect()
        subject.rect.x = random.randrange(width - subject.rect.width)
        subject.rect.y = random.randrange(-100, -40)
        subject.speedy = random.randrange(1, 9)
        subject.speedx = random.randrange(-3, 3)
        subject.time_now = 0
  

    def update(subject):
        subject.rect.x += subject.speedx
        subject.rect.y += subject.speedy
        subject.time_now = pygame.time.get_ticks()
        if subject.rect.top > height + 10 or subject.rect.left < -15 or subject.rect.right > width + 10:
            subject.rect.x = random.randrange(width - subject.rect.width)
            subject.rect.y = random.randrange(-100, -40)
            subject.speedy = random.randrange(1, 11)

                 

class Bullet(pygame.sprite.Sprite):
    
    def __init__(subject, x,y):
        pygame.sprite.Sprite.__init__(subject)
        subject.image = pygame.transform.scale(bullet_img, (8,30))
        subject.image.set_colorkey(white)
        subject.rect = subject.image.get_rect()
        subject.rect.bottom = y
        subject.rect.centerx = x
        subject.speedy = -10
        
    def update(subject):
        subject.rect.y += subject.speedy
        if subject.rect.bottom < 0:
            subject.kill()

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "DESTROY   VIKAS", 64, width / 2, height / 4)
    draw_text(screen, "Arrow Keys to Move         Space To Fire", 22, width / 2, height / 2)
    draw_text(screen, "Press Any Key To Begin", 18, width / 2, height * 3 / 4)
    draw_text(screen, str(score), 50, width/2, 20)
    pygame.display.flip()
    waiting = True
    

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                for i in range(3,0,-1):
                    sys.stdout.write(str(i)+' ')
                    sys.stdout.flush()
                    time.sleep(1)
                waiting = False




        


                



background = pygame.image.load('stars.png')
background_rect = background.get_rect()
player_img  = pygame.image.load('hey.png')
bullet_img  = pygame.image.load('bullet.png')
enemy_img = pygame.image.load('book.jpg')
worse_img = pygame.image.load('vikas.png')
hurt_sound = pygame.mixer.Sound('oof.wav')
dead_sound = pygame.mixer.Sound('wasted.wav')
mlg_sound = pygame.mixer.Sound('mlg.wav')



                                


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    score = 0

game_over = True

running  = True



while running:
    
    clock.tick(FPS)
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        



        
        all_sprites.add(player)
        for i in range(8):
            newmob()
        score = 0
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        


    
    all_sprites.update()

 

    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        hurt_sound.play()
        score += 10
        if score == 500:
            mlg_sound.play()
            
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        
    hits = pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        dead_sound.play()
        game_over = True
        time.sleep(2)

    screen.fill(black)
    screen.blit(background, background_rect)

    draw_text(screen, str(score), 30, width / 2, 20)
    all_sprites.draw(screen)

    pygame.display.flip()
    

pygame.quit()
quit()
        

        

        

    

 



