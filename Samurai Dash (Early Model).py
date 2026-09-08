##10/07/2021
##Pygame Template

##Pygame Libraries

import random
import pygame

##Initialise pygame
pygame.init()
pygame.mixer.init()

##Screen Size and Frame Rate
WIDTH = 1500
HEIGHT = 900
FPS = 60

##Font Initialise
pygame.font.init()
FONT = pygame.font.Font("PixelBase.ttf",28)
SMALLFONT = pygame.font.Font("PixelBase.ttf",24)
TITLEFONT = pygame.font.Font("PixelBase.ttf",40)
ENDFONT = pygame.font.Font("PixelBase.ttf",100)
Typed = False
charactertyped = 0
slowcharactertyped = 0
CharactertypedCheck = False
SlowTypingMessage = str("")


##Font Attributes
typing_speed = 40
TYPING = pygame.USEREVENT+11
slowtyping_speed = 200
SLOWTYPING = pygame.USEREVENT+12

##Background
Background = pygame.image.load("BG.png")
##Base kept so it can be varied, but easily brought back to base
BaseBGspeed = 15
BGspeed = BaseBGspeed

##Sound
Sword_draw = pygame.mixer.Sound("Sword draw.wav")
Sword_clash = pygame.mixer.Sound("Sword Clash.wav")
Footstep1 = pygame.mixer.Sound("Footstep1.wav")
Footstep2 = pygame.mixer.Sound("Footstep2.wav")
Gore_slash = pygame.mixer.Sound("Slashed SFX.wav")

##Static Images
Title = pygame.image.load("Title place name.png")
Mousereticle = pygame.image.load("Reticle.png")
Big_plat = pygame.image.load("Bigplatform2.png")

SamuraiIMG = pygame.image.load("SamuraiTitle.png")
EnemiesIMG = pygame.image.load("EnemiesTitle.png")
    
##Animations

##ANIMATION NOTES:
##Frametracker are set to -1, not 0, this is becuase the frame tracker will always tick before -1 causes an error (It no longer causes errors)

KKRun = [pygame.image.load("SamuraiSprint1.png"),pygame.image.load("SamuraiSprint2.png"),pygame.image.load("SamuraiSprint3.png"),pygame.image.load("SamuraiSprint4.png"),pygame.image.load("SamuraiSprint5.png"),pygame.image.load("SamuraiSprint6.png")]
KKFall = pygame.image.load("SamuraiFall3.png")
KKJump = pygame.image.load("SamuraiLeap.png")
KKSlash = [pygame.image.load("Samurairun1.png"),pygame.image.load("Samurairun2.png"),pygame.image.load("Samuraislash1.png"),pygame.image.load("Samuraislash2.png")]
KKCollapse = [pygame.image.load("SamuraiCollapse1.png"),pygame.image.load("SamuraiCollapse2.png"),pygame.image.load("SamuraiCollapse3.png"),pygame.image.load("SamuraiCollapse4.png"),pygame.image.load("SamuraiCollapse5.png")]
KKUnsheathe = [pygame.image.load("SamuraiUnsheathe13.png"),pygame.image.load("SamuraiUnsheathe12.png"),pygame.image.load("SamuraiUnsheathe11.png"),pygame.image.load("SamuraiUnsheathe10.png"),pygame.image.load("SamuraiUnsheathe8.png"),pygame.image.load("SamuraiUnsheathe7.png"),pygame.image.load("SamuraiUnsheathe9.png"),pygame.image.load("SamuraiUnsheathe6.png"),pygame.image.load("SamuraiUnsheathe5.png"),pygame.image.load("SamuraiUnsheathe4.png"),pygame.image.load("SamuraiUnsheathe3.png"),pygame.image.load("SamuraiUnsheathe1.png"),pygame.image.load("SamuraiUnsheathe2.png")]#,pygame.image.load("SamuraiUnsheathe14.png")]
KKDeathfall = pygame.image.load("Samuraiairfall.png")

Gold_knightRun = [pygame.image.load("KKRun1.png"),pygame.image.load("KKRun2.png"),pygame.image.load("KKRun3.png"),pygame.image.load("KKRun4.png"),pygame.image.load("KKRun5.png"),pygame.image.load("KKRun6.png")]
Gold_knightCharge = pygame.image.load("KKCharge1.png")
Gold_knightDead = pygame.image.load("KKDead.png")
Gold_knightTaunt = [pygame.image.load("KKTaunt1.png"),pygame.image.load("KKTaunt2.png"),pygame.image.load("KKTaunt3.png"),pygame.image.load("KKTaunt4.png"),pygame.image.load("KKTaunt5.png"),pygame.image.load("KKTaunt6.png")]

Spectre_idle = [pygame.image.load("Spectreidle1.png"),pygame.image.load("Spectreidle2.png"),pygame.image.load("Spectreidle3.png"),pygame.image.load("Spectreidle4.png")]
Spectre_slash = [pygame.image.load("Spectreswing1.png"),pygame.image.load("Spectreswing2.png"),pygame.image.load("Spectreswing3.png")]
Spectre_death = [pygame.image.load("Spectredeath1.png"),pygame.image.load("Spectredeath2.png"),pygame.image.load("Spectredeath3.png"),pygame.image.load("Spectredeath4.png"),pygame.image.load("Spectredeath5.png"),pygame.image.load("Spectredeath6.png"),pygame.image.load("Spectredeath7.png")]
##Flipped


##Player Attributes
##Playejumpspeed should be greater than jump height, or else player will fall during jump
Playerjumpspeed = int(35)
Playerjumpspeedvary = Playerjumpspeed
Playerjumpheight = int(25)
Playerjumpcap = int(0)
Playerjumping = False
Playerfalling = False
Playercasting = False
Playeronfloor = False
Playerplatformcorrection = False
Playerup = False
Playerdown = False
Playerleft = True
Playerright = False
Playerfallcap = Playerjumpheight-1
Playerhp = int(100)
PlayerINV = False

##Platform attributes
Baseplatformposy = (HEIGHT-200)

##Particle Config
Baseparticleon = True
PARTICLE_FREQ = 3

##Enemy Config
SPECTRE_FREQ = 10000
GOLDEN_FREQ = 5000

Enemieson = True



##Misc
Coins = int(0)
Gamebegun = False
GameSTART = False
textloc = WIDTH//30
Framecounter = 0
Ready = False
        
    
        
##Player Related Timers
playerjump_time = 15
PLAYERJUMP_EVENT = pygame.USEREVENT+1

PLAYERINVFRAMES_EVENT = pygame.USEREVENT+30
playerinv_time = 1000
pygame.time.set_timer(PLAYERINVFRAMES_EVENT, playerinv_time)
PLAYERINVFRAMES = False

##Animation Tickers



##Colour Library
BLACK = (0, 0, 0)
WHITE = (255, 255 , 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
DARKBLUE = (0,100,130)
BROWN = (150, 75, 0)
PURPLE = (216, 191, 216)
VIOLET = (238,130,238)
ORANGE = (255,215,0)
PINK = (255,192,203)
TRANSPARENT = (0,0,0,0)


##Positions
XMiddle = WIDTH/2
##Objects

def Flipx(image):
    imageF = pygame.transform.flip(image,True,False)

    return imageF

def Scale(image,sprite,mag):
    width = int((sprite.rect.x*mag)//1)
    height = int((sprite.rect.y*mag)//1)
    
    imageS = pygame.transform.scale(image,(width,height))

    return imageS
    
def Randomiser(totalrandom):
    outofrandom = random.randint(1,totalrandom)
    
    return outofrandom
    
       
##Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        ##170, 108
        ##118, 72
        self.image = pygame.Surface((170,108))
        self.rect = self.image.get_rect()
        self.rect.centerx = (350)
        self.rect.bottom= largeplatform1.rect.top
        self.image.set_colorkey(GREEN)
        self.speedx = 0
        self.speedy = 0
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = KKFall
        ##Self.frame means current animation frame

        self.dead = False
        self.deadframes = 0

        self.slashedframes = 0

        self.anireset = False
        ##Slash is the anim, killing are the damage frames
        self.slashing = False
        self.killing = False

        self.deadframe_beenreset = False


       
    def update(self):
        if Gamebegun == True:
            global Playerfallcap
            if self.frametracker != FPS:
                self.frametracker +=1
            else:
                self.frametracker = 0

                
            ##Player-State checker
            ##Animations
            while True:
                try:
                    ##Types of anim
                    global Ready
                    if Ready == True:
                
                        if Playerfalling == True and self.slashing == False:
                            
                            self.frame = KKFall
                        

                        elif Playerjumping == True and self.slashing == False:
                            self.frame = KKJump

                        elif self.slashing == True and Playerfalling == False:
                            self.frame = KKSlash[self.anitrack]
                            ##Changes the timing of the animation depedning on the frame, the run is slower than the slash
                            if self.frametracker > 5 and self.slashedframes <=1 or self.frametracker>3 and self.slashedframes > 1 :
                                self.frametracker = 0
                                self.anitrack+=1
                                self.slashedframes +=1 
    ##                            if self.anitrack== 2:
    ##                                self.rect.x+=30
                                
                                if self.slashedframes == 1:
                                    self.rect.x +=10
                                    

                                ##If you want constant movement, not just between animations flips, unindent this
                                if self.slashedframes == 2:
                                    self.killing = True
                                    self.rect.x+=40

                                    
                            if self.slashedframes > 3:
                                self.slashing = False
                                self.slashedframes = 0
                                self.rect.x-=40
                                self.killing = False
                                break

                        elif self.dead == False:
                            self.frame = KKRun[self.anitrack]
                            if self.frametracker > 2:
                                self.frametracker = -1
                                self.anitrack+=1

                                    

                        if self.dead == True:
                            if self.deadframe_beenreset == False:
                                self.deadframe_beenreset = True
                                self.frametracker = 0
                                self.anitrack = 0
                                self.slashing = False
            

                                
                            
                            if Playerfalling == True or Playerjumping == True:
                                self.frame = KKDeathfall
                            else:
                                self.frame = KKCollapse[self.anitrack]

                                
                                if self.frametracker > 5 and self.deadframes < 2:
                                        self.frametracker = -1
                                        self.anitrack+=1
                                        self.deadframes+=1
                                        
                                if self.frametracker >20 and self.deadframes >=2:
                                    self.frametracker = -1                                   
                                    self.anitrack+=1
                                    self.deadframes+=1
                             
                                    
                    if Gamebegun == True and Ready == False:
                        self.frame = KKUnsheathe[self.anitrack]
                        if self.frametracker > 2:
                            self.frametracker = -1
                            self.anitrack+=1
                            if self.anitrack == 3: Sword_draw.play()
                            
                    

                    self.image.fill(GREEN)
                    if self.deadframes > 4:
                        self.frame = KKCollapse[4]
                    self.image.blit(self.frame,(0,0))
                    break
                        
                except IndexError:
                    self.anitrack = 0
                    
                    ##Game ready, this is for the taunt at the start
                    if Ready == False:
                        
                        ##Once the animation which increases the rect is over, it is sent back to normal size
                        self.ready_positionx = self.rect.left
                        self.ready_positiony = self.rect.bottom
                        self.image = pygame.Surface((118, 72))
                        self.rect = self.image.get_rect()
                        self.image.set_colorkey(GREEN)
                        self.rect.left = (self.ready_positionx)
                        self.rect.bottom = self.ready_positiony
                        self.rect.x+=30
                        self.anitrack = 4
                        
                        Ready = True
##                    if self.slashing == True:
##                        self.slashing = False
##                        self.slashedframes = 0

            self.speedx=0
            self.speedy=0

            keystate = pygame.key.get_pressed()

            if Playerfalling == True:
                self.speedy = Playerfallcap - Playerjumpheight
                if self.speedy < 3:
                    self.speedy == 3
                Playerfallcap +=1
            elif Playerfalling == False and Playerjumping == False:
                Playerfallcap = Playerjumpheight-1

            if self.slashing == False and Ready == True and self.dead == False:
                if keystate[pygame.K_a]:
                    self.speedx = -6
                if keystate[pygame.K_d]:
                    self.speedx = 8
    
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            

    def jump(self):
        self.speedy = -Playerjumpspeedvary
        self.rect.y += self.speedy

    def slash(self):
        if self.dead == False and Playerjumping == False and Playerfalling == False and self.slashing == False:

            self.anitrack = 0
            self.frametracker=0
            self.slashing = True
##Enemies

class Spectre(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((322,168))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0,WIDTH)
        self.rect.top= largeplatform1.rect.top
        self.image.set_colorkey(GREEN)
        self.speedx = 0
        self.speedy = 0
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = Spectre_idle[1]
        ##Self.frame means current animation frame

        self.dead = False
        self.speedx = 0
        self.speedy = 0

        self.slashing = False

        self.taunting = False
        self.killing = False

    def update(self):
        self.frametracker +=1
        try:
            if self.frametracker >3 and self.dead == False and self.slashing == False:
                self.frame = Spectre_idle[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1

            elif self.frametracker >3 and self.dead == False and self.slashing == True and player.dead== False:
                self.frame = Spectre_slash[self.anitrack]
                if self.frame == Spectre_slash[1]:
                    self.killing = True
                else:
                    self.killing = False
                self.anitrack +=1
                self.frametracker = -1

            elif self.dead == True and self.frametracker >3:
                self.frame= Spectre_death[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1
       
        except IndexError:
            self.anitrack = 0
            if self.dead == True:
                self.kill()
            if self.slashing == True:
                self.slashing = False

        if player.rect.centerx>self.rect.right-100:
            self.speedx = 3
        elif player.rect.centerx<self.rect.right-100:
            self.speedx = -2
        else:
            self.speedx = 0

        if player.dead == False:
            if player.rect.centery<self.rect.centery-2:
                self.speedy = -4
            elif player.rect.centery>self.rect.centery+2:
                self.speedy = 4
            else:
                self.speedy = 0

            if self.speedy == 0 and self.rect.centerx< player.rect.centerx+20 and self.rect.right >player.rect.centerx:
                if self.slashing == False:
                    self.slashing = True
                    self.anitrack = 0
                    
            self.rect.y+=self.speedy
            self.rect.x+=self.speedx
        else:
            self.slashing == False
            self.dead = True
            
        

        self.image.blit(self.frame,(0,0))

        
        
class Golden_knight(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((104,80))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom= largeplatform1.rect.top
        self.image.set_colorkey(GREEN)
        self.speedx = 0
        self.speedy = 0
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = Gold_knightCharge
        ##Self.frame means current animation frame

        self.dead = False
        self.speedx = -6
        self.speedy = 0

        self.charging = False

        self.taunting = False

        
        
    def update(self):
        self.frametracker += 1
        if self.frametracker>60: self.frametracker=0
        self.speedx = BGspeed*-1
        try:
            if self.frametracker >1 and self.dead == False and BGspeed > 7:
                self.frame = Gold_knightRun[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1
            elif self.frametracker >2 and self.dead == False:
                if self.taunting == False:
                    self.taunting = True
                    
                    self.ready_positionx = self.rect.left
                    self.ready_positiony = self.rect.bottom
                    self.image = pygame.Surface((176,110))
                    self.rect = self.image.get_rect()
                    self.image.set_colorkey(GREEN)
                    self.rect.left = self.ready_positionx
                    self.rect.bottom = self.ready_positiony
                    
                self.frame = Gold_knightTaunt[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1             
        except IndexError:
            self.anitrack = 0


        if player.dead == False and self.rect.x+200 > player.rect.left and  player.rect.left > self.rect.right-500:
            self.frame = Gold_knightCharge
            self.charging = True
        else:
            self.charging = False
        if self.dead == True:
            self.frame = Gold_knightDead
            self.speedy = 2
        self.image.blit(Flipx(self.frame),(0,0))

        if self.rect.right <0:
            self.kill()

        self.rect.x +=self.speedx
        self.rect.y +=self.speedy
    
##Platforms    
class LargePlatform(pygame.sprite.Sprite):

    def __init__(self,designation):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3000, 250))
        self.rect = self.image.get_rect()
        if designation == 1:            
            self.rect.left = (0)
        elif designation == 2:
            self.rect.right = 1
        else:
            self.rect.right = 1
        self.rect.top = (Baseplatformposy)
        self.speedx = 0
        self.speedy = 0
        self.image.blit(Big_plat,(0,0))
##        self.image.fill(WHITE)

    def update(self):
        global BGspeed
        global BaseBGspeed
        if player.dead == True:
            if GAMEFRAME % 30 == 0:
                if BGspeed > 0:
                    BGspeed-=2
                else:
                    BGspeed = 0
                    
        elif player.speedx == 8 and BGspeed == BaseBGspeed:
            BGspeed +=6
        elif player.speedx == -6 and BGspeed == BaseBGspeed:
            BGspeed -=4
        else:
            BGspeed = BaseBGspeed
        self.rect.x -= (BGspeed)
        if self.rect.right<=0:
            self.rect.left = WIDTH


class SmallPlatform(pygame.sprite.Sprite):

    def __init__(self,x,y,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        
    def update(self):
        hits = pygame.sprite.spritecollide(self,player_group,False)
        for hit in hits:
            if Playerjumping == False:
                player.rect.bottom = self.rect.top+1
                
##            smallplats.add(smallplatform1)
##            smallplats.add(smallplatform2)
##        else:
##            platforms.add(smallplatform1)
##            platforms.add(smallplatform2)
##            all_sprites.add(platforms)
       
    
        
        
            

##Particle Effects
class Baseparticle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((6,random.randint(6,8)))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(WIDTH,WIDTH+50)
        self.rect.y = random.randint(-200,HEIGHT-200)#
        self.speedx = random.randint(5,12)*-1
        self.startspeed = self.speedx
        self.speedy = random.randint(1,2)
        self.playerdeadspeed = 0
        
    def update(self):
        global BGspeed
        global BaseBGspeed
        if player.speedx == 8 and self.speedx == self.startspeed:
            self.speedx -=3
        elif player.speedx == -6 and self.speedx == self.startspeed:
            self.speedx  +=3
        else:
            self.speedx = self.startspeed

        if player.dead == True and self.playerdeadspeed == 0:
            self.playerdeadspeed = random.randint(2,6)*-1

        
        self.rect.y += self.speedy
        if player.dead == True:
            self.rect.x += self.playerdeadspeed
        elif player.dead == False:
            self.rect.x +=self.speedx
            
        if self.rect.top >HEIGHT or self.rect.right<0:
            self.kill()

class Portrait(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((512,530))
        self.image.set_colorkey(GREEN)
        self.image.blit(SamuraiIMG,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery = HEIGHT//2

class Enemies_Portrait(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((700,900))
        self.image.set_colorkey(GREEN)
        self.image.blit(EnemiesIMG,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 250
        self.rect.centery = HEIGHT//2        

##Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Success!")
clock = pygame.time.Clock()

##Group Declaration
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_group = pygame.sprite.Group()
##infos = pygame.sprite.Group()
smallplats = pygame.sprite.Group()
opening = pygame.sprite.Group()
particles = pygame.sprite.Group()
largeplats = pygame.sprite.Group()
gold_group = pygame.sprite.Group()
spec_group = pygame.sprite.Group()

##Sprite Declaration
largeplatform1 = LargePlatform(1)
largeplatform2 = LargePlatform(2)
largeplatform3 = LargePlatform(3)
player = Player()
portrait = Portrait()
enemies_portrait = Enemies_Portrait()
baseparticle = Baseparticle()
##infoholder = Infoholder()

##Small Platform Delcarations
smallplatform1 = SmallPlatform(XMiddle,HEIGHT-400 ,300)
smallplatform2 = SmallPlatform(XMiddle,HEIGHT-650 ,150)

##Sprite Adding

platforms.add(largeplatform1)
platforms.add(largeplatform2)
platforms.add(largeplatform3)
largeplats.add(platforms)
platforms.add(smallplatform1)
platforms.add(smallplatform2)
smallplats.add(smallplatform1)
smallplats.add(smallplatform2)

opening.add(portrait)
opening.add(enemies_portrait)

##all_sprites.add(basicenemies)
##all_sprites.add(player)
##all_sprites.add(platforms)




##Setting timers

##Particle Timer
particle_timer = 0
now3 = pygame.time.get_ticks()

##Golden Knight
golden_timer = 0
now4 = pygame.time.get_ticks()

##Spectre Timer
spectre_timer = 0
now5 = pygame.time.get_ticks()

##Setting Timers w/ USEREVENTS
pygame.time.set_timer(PLAYERJUMP_EVENT, playerjump_time)
PLAYERJUMP_EVENT = False
pygame.time.set_timer(TYPING, typing_speed)
pygame.time.set_timer(SLOWTYPING, slowtyping_speed)


GAMEFRAME = 0
## Game Loop ##

running = True
while running:
    GAMEFRAME += 1
    clock.tick(FPS)
    if Framecounter!=FPS:
        Framecounter+=1
    else:
        Framecounter = 0
    Mouseco = []
    Mouseco = pygame.mouse.get_pos()
    mx = int(Mouseco[0])
    my = int(Mouseco[1])
    ## 1)Input Process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_k:
                player.dead = True

            if event.key == pygame.K_SPACE:
                if Gamebegun == False:
                    Gamebegun = True
                    UntilStart = pygame.time.get_ticks()
                    all_sprites.add(player)
                    player_group.add(player)

                else:
                    player.slash()
                    
            if Playerfalling == False and Playerjumping == False:
                if event.key == pygame.K_w:
                    if player.dead == False and Ready == True:
                        PLAYERJUMP_EVENT = pygame.USEREVENT+1
                
        elif event.type == PLAYERJUMP_EVENT:
            if Playerjumpcap != Playerjumpheight:
                Playerjumping = True
                player.jump()                
                Playerjumpcap+= 1
                Playerjumpspeedvary = Playerjumpheight-Playerjumpcap
                
            else:
               PLAYERJUMP_EVENT = False
               Playerjumpcap = 0
               Playerjumpspeedvary = Playerjumpspeed
               Playerjumping = False
        
                
        if event.type == TYPING:
            if charactertyped!=len(TypingMessage):
                Typed = False
                charactertyped += 1

        if event.type == PLAYERINVFRAMES_EVENT:
            PlayerINV = False
        

    ##Baseparticle Spawn Timer
    if Baseparticleon == True:
        particlesize = random.randint(1,3)
        particle_timer = pygame.time.get_ticks() - now3
        if particle_timer >= PARTICLE_FREQ:
            now3 = pygame.time.get_ticks()
            for number in range(particlesize):
                bp = Baseparticle()
                particles.add(bp)
                all_sprites.add(bp)

    ##Golden Knight spawn Timer
    if Enemieson == True and Ready == True:
        golden_timer = pygame.time.get_ticks() - now4 - UntilStart
        if golden_timer >= GOLDEN_FREQ:
            now4 = pygame.time.get_ticks()
            GK = Golden_knight()
            enemies.add(GK)
            all_sprites.add(GK)
            gold_group.add(GK)

    ##Spectre spawn Timer
    if Enemieson == True and Ready == True:
        spectre_timer = pygame.time.get_ticks() - now5 - UntilStart
        try: ##Checking whetehr the spectre is dead or not is in consequential, we are actually looking for a name error to prove his existence
            if SP.dead == True:
                if spectre_timer >= SPECTRE_FREQ:
                    now5 = pygame.time.get_ticks()
                    SP = Spectre()
                    enemies.add(SP)
                    all_sprites.add(SP)
                    spec_group.add(SP)
        
                
        except NameError:
            if spectre_timer >= SPECTRE_FREQ:
                now5 = pygame.time.get_ticks()
                SP = Spectre()
                enemies.add(SP)
                all_sprites.add(SP)
                spec_group.add(SP)
        
            
                        

    ##Collisions
            
    hits = pygame.sprite.spritecollide(player, platforms, False)

    if hits:
        GameSTART = True
        Playerfalling  = False
        if Playerjumping == False:
            Playerplatformcorrection = True
    else:
        if Playerjumping == False:
            Playerfalling = True
        
    hits = pygame.sprite.groupcollide(largeplats,player_group,False,False)
    for hit in hits:
        player.rect.bottom = Baseplatformposy+1


    hits = pygame.sprite.groupcollide(gold_group,player_group,False,False)
    if hits:
        if GK.dead == True:
            pass
        elif player.killing == True:
            GK.dead = True
            Sword_clash.play()
        else:
            player.dead = True


    hits = pygame.sprite.groupcollide(spec_group,player_group,False,False)
    if hits:
        if SP.dead == True:
            pass
        elif player.killing == True:
            SP.dead = True
            Sword_clash.play()
        elif SP.killing == True:
            if player.dead == False:
                Gore_slash.play()
            player.dead = True



    ##Primary collision to stop falling, correction within the class itself

       

        
    ## 2)Update
    
    all_sprites.update()
    if Gamebegun == True:
        if Ready == True:
            platforms.update()
        ##infos.update()
            smallplats.update()
    else:
        opening.update()
        

    ## 3)Text sorting
    
    TitleMessage = "Press Space To Start"

    ## 4)Render
    screen.blit(Background,(-190,0))
    
    if Gamebegun == False:
        ##screen.blit(Title,(WIDTH//1.8-Title.get_width()//2+8,HEIGHT//4))
        particles.draw(screen)
        
    if Typed == False and Gamebegun == False:
        TypingMessage  = TitleMessage
        characters = str(TitleMessage[:charactertyped])
        Typed = True

    TitleMessageTyped= TITLEFONT.render(characters,False,WHITE)
    
    if Gamebegun == True:
        all_sprites.draw(screen)
        particles.draw(screen)
        platforms.draw(screen)
        player_group.draw(screen)

    else:
        opening.draw(screen)


    
        screen.blit(Mousereticle,(mx-Mousereticle.get_width()//2,my - Mousereticle.get_height()//2))
        ##Key Rendering

        ##Infobar Coing rendering  


    if Gamebegun == False:
        AuthorMessage = FONT.render("By Tyler Lynch",False,(WHITE))
        screen.blit(TitleMessageTyped,(WIDTH//2-(300),HEIGHT//2))
        screen.blit(AuthorMessage,(WIDTH//2-(120),HEIGHT//1.2))
    ##after render flip display
    pygame.display.flip()
    
pygame.quit()
        
