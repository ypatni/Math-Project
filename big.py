import pygame, random, time, sys

black = (0, 0, 0)
white = (255,255,255)
cadetblue1 = (152,245,255)
cyan = (0,255,255)
gold = (255, 193, 37)
green = (0, 255, 0)
red = (91,24,0)
pygame.init()

width = 480
height = 600
FPS = 60
score = 0
start = time.time()
period = 15

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
    
#declare 'Player' Sprite
class Player(pygame.sprite.Sprite):
    def __init__(subject):
        pygame.sprite.Sprite.__init__(subject)
        
        #characteristics of player
        subject.image = pygame.transform.scale(player_img, (50,50))
        subject.image.set_colorkey(black)
        subject.rect = subject.image.get_rect()
        
        #placement of the sprite 
        subject.rect.centerx = width/2
        subject.rect.bottom = height - 15
        
        #intial speed of sprite
        subject.speedx = 0
        subject.shoot_delay = 200
        subject.last_shot = pygame.time.get_ticks()

    def update(subject):
        subject.speedx = 0
        
        keystate = pygame.key.get_pressed()
        # if left arrow key is pressed
        if keystate[pygame.K_LEFT]:
            subject.speedx = player_speed_x_left
        # if right arrow key is pressed
        if keystate[pygame.K_RIGHT]:
            subject.speedx = player_speed_x_right
        # if space key is pressed
        if keystate [pygame.K_SPACE]:
            subject.shoot()

        # if both keys are pressed
        if keystate[pygame.K_LEFT] and keystate[pygame.K_RIGHT]:
            subject.speedx = 0
        # if none of the keys are pressed
        if not keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
            subject.speedx = 0
            
        # making sure that the sprite stays on the screen
        subject.rect.x += subject.speedx
        if subject.rect.right > width:
            subject.rect.right = width
        if subject.rect.left < 0:
            subject.rect.left = 0

    def shoot(subject):
        now = pygame.time.get_ticks()
        # to keep the bullets shooting when spacebar is held
        
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
        subject.speedy = random.randrange(5, 11)
        subject.speedx = random.randrange(-3, 3)
        subject.time_now = 0

    def update(subject):
        subject.rect.x += subject.speedx
        subject.rect.y += subject.speedy
        subject.time_now = pygame.time.get_ticks()
        if subject.rect.top > height + 10 or subject.rect.left < -15 or subject.rect.right > width + 10:
            subject.rect.x = random.randrange(width - subject.rect.width)
            subject.rect.y = random.randrange(-100, -40)
            subject.speedy = random.randrange(5, 11)

    def drop_powerup(subject):
        powerup = Powerup(subject.rect.centerx, subject.rect.top)     # need this to be from most recent dead shrek
        all_sprites.add(powerup)
        powerups.add(powerup)

class Powerup(pygame.sprite.Sprite):
    def __init__(subject, x, y):
        pygame.sprite.Sprite.__init__(subject)
        subject.image = pygame.transform.scale(powerup_img, (59,50))
        subject.image.set_colorkey(white)
        subject.rect = subject.image.get_rect()
        subject.rect.x = x
        subject.rect.y = y
        subject.speedy = 3
        subject.speedx = random.randrange(-1, 1)

    def update(subject):
        subject.rect.x += subject.speedx
        subject.rect.y += subject.speedy

        if subject.rect.right > width:
            subject.rect.right = width
        if subject.rect.left < 0:
            subject.rect.left = 0
        if subject.rect.bottom > height:
            subject.kill()

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



class button():
    def __init__(self, color, x,y,width,height,text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        font = pygame.font.Font(font_name, 60)
        text = font.render(self.text, 1, gold)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
leaderboard = button(red, 53, 85, 375, 50, 'LEADERBOARD')
exit_leaderboard = button(red, 165, 500, 150, 50, ' EXIT')

def open_leaderboard():
    screen.blit(background, background_rect)
    exit_leaderboard.draw(screen, black)
    draw_text(screen, "Leaderboard", 64, width / 2, height / 8)
    draw_text(screen, 'PLACE', 40, 75, 175)
    #draw_text(screen, 'NAME', 40, width / 2, 175)
    draw_text(screen, 'SCORE', 40, 400, 175)
    for i in range(0, len(scores)):
        draw_text(screen, str(i+1), 64, ((width / 4)-35), (200 + 64*i))
        draw_text(screen, str(scores[i]), 64, 400, (200 + 64*i))
        #draw_text(screen, str(names[i]), 64, (width * 2/3), (175 + 64*i))
    pygame.display.flip()

    waiting = True

    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_leaderboard.isOver(pos):
                    waiting = False
                    show_screen()
                    break

def show_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "DESTROY SHREK", 64, width / 2, height / 4)
    draw_text(screen, "Arrow Keys to Move         Space To Fire", 22, width / 2, height / 2)
    draw_text(screen, "Press Any Key To Begin", 18, width / 2, height * 3 / 4)
    draw_text(screen, str(score), 50, width/2, 20)
    leaderboard.draw(screen, black)
    pygame.display.flip()
    waiting = True

    start_time = time.time()
    
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if leaderboard.isOver(pos):
                    waiting = False
                    open_leaderboard()
                    break
            
            if event.type == pygame.KEYUP:
                if (time.time() - start_time > 2):
                    num_spot = 200
                    for i in range(3,0,-1):
                        sys.stdout.write(str(i)+' ')
                        draw_text(screen, str(i), 30, num_spot, 200)
                        num_spot += 40
                        pygame.display.flip()
                        sys.stdout.flush()
                        time.sleep(1)
                    waiting = False

background = pygame.image.load('stars.png')
background_rect = background.get_rect()
player_img  = pygame.image.load('hey.png')
bullet_img  = pygame.image.load('bullet.png')
enemy_img = pygame.image.load('book.jpg')
worse_img = pygame.image.load('shrek_small.png')
powerup_img = pygame.image.load('powerup_img.png')
hurt_sound = pygame.mixer.Sound('bruh.wav')
dead_sound = pygame.mixer.Sound('wasted.wav')
mlg_sound = pygame.mixer.Sound('mlg.wav')
powerup_sound = pygame.mixer.Sound('powerup_sound.wav')
scores = []
names = []
start_time_powerup = 0
player_speed_x_left = -7
player_speed_x_right = 7

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    

# game loop


game_over = True

running  = True

while running:
    
    clock.tick(FPS)
    if game_over:
        # go back to original screen
        
        show_screen()
        game_over = False
        # reset all attributes of game
        
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()

        # spawns in new mobs
        
        all_sprites.add(player)
        for i in range(random.randint(3,5)):
            newmob()
        score = 0
        player_speed_x_left = -7
        player_speed_x_right = 7

            # exit out of game
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            

    all_sprites.update()
    
    # when bullets hits mobs
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        hurt_sound.play()
        score += 10
        if score == 500:
            mlg_sound.play()
        if (random.randint(1,101) <= 5+len(mobs)):
            if (len(powerups) < 3):
                Mob.drop_powerup(m)
            if (random.randint(1,101) <= 50+len(mobs)):
                newmob()
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # when player hits mobs
    
    hits = pygame.sprite.spritecollide(player,mobs,False)
    if hits:
        dead_sound.play()
        scores.append(score)
        scores.sort(reverse=True)
        time.sleep(2)
        game_over = True

    hits = pygame.sprite.spritecollide(player,powerups,True) # CREATE GRAPHICS FOR GETTING POWERUP
    if hits:
        powerup_sound.play()
        score += 50
        player.shoot_delay -= 50
        if player_speed_x_left >= -10:
            player_speed_x_left -= 1
        if player_speed_x_right <= 10:
            player_speed_x_right += 1
        start_time_powerup = time.time()
    if (time.time() - start_time_powerup > 5):
        player.shoot_delay = 200
    
    screen.blit(background, background_rect)

    draw_text(screen, str(score), 30, width / 2, 20)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()
quit()
