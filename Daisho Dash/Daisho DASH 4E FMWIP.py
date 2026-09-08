##10/07/2021

##NOTES:
##Gamestarting:
'''
There are three main Variables for starting the game
Ready - When ready is True, enemies begun to spawn and the game has truly begun, it starts when the players unsheathes their blade (Check Player Class)
Gamebegun - Somewhat misleading, as it was made first, Gamebegun is when the Large platform and the player is in poisition, Gamebegun becomes True once BGshift is False, and, as stated prior, the two main sprites are in position
BGshift - This is the cause of the fancy shift at the beginning (Where the platform and player rise), it is activated when Space key is pressed (Check key events)

When ALL of these are false it displays the 'Opening' (Image of all characters (and my name :D))
'''
##Player Quirks
'''
The player, despite the long amount of code, is a relatively simple sprite, however the jump can be quite confusing
The Jump Constists of SIX main variables:
Playerjumpspeed - This is the amount of BASE distance (It varies with "jumpspeedvary", this is for a more realistic ascent) the player ascends in 1 frame of jumping
Playerjumpheight - This is the amount of frames the player jumps for
Playerjumpcap - This is set to 0 at start; As the player begins to ascend, this accumulates and is subtracted from Playerjumpspeed (Forming Playerjumpspeedvary), this causes a more realistic inclince
Playerfallcap - Essentially Playerjumpcap but in reverse, this allows for a smooth descent
Playerjumping - Just the state of whether or not the player is jumping
Playerfalling - Same as above, jsut for falling
'''
##Animation
'''
I have made several different methods of animation, this one is the best so far, it allows for:
More than one sprite from same class to be animated at the same time
Each sprite to be on different animation frames at the same times
Varying Animation speeds (Even DURING an animation, that animation can vary in speed)
Seamless Looping
Seamless and easy to include and remove animation frames (It just works, you dont need to manually adustt animation sizes and such)

Animations Consists of three main Variables, here's how it works:
Frametracker - There is a 'self.frametracker' in every sprite that needs animation, every frame the sprite is updated, this accumulates (it resets to -1 (-1 becuase its added to at the start of every update) when it reaches the FPS
Anitrack - Everytime a timer is exceeded (Timers are calculated with Frametracker), the self.anitrack increases by 1, the anitrack is the number used to find the animation frame of an animation reel list
(self.)Frame - To only have one singular blit, the self.frame is equal to 'Testanimation[self.anitrack]', this is then blitted onto the screen
'''
##Extras
'''
Most Small Extras have comments explaining their use, but the ones that haven't are located here:
Slice - Slice is the opening where the screen splits in two
'''

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

##Music/Ambience
AceK_theme = pygame.mixer.Sound("AceK_Theme.wav")
Base_music = pygame.mixer.Sound("Base Music.wav")
Base_music.play()

##Sound
KickSFX= pygame.mixer.Sound("KickImpact.wav")
Sword_draw = pygame.mixer.Sound("Sword draw.wav")
Sword_clash = pygame.mixer.Sound("Sword Clash.wav")
Footstep1 = pygame.mixer.Sound("Footstep1.wav")
Footstep2 = pygame.mixer.Sound("Footstep2.wav")
Gore_slash = pygame.mixer.Sound("Slashed SFX.wav")
Gold_tackleSFX = pygame.mixer.Sound("KKTackle SFX.wav")

##Static Images
Title = pygame.image.load("Title name.png")
Mousereticle = pygame.image.load("Reticle.png")
Big_plat = pygame.image.load("Bigplatform2.png")

SamuraiIMG = pygame.image.load("SamuraiTitle.png")
EnemiesIMG = pygame.image.load("EnemiesTitle.png")

DONTHITME = pygame.image.load("HITME.png")

Progress_bar_anim = pygame.image.load("Progress_bar.png")

Screen_slice1 = pygame.image.load("Sliced_screen_1.png")
Screen_slice2 = pygame.image.load("Sliced_screen_2.png")

##Bar animations
PKBar = [pygame.image.load("PKBar1.png"),pygame.image.load("PKBar2.png"),pygame.image.load("PKBar3.png"),pygame.image.load("PKBar4.png")]

##Animations

##KK is player
KKRun = [pygame.image.load("SamuraiSprint1.png"),pygame.image.load("SamuraiSprint2.png"),pygame.image.load("SamuraiSprint3.png"),pygame.image.load("SamuraiSprint4.png"),pygame.image.load("SamuraiSprint5.png"),pygame.image.load("SamuraiSprint6.png")]
KKFall = pygame.image.load("SamuraiFall3.png")
KKJump = pygame.image.load("SamuraiLeap.png")
KKSlash = [pygame.image.load("Samurairun1.png"),pygame.image.load("Samurairun2.png"),pygame.image.load("Samuraislash1.png"),pygame.image.load("Samuraislash2.png")]
KKCollapse = [pygame.image.load("SamuraiCollapse1.png"),pygame.image.load("SamuraiCollapse2.png"),pygame.image.load("SamuraiCollapse3.png"),pygame.image.load("SamuraiCollapse4.png"),pygame.image.load("SamuraiCollapse5.png")]
KKUnsheathe = [pygame.image.load("SamuraiUnsheathe13.png"),pygame.image.load("SamuraiUnsheathe12.png"),pygame.image.load("SamuraiUnsheathe11.png"),pygame.image.load("SamuraiUnsheathe10.png"),pygame.image.load("SamuraiUnsheathe8.png"),pygame.image.load("SamuraiUnsheathe7.png"),pygame.image.load("SamuraiUnsheathe9.png"),pygame.image.load("SamuraiUnsheathe6.png"),pygame.image.load("SamuraiUnsheathe5.png"),pygame.image.load("SamuraiUnsheathe4.png"),pygame.image.load("SamuraiUnsheathe3.png"),pygame.image.load("SamuraiUnsheathe1.png"),pygame.image.load("SamuraiUnsheathe2.png")]#,pygame.image.load("SamuraiUnsheathe14.png")]
KKDeathfall = pygame.image.load("Samuraiairfall.png")

KKBar = pygame.image.load("SamuraiBar.png")

Gold_knightRun = [pygame.image.load("KKRun1.png"),pygame.image.load("KKRun2.png"),pygame.image.load("KKRun3.png"),pygame.image.load("KKRun4.png"),pygame.image.load("KKRun5.png"),pygame.image.load("KKRun6.png")]
Gold_knightCharge = pygame.image.load("KKCharge1.png")
Gold_knightDead = pygame.image.load("KKDead.png")
Gold_knightTaunt = [pygame.image.load("KKTaunt1.png"),pygame.image.load("KKTaunt2.png"),pygame.image.load("KKTaunt3.png"),pygame.image.load("KKTaunt4.png"),pygame.image.load("KKTaunt5.png"),pygame.image.load("KKTaunt6.png")]

Spectre_idle = [pygame.image.load("Spectreidle1.png"),pygame.image.load("Spectreidle2.png"),pygame.image.load("Spectreidle3.png"),pygame.image.load("Spectreidle4.png")]
Spectre_slash = [pygame.image.load("Spectreswing1.png"),pygame.image.load("Spectreswing2.png"),pygame.image.load("Spectreswing3.png")]
Spectre_death = [pygame.image.load("Spectredeath1.png"),pygame.image.load("Spectredeath2.png"),pygame.image.load("Spectredeath3.png"),pygame.image.load("Spectredeath4.png"),pygame.image.load("Spectredeath5.png"),pygame.image.load("Spectredeath6.png"),pygame.image.load("Spectredeath7.png"),pygame.image.load("Spectredeath8.png")]

Baron_Downstrike = pygame.image.load("SKDown_strike.png")

Baron_propel = [pygame.image.load("SKPropel1.png"),pygame.image.load("SKPropel2.png"),pygame.image.load("SKPropel3.png"),pygame.image.load("SKPropel4.png")]

Baron_dead = pygame.image.load("SKDead.png")

Floater = [pygame.image.load("Rocketpad1.png"),pygame.image.load("Rocketpad2.png"),pygame.image.load("Rocketpad3.png")]

AceK_Float = [pygame.image.load("PKFloat1.png"),pygame.image.load("PKFloat2.png"),pygame.image.load("PKFloat3.png"),pygame.image.load("PKFloat4.png")]
AceK_Draw = [pygame.image.load("PKDraw18.png"),pygame.image.load("PKDraw1.png"),pygame.image.load("PKDraw2.png"),pygame.image.load("PKDraw3.png"),pygame.image.load("PKDraw4.png"),pygame.image.load("PKDraw5.png"),pygame.image.load("PKDraw6.png"),pygame.image.load("PKDraw7.png"),pygame.image.load("PKDraw8.png"),pygame.image.load("PKDraw9.png"),pygame.image.load("PKDraw10.png"),pygame.image.load("PKDraw11.png"),pygame.image.load("PKDraw12.png"),pygame.image.load("PKDraw13.png"),pygame.image.load("PKDraw14.png"),pygame.image.load("PKDraw15.png"),pygame.image.load("PKDraw16.png")]
AceK_Corkscrew = [pygame.image.load("PKCorkscrew1.png"),pygame.image.load("PKCorkscrew2.png"),pygame.image.load("PKCorkscrew3.png"),pygame.image.load("PKCorkscrew4.png"),pygame.image.load("PKCorkscrew5.png"),pygame.image.load("PKCorkscrew6.png"),pygame.image.load("PKCorkscrew7.png"),pygame.image.load("PKCorkscrew8.png")]
AceK_Lunge = [pygame.image.load("PKLunge1.png"),pygame.image.load("PKLunge2.png"),pygame.image.load("PKLunge3.png"),pygame.image.load("PKLunge4.png"),pygame.image.load("PKLunge5.png"),pygame.image.load("PKLunge6.png"),pygame.image.load("PKLunge7.png")]
AceK_Laugh = [pygame.image.load("PKLaugh1.png"),pygame.image.load("PKLaugh2.png"),pygame.image.load("PKLaugh3.png")]

Airshipflying = [pygame.image.load("Airship1.png"),pygame.image.load("Airship2.png"),pygame.image.load("Airship3.png"),pygame.image.load("Airship4.png"),pygame.image.load("Airship5.png"),pygame.image.load("Airship6.png")]

CannonballAnim = pygame.image.load("Cannon_ball.png")
             
##HMT - HatManTea
HMTRun = [pygame.image.load("HMTRun1.png"),pygame.image.load("HMTRun2.png"),pygame.image.load("HMTRun3.png"),pygame.image.load("HMTRun4.png"),pygame.image.load("HMTRun5.png"),pygame.image.load("HMTRun6.png")]
HMTDead = pygame.image.load("HMTDead.png")

##HM - HatMan
HMSprint = [pygame.image.load("Hatmanrun1.png"),pygame.image.load("Hatmanrun2.png"),pygame.image.load("Hatmanrun3.png"),pygame.image.load("Hatmanrun4.png"),pygame.image.load("Hatmanrun5.png"),pygame.image.load("Hatmanrun6.png")]
HMSlash = [pygame.image.load("HMAttack1.png"),pygame.image.load("HMAttack2.png"),pygame.image.load("HMAttack3.png"),pygame.image.load("HMAttack4.png"),pygame.image.load("HMAttack5.png")]
HMTaunt = [pygame.image.load("Hatmantaunt1.png"),pygame.image.load("Hatmantaunt2.png"),pygame.image.load("Hatmantaunt3.png"),pygame.image.load("Hatmantaunt4.png"),pygame.image.load("Hatmantaunt5.png")]


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
SPECTRE_FREQ = 7000
GOLDEN_FREQ = 3000
TEAMAN_FREQ = 8000
BARONDOWN_FREQ = 3000


Enemieson = True

##Score
Current_score = int(0)
HGH_SCR = open("HIGHSCR.txt","r")
while True:
    a = HGH_SCR.readline()
    print(a)
    if not a: break
    High_score = a
HGH_SCR.close()

##Misc
Gamebegun = False
GameSTART = False
textloc = WIDTH//30
Framecounter = 0
Ready = False
enemy_income_reset = False
clean_slate_income = False


##Bossfight
Boss_incoming = False
BOSS_BATTLE = False
Ready_for_boss = False
DRAW = False

Boss_movecount = 0
Boss_hp = 2
##Time UNTIL Boss, not lenght of boss fight
##This is in seconds
Boss_time = 45



##BG Stuff
BGshift = False
BGY_loc = 0        
    
        
##Player Related Timers
playerjump_time = 15
PLAYERJUMP_EVENT = pygame.USEREVENT+1

PLAYERINVFRAMES_EVENT = pygame.USEREVENT+30
playerinv_time = 1000
pygame.time.set_timer(PLAYERINVFRAMES_EVENT, playerinv_time)
PLAYERINVFRAMES = False

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

def Ace_Knight_move():
    global Boss_movecount
    global Boss_hp
    ##BOSS MOVE AMOUNT
    if Boss_hp !=0:
        if Boss_movecount < 4:
            ##It cannot be random.choice([x()]) or similar becuase methods are not subscriptable
            chooser = random.randint(1,2)
            if chooser == 1:
                AKC = Ace_Knight_Corkscrew()
                cork_group.add(AKC)
                ##Extra Movecount as kicks are technically 3 moves in one
                Boss_movecount +=1
            elif chooser == 2:
                AKC = Ace_Knight_Lunger()
                lunger_group.add(AKC)
            Boss_movecount +=1
        else:
            floatpod = Floatpod()
            all_sprites.add(floatpod)
            rocketplat.add(floatpod)
            AKC = Ace_Knight_Laugher()
            laugher_group.add(AKC)
            Boss_movecount = 0
    else: Boss_hp = 2
            
    all_sprites.add(AKC)
    enemies.add(AKC)

##This is so it either immediately removes the sprite, or plays the deah animation
##Positional argument either True or False
def Enemy_wipe(Death_anim):
    enemylist = pygame.sprite.Group.sprites(enemyprojectile_group)
    for number in range(len(enemylist)):
        enemylist[number].kill()
        
    if Death_anim == True:
        enemylist = pygame.sprite.Group.sprites(enemies)
        for number in range(len(enemylist)):
            enemylist[number].dead = True
    elif Death_anim == False:
        enemylist = pygame.sprite.Group.sprites(enemies)
        for number in range(len(enemylist)):
            enemylist[number].kill()

def Player_reset():
    player.dead = False
    player.deadframe_beenreset = False
    player.deadframes = 0
    player.rect.left = 350
    player.rolling = False
    player.rollframes = 0
    
##Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        ##170, 108
        ##118, 72
        self.image = pygame.Surface((170,108))
        self.rect = self.image.get_rect()
        self.rect.left= (350)
        self.rect.bottom= largeplatform1.rect.top+1
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

        self.rolling = False
        self.rollframes = 0
        self.sheathing = False

        self.FIGHTREADY = False


       
    def update(self):
        
        ##Relocation in opening
        if BGshift == True and Gamebegun == False:
            self.image.fill(GREEN)
            self.image.blit(KKUnsheathe[0],(0,0))
            self.rect.bottom = largeplatform1.rect.top+1

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
                    global BGspeed
                    global BaseBGspeed
                    global DRAW
                    global UntilStart
                    
                    if Ready == True and Boss_incoming == False:
                
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

                    ##BOSS PREPARATION
                    if Boss_incoming == True and BOSS_BATTLE == False:
                        self.speedx =0
                        self.speedy =0
                        if self.rect.left>250:
                            self.frame = KKRun[self.anitrack]
                            if self.frametracker > 2:
                                self.frametracker = -1
                                self.anitrack+=1
                            self.rect.x-=7
                            
                        elif self.sheathing == False:
                            self.sheathing = True
                            self.anitrack = 12
                            
                        elif self.anitrack != -1 and self.FIGHTREADY == False:
                            ##This if statement is to avoid constantly readjusting the rect
                            if self.anitrack == 12: 
                                self.image = pygame.Surface((170,108))
                                self.rect = self.image.get_rect()
                                self.image.set_colorkey(GREEN)
                                self.rect.left = (250)
                                self.rect.bottom= largeplatform1.rect.top+1
                            if self.rect.left:
                                BaseBGspeed = 0
                                BGspeed = 0
                                
                            self.frame = KKUnsheathe[self.anitrack]
                            if self.frametracker > 2:
                                self.frametracker = -1
                                self.anitrack-=1
                                if self.anitrack == 3: Sword_draw.play()
                                if self.anitrack == -1:
                                    self.FIGHTREADY = True
                                    self.anitrack = 0
                                
                        elif DRAW == True:
                            self.frame = KKUnsheathe[self.anitrack]
                            if self.frametracker > 2:
                                self.frametracker = -1
                                self.anitrack+=1
                                if self.anitrack == 3: Sword_draw.play()

                            
                                                      
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
                        self.ready_positiony = largeplatform1.rect.top
                        self.image = pygame.Surface((118, 72))
                        self.rect = self.image.get_rect()
                        self.image.set_colorkey(GREEN)
                        self.rect.left = (self.ready_positionx)
                        self.rect.bottom = self.ready_positiony
                        self.rect.x+=30
                        self.anitrack = 4
                        BaseBGspeed = 10

                        Ready = True
                        try:
                            ##Used for resetting
                            if Untilstart >0:
                                UntilStart = Untilstart + Seconds_elapsed - (UntilStart*1000)
                        except NameError:
                            UntilStart = pygame.time.get_ticks()

                    if DRAW == True:
                        DRAW = False
                        self.ready_positionx = self.rect.left
                        self.ready_positiony = largeplatform1.rect.top
                        self.image = pygame.Surface((118, 72))
                        self.rect = self.image.get_rect()
                        self.image.set_colorkey(GREEN)
                        self.rect.left = (self.ready_positionx)
                        self.rect.bottom = self.ready_positiony
                        self.rect.x+=30
                        self.anitrack = 4
                        BaseBGspeed = 10
##                    if self.slashing == True:
##                        self.slashing = False
##                        self.slashedframes = 0

            self.rect.x+=self.speedx
            if Playerjumping == False:
                self.rect.y+=self.speedy
            
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

            if self.slashing == False and Ready == True and self.dead == False and Boss_incoming == False:
                if keystate[pygame.K_a]:
                    self.speedx = -7
                if keystate[pygame.K_d]:
                    self.speedx = 8

            ##Roll code
            if self.rolling == True and not BGspeed <=1:
                self.rect.x-=8
                self.rollframes +=1

            ##Barrier
            if self.rect.left < 10:
                self.rect.left =10
            elif self.rect.right> WIDTH-10:
                self.rect.right = WIDTH-10

            
    def jump(self):
        self.speedy = -Playerjumpspeedvary
        self.rect.y += self.speedy

    def slash(self):
        if self.dead == False and Playerjumping == False and Playerfalling == False and self.slashing == False:

            self.anitrack = 0
            self.frametracker=0
            self.slashing = True

            
    ##Happens in death
    def roll(self):
        if self.rolling == False:
            self.rollframes = 0
            self.rolling = True
        
##Enemies

class Spectre(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((322,168))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0,player.rect.left)
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
            self.speedx = 4
        elif player.rect.centerx<self.rect.right-100:
            self.speedx = -2
        else:
            self.speedx = 0

        if player.dead == False:
            if player.rect.centery<self.rect.centery-2:
                self.speedy = -2
            elif player.rect.centery>self.rect.centery+2:
                self.speedy = 3
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
        
class Hatman(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((160,150))
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.bottom =  largeplatform1.rect.top 
        self.image.set_colorkey(GREEN)
        self.speedx = 0
        self.speedy = 0
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = HMSprint[0]
        self.image.blit(self.frame,(0,0))
        ##Self.frame means current animation frame

        self.dead = False
        self.speedx = 0
        self.speedy = 0
        self.playerfound = False
        self.slashing = False
        self.killing = False

        ##Helps to lock last frame with ease
        self.framelock = False



    def update(self):
        self.frametracker += 1
        if self.frametracker>60: self.frametracker=0
        try:

            if self.frametracker > 2 and self.slashing == True:
                if self.anitrack == 1: self.killing = True
                self.frame = HMSlash[self.anitrack]
                self.anitrack +=1
                self.frametracker =-1

            elif self.frametracker >3 and player.dead == True:
                self.frame = HMTaunt[self.anitrack]
                self.frametracker =-1
                ##This freezes it on the final frame of the salute
                if self.anitrack != len(HMTaunt)-1: self.anitrack+=1

            elif self.frametracker >3 and self.slashing == False:
                
                self.frame = HMSprint[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1

        except IndexError:
            self.anitrack = 0
            if player.dead == True:
                if self.slashing == True:
                    self.slashing = False
                    self.anitrack = 0


        ##Coding this part was absolutey horrible, please reuse and dont try to reinvent
        if self.playerfound == False and self.framelock==False:
            if self.rect.left< player.rect.left and self.rect.right-80 > player.rect.left :
                self.speedx = 0
                self.playerfound = True
                self.anitrack = 0
                self.frametrack = -1
            
            else: self.speedx = 16
        else:
            self.speedx = player.speedx
            self.speedy = player.speedy

        if self.framelock == False and self.playerfound == True and player.rect.bottom>self.rect.top and self.slashing == False:
            self.slashing = True
            self.framelock = True

        if BOSS_BATTLE == True or Boss_incoming == True:
            self.kill()

        self.image.fill(GREEN)
        self.image.blit(self.frame,(0,0))
        self.rect.x+=self.speedx

        ##Collision Located here to solve Unidentified Name error
        hits = pygame.sprite.spritecollide(self,player_group,False)
        if hits:
            if self.killing == True:
                player.dead = True
                self.killing = False
                Gore_slash.play()

        
class Donthitme(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((140,140))
        self.rect = self.image.get_rect()
        self.rect.centerx = TM.rect.centerx-25
        self.rect.bottom= TM.rect.top + 40
        self.image.blit(DONTHITME,(0,0))
        self.image.set_colorkey(GREEN)
        

    def update(self):
        self.rect.x = TM.rect.centerx-25
        self.rect.bottom = TM.rect.top + 40

        if self.rect.left>WIDTH or self.rect.top>largeplatform1.rect.top: self.kill()
        

    
class Hatman_tea(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((112,92))
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.bottom= largeplatform1.rect.top
        self.image.set_colorkey(GREEN)
        self.speedx = 0
        self.speedy = 0
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = HMTRun[1]
        ##Self.frame means current animation frame

        self.dead = False
        self.speedx = 6
        self.speedy = 0

        self.image.fill(GREEN)

    def update(self):
        self.frametracker += 1
        if self.frametracker>60: self.frametracker=0
        try:
            if self.frametracker >3 and self.dead == False:
                
                self.frame = HMTRun[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1

        except IndexError:
            self.anitrack = 0

        if self.dead == True:
            self.frame = HMTDead
            self.speedx = -2
            self.speedy = 4
        self.image.blit(self.frame,(0,0))


        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.left>WIDTH:self.kill()
        
        if self.rect.top>HEIGHT:
            HMSoldier = Hatman()
            enemies.add(HMSoldier)
            hatman_group.add(HMSoldier)
            all_sprites.add(HMSoldier)
            self.kill()
            
class Baron_Downstriker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((56,96))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.bottom= 0
        self.image.set_colorkey(GREEN)
        
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.image.blit(Baron_Downstrike,(0,0))
        ##Self.frame means current animation frame
        self.deadthsetup = False
        self.dead = False
        self.speedx = 0
        self.speedy = 12

    def update(self):
        ##Slight X movement detector
        if self.rect.centerx>player.rect.centerx:
            self.rect.x-=2
        elif self.rect.centerx<player.rect.centerx:
            self.rect.x+=2
        self.rect.y +=self.speedy
        if self.rect.top>HEIGHT: self.kill()
        if self.dead == True:
            if self.deadthsetup == False:
                self.oldposx = self.rect.left
                self.oldposy = self.rect.top
                self.image.fill(GREEN)
                self.image = pygame.Surface((70,78))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(GREEN)
                self.image.blit(Baron_dead,(0,0))
                self.rect.left = self.oldposx
                self.rect.top = self.oldposy
                self.deadthsetup = True
            self.rect.y+=3

        

class Baron_Sidestriker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ##1 - Spawn Left
        ##2 - Spawn Right
        self.sidespawn = random.choice([1,2])
        
        self.image = pygame.Surface((112,56))
        self.rect = self.image.get_rect()
        if self.sidespawn == 1:
            self.rect.right = 0
            self.speedx = 8
        else:
            self.rect.left = WIDTH
            self.speedx = -8
        self.rect.centery = player.rect.centery
        self.image.set_colorkey(GREEN)
        
        ##Frametracker counts the frames, it is used for animations
        self.frametracker = 0
        self.anitrack = 0
        self.frame = Baron_propel[0]
        ##Self.frame means current animation frame

        self.dead = False
        self.deadthsetup = False
        
        self.speedy = 0

    def update(self):
        self.frametracker += 1
        if self.frametracker>60: self.frametracker=0
        try:
            if self.frametracker >2 and self.dead == False:
                self.frame = Baron_propel[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1
            elif self.dead == True:
                if self.deadthsetup == False:
                    self.oldposx = self.rect.left
                    self.oldposy = self.rect.top
                    self.image = pygame.Surface((70,78))
                    self.rect = self.image.get_rect()
                    self.image.set_colorkey(GREEN)
                    self.deadthsetup = True
                    self.rect.left = self.oldposx
                    self.rect.top = self.oldposy
                self.image.blit(Baron_dead,(0,0))
                self.rect.y+=3
                

                
        except IndexError:
            self.anitrack = 0
        
        self.rect.x +=self.speedx
        self.image.fill(GREEN)
        
        if self.sidespawn == 2:
            self.image.blit(Flipx(self.frame),(0,0))
        else:
            self.image.blit(self.frame,(0,0))
        if self.rect.top>HEIGHT: self.kill()
       
class Golden_knight(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((104,80))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom= largeplatform1.rect.top
        self.image.set_colorkey(GREEN)
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
        self.dirflip = False

        
        
    def update(self):
        self.frametracker += 1
        if self.frametracker>60: self.frametracker=0
        self.speedx = BGspeed*-1 
        try:
            if self.frametracker >1 and self.dead == False and player.dead == False:
                self.frame = Gold_knightRun[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1
            elif self.frametracker >2 and self.dead == False:
                if self.taunting == False:
                    self.taunting = True
                    
                    self.ready_positionx = self.rect.left
                    self.ready_positiony = self.rect.bottom
                    self.image = pygame.Surface((90,88))
                    self.rect = self.image.get_rect()
                    self.image.set_colorkey(GREEN)
                    self.rect.left = self.ready_positionx
                    self.rect.bottom = self.ready_positiony
                    
                self.frame = Gold_knightTaunt[self.anitrack]
                self.anitrack +=1
                self.frametracker = -1
        except IndexError:
            self.anitrack = 0


        if player.dead == False and self.rect.x+300 > player.rect.left and  player.rect.left > self.rect.right-300:
            self.frame = Gold_knightCharge
            self.charging = True
        else:
            self.charging = False
            

        self.image.blit(Flipx(self.frame),(0,0))
        
        if self.dead == True and self.rect.top > largeplatform1.rect.top: self.kill()
        if self.rect.right<0: self.kill()
        
        if self.dead == True:
            self.image.blit(Gold_knightDead,(0,0))
            self.rect.y+=3
            self.rect.x+=self.speedx
            
        elif player.dead == False:
            self.rect.x +=self.speedx - 10
            self.rect.y +=self.speedy

        elif player.dead == True:
            self.rect.x+=self.speedx
        
##PROPELLER KNIGHT BOSS SPRITES
class Cannonball(pygame.sprite.Sprite):

    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((72,72))
        self.rect = self.image.get_rect()
        self.rect.centerx = player.rect.centerx
        self.rect.bottom= 0 -x
        self.image.set_colorkey(GREEN)
        self.xoffset = x
        
        ##Frametracker counts the frames, it is used for animations
        self.image.blit(CannonballAnim,(0,0))
        ##Self.frame means current animation frame

        self.dead = False
        self.speedx = 0
        self.speedy = 9

    def update(self):
        if self.rect.bottom<0:
            self.rect.centerx = player.rect.centerx
        ##Slight X movement detector
        if self.rect.top>HEIGHT:
            if BOSS_BATTLE == True:
                CB = Cannonball(self.xoffset)
                all_sprites.add(CB)
                
                enemyprojectile_group.add(CB)
            self.kill()
        self.rect.y+=self.speedy
            
        
class Floatpod(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((192,84))
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.top = 300
        self.speedx = 4
        self.speedy = 0
        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = Floater[0]

    def update(self):
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0

        try:
            if self.frametracker>3:
                self.frame = Floater[self.anitrack]
                self.anitrack+=1
                self.frametracker =-1
        except IndexError:
            self.anitrack = 0

        if self.rect.left>WIDTH: self.kill()
        self.rect.x+=self.speedx
        self.image.blit(self.frame,(0,0))
        
            

        
class Air_ship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((206,136))
        self.rect = self.image.get_rect()
        self.rect.right = 0
        self.rect.centery = HEIGHT//2
        self.speedx = 0
        self.speedy = 0
        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = Airshipflying[0]
        self.random_movement = False

    def update(self):

        if self.frametracker>FPS:
            self.frametracker = 0
        else: self.frametracker +=1
        
        try:

            if BOSS_BATTLE == False and Boss_incoming == False:
                self.rect.x-=7
                self.rect.y+=5
                if self.rect.left>WIDTH: self.kill()
            elif self.random_movement == True:
                
                self.rect.x+=6
                if self.rect.left>WIDTH: self.rect.right = 0

            elif self.rect.centerx<WIDTH//2 and self.random_movement == False:
                self.rect.x +=10
                self.random_movement = False
            elif self.rect.centerx>=WIDTH//2 and self.random_movement == False:
                self.random_movement = True
                
            if self.frametracker>4:
                self.frame = Airshipflying[self.anitrack]
                self.anitrack+=1
                self.frametracker = -1
        
                
                    
        except IndexError:
            self.anitrack = 0

        self.image.blit(self.frame,(0,0))
        
        
##Intro Class, not fight class
class Ace_Knight(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#
        self.image = pygame.Surface((190,120))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom = largeplatform1.rect.top +4
        self.speedx = 0
        self.speedy = 0
        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = AceK_Draw[0]
        self.dead = False
        self.FIGHTREADY = False
        
    def update(self):
        global BOSS_BATTLE
        global BGspeed
        global DRAW
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0
        try:

            if BOSS_BATTLE == True:
                self.frame = AceK_Float[self.anitrack]
                self.anitrack+=1
                self.frametracker = -1
                self.rect.y-=10
                self.rect.x-=3
                
            elif BOSS_BATTLE == False and self.rect.left>WIDTH-350:
                self.rect.x-=10

            elif BOSS_BATTLE == False:
                self.FIGHTREADY = True
                if self.frametracker >1 and player.rect.left<=250 and DRAW ==True:
                    self.frame = AceK_Draw[self.anitrack]
                    self.anitrack +=1
                    self.frametracker = -1

            if self.rect.bottom<0:
                Ace_Knight_move()
                self.kill()

                    
        except IndexError:
            self.anitrack = 0
            if BOSS_BATTLE == False:
                self.rect.x-=50
                ##Increasing the anitrack causes a player error, adjusting the rect sooner
                player.anitrack = 50
                BOSS_BATTLE = True
                Boss_incoming = False
                
        self.image.fill(GREEN)      
        if player.rect.centerx<self.rect.centerx: self.image.blit(Flipx(self.frame),(0,0))
        else: self.image.blit(self.frame,(0,0))


##BOSS MOVES
class Ace_Knight_Corkscrew(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dir = random.choice([-1,1])
        ##0 is spawn left, 1 is right
        self.image = pygame.Surface((80,104))
        self.rect = self.image.get_rect()
        if self.dir == -1:
            self.rect.centerx = player.rect.left - 500
            self.rect.centery = player.rect.centery -600
        else:
            self.rect.centerx = player.rect.right+ 500
            self.rect.centery = player.rect.centery -600
        ##Movement must be in 5 to 6 (or 7) ratio
        if self.dir==-1:
            self.speedx = 10
        else:
            self.speedx = -10
        self.speedy = 14

        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = AceK_Corkscrew[0]
        self.dead = False
        ##If kicks is greater than 3, the move ends
        self.kicks = 0

    def update(self):
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0
        try:
            if self.frametracker>3:
                self.frame = AceK_Corkscrew[self.anitrack]
                self.anitrack+=1
                self.frametracker = -1

            
                    
        except IndexError:
            self.anitrack = 0
        if self.rect.top>HEIGHT:
            if self.kicks==2:
                Ace_Knight_move()
                self.kill()
            else: self.kicks+=1
            self.dir*=-1
            if self.dir == -1:
                self.rect.centerx = player.rect.left - 400
                self.rect.centery = player.rect.centery -700
                self.speedx = 10
            else:
                self.rect.centerx = player.rect.right+ 400
                self.rect.centery = player.rect.centery -700
                self.speedx = -10
                
        self.image.fill(GREEN)
        
        ##if player.rect.centerx<self.rect.centerx: self.image.blit(Flipx(self.frame),(0,0))
        if self.dir == -1: self.image.blit(self.frame,(0,0))
        else: self.image.blit(Flipx(self.frame),(0,0))


        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        
class Ace_Knight_Lunger(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#
        self.image = pygame.Surface((190,120))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.bottom = largeplatform1.rect.top +2
        self.speedx = -4
        self.speedy = 0
        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = AceK_Lunge[3]
        self.dead = False
        self.FIGHTREADY = False
        self.lunging = False
        self.movetime = 750
        self.now = pygame.time.get_ticks()

    def update(self):
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0
        try:
            if self.lunging == True:
                
                if self.frametracker>1 and self.anitrack<5:
                    self.frame = AceK_Lunge[self.anitrack]
                    self.anitrack+=1
                    self.frametracker = -1
                elif self.frametracker>1:
                    self.frame = AceK_Lunge[4]
                self.speedx-=1.5
            elif pygame.time.get_ticks()>(self.now+self.movetime):
                self.lunging = True
                    
        except IndexError:
            self.anitrack = 0

        if self.rect.right<0:
            Ace_Knight_move()
            self.kill()
            

        self.rect.x +=self.speedx
        self.rect.y +=self.speedy
                
        self.image.fill(GREEN)      
        self.image.blit(Flipx(self.frame),(0,0))

##Meant to be Laugher, not laughter
class Ace_Knight_Laugher(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#
        self.image = pygame.Surface((190,120))
        self.rect = self.image.get_rect()
        self.rect.centerx = +5
        self.rect.bottom = 310
        self.speedx = 4
        self.speedy = 0
        self.image.set_colorkey(GREEN)
        self.frametracker = 0
        self.anitrack = 0
        self.frame = AceK_Lunge[3]
        self.dead = False
        self.FIGHTREADY = False
        self.lunging = False
        self.movetime = 750
        self.hp = Boss_hp
        self.now = pygame.time.get_ticks()
        self.image.fill(GREEN)
        ##Killing Cannon Balls
        enemylist = pygame.sprite.Group.sprites(enemyprojectile_group)
        for number in range(len(enemylist)):
            enemylist[number].kill()

    def update(self):
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0
        try:
            if self.frametracker>4:
                self.frame = AceK_Laugh[self.anitrack]
                self.anitrack+=1
                self.frametracker = -1                   
        except IndexError:
            self.anitrack = 1

        if self.dead == True:
            ##Rudimentary lock out
            if self.rect.bottom == 310:
                self.hp = Boss_hp -1
            ##First frame is a falling frame for efficiency
            self.frame = AceK_Laugh[0]
            self.rect.y+=8

        if self.rect.left>WIDTH or self.rect.top>HEIGHT:

            ##Adding cannon balls
            for number in range(2):
                ##number is Y differential
                ##+1 so isn't zero
                CB = Cannonball((number+1)*200)

                all_sprites.add(CB)
                enemyprojectile_group.add(CB)
            if Boss_hp>0:
                Ace_Knight_move()
            self.kill()
        self.rect.x += 4
        self.image.blit(self.frame,(0,0))
        
    
##HUD
class Ace_Knight_Bar(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((182,100))
        self.rect = self.image.get_rect()
        self.anitrack = 0
        self.frametracker = 0
        self.image.set_colorkey(GREEN)
        self.rect.centery = PL.rect.centery-10
        self.rect.centerx = PL.rect.right+40
        self.frame = PKBar[0]

    def update(self):
        self.frametracker+=1
        if self.frametracker>FPS:
            self.frametracker = 0

        try:
            if self.frametracker>10:
                self.frame = PKBar[self.anitrack]
                self.anitrack+=1
                self.frametracker = -1

        except IndexError: self.anitrack = 0

        self.image.fill(GREEN)
        self.image.blit(self.frame,(0,0))

class Progress_Line(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((510,31))
        self.rect = self.image.get_rect()
        self.anitrack = 0
        self.frametracker = 0
        self.rect.centery = 65
        self.rect.right = 990
        self.image.blit(Progress_bar_anim,(0,0))

class Progress_Line_Filler(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((0,15))
        self.rect = self.image.get_rect()
        self.anitrack = 0
        self.frametracker = 0
        self.rect.centery = 70
        self.rect.right = 1000
        self.image.fill(RED)

    def update(self):
        X_len = PS.rect.centerx-500
        self.image = pygame.Surface((X_len,21))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.rect.centery = PL.rect.centery
        self.rect.right = PS.rect.centerx+10

class Progress_Samurai(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((34,30))
        self.rect = self.image.get_rect()
        self.rect.centery = PL.rect.centery-5
        self.rect.right = 550
        self.image.blit(KKBar,(0,0))
        self.image.set_colorkey(GREEN)
        self.BOSS_BATTLE_SIGNAL = False
        self.frametracker = 0
        
        ##Calculated incase of changing boss time, this figures out the distance to make it smooth
        ##440 is length, Boss_time is time
        
        self.movedistance = 450//Boss_time

    def update(self):
        ##Divided by eight forsmoother movement, updated more, moves less, same output
        if Ready == True and player.dead == False:
            self.frametracker+=1
            if self.frametracker>(FPS//7):
                self.frametracker = 1
                if self.rect.centerx<1000:
                    self.rect.x+=self.movedistance//7
            elif self.rect.centerx>=1000:
                if self.BOSS_BATTLE_SIGNAL == False:
                    self.BOSS_BATTLE_SIGNAL = True
                
##Reset Sprite
class Reset_Slate(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500,900))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = HEIGHT
        self.speedx = 0
        ##Speedy MUST be a factor of 900
        self.speedy = -45
        self.image.fill(BLACK)
        self.reset = False

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top == 0: self.reset = True
        else: self.reset = False
            
        
        
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

        ##108 is player height, so player's head doesnt stick out at start
        self.rect.top = HEIGHT + 108
        self.speedx = 0
        self.speedy = 0
        self.image.blit(Big_plat,(0,0))
##        self.image.fill(WHITE)

    def update(self):
        global Gamebegun
        global BGspeed
        global BaseBGspeed
        if player.dead == True:
            if GAMEFRAME % 30 == 0:
                if BGspeed > 0:
                    BGspeed-=2
                else:
                    BGspeed = 0
            
        ##Movement                    
        elif player.speedx == 8 and BGspeed == BaseBGspeed:
            BGspeed +=6
        elif player.speedx == -6 and BGspeed == BaseBGspeed:
            BGspeed -=4
        else:
            BGspeed = BaseBGspeed

    
        if BGshift == True and self.rect.y>(Baseplatformposy):
            self.rect.y-=4
            
        elif Gamebegun == False and self.rect.y <= Baseplatformposy:
            Gamebegun = True
            platforms.add(smallplatform1)

        if BGspeed<0:
            BGspeed = 0
            
        if Ready == True:
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

##OPENING
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
        

class Left_slice(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500,900))
        self.image.set_colorkey(GREEN)
        self.image.blit(Screen_slice2,(0,0))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = HEIGHT

    def update(self):
        self.rect.x+=15
        if self.rect.left>WIDTH: self.kill()

class Right_slice(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500,900))
        self.image.set_colorkey(GREEN)
        self.image.blit(Screen_slice1,(0,0))
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT
        
    def update(self):
        self.rect.x-=15
        if self.rect.right<0: self.kill()


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
teaman_group = pygame.sprite.Group()
hatman_group = pygame.sprite.Group()
baron_group = pygame.sprite.Group()
enemyprojectile_group = pygame.sprite.Group()
cork_group = pygame.sprite.Group()
lunger_group =  pygame.sprite.Group()
laugher_group =  pygame.sprite.Group()
rocketplat = pygame.sprite.Group()
HUD = pygame.sprite.Group()
reset_group = pygame.sprite.Group()
slice = pygame.sprite.Group()

##Sprite Declaration
largeplatform1 = LargePlatform(1)
largeplatform2 = LargePlatform(2)
largeplatform3 = LargePlatform(3)
player = Player()
portrait = Portrait()
enemies_portrait = Enemies_Portrait()
baseparticle = Baseparticle()
PL = Progress_Line()
PS = Progress_Samurai()
AKB = Ace_Knight_Bar()
PLF = Progress_Line_Filler()

LSlice = Left_slice()
RSlice = Right_slice()

##Small Platform Delcarations
smallplatform1 = SmallPlatform(XMiddle,HEIGHT-400 ,300)
smallplatform2 = SmallPlatform(XMiddle,HEIGHT-650 ,150)

##Sprite Adding

opening.add(portrait)
opening.add(enemies_portrait)

slice.add(LSlice)
slice.add(RSlice)

##all_sprites.add(basicenemies)

HUD.add(PL)
HUD.add(PLF)
HUD.add(PS)
HUD.add(AKB)
all_sprites.add(HUD)



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

##Teaman Timer
teaman_timer = 0
now6 = pygame.time.get_ticks()

##Baron_down Timer
barondown_timer = 0
now7 = pygame.time.get_ticks()

nowlist = [now3,now4,now5,now6,now7]

##Setting Timers w/ USEREVENTS
pygame.time.set_timer(PLAYERJUMP_EVENT, playerjump_time)
PLAYERJUMP_EVENT = False
pygame.time.set_timer(TYPING, typing_speed)
pygame.time.set_timer(SLOWTYPING, slowtyping_speed)

##Time Variables
Seconds_elapsed = 0
GAMEFRAME = 0
Timervarier = random.choice([-500,-250,0,250,500])

## Game Loop ##


running = True
while running:

        
    ##In running loop so it constantly changes
    Timervarier = 0
    
    GAMEFRAME +=1
    if GAMEFRAME>FPS:
        GAMEFRAME = 0
    clock.tick(FPS)
    if Framecounter!=FPS:
        Framecounter+=1
    else:
        Seconds_elapsed +=1

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

            if event.key == pygame.K_b:
                PS.rect.centerx = 1001
                
            if event.key == pygame.K_SPACE:
                if Gamebegun == False and BGshift == False:
                    BGshift = True
                    
                    platforms.add(largeplatform1)
                    platforms.add(largeplatform2)
                    platforms.add(largeplatform3)
                    largeplats.add(platforms)
                    smallplats.add(smallplatform1)
                    smallplats.add(smallplatform2)
                    all_sprites.add(player)
                    player_group.add(player)

                elif player.dead == False:
                    player.slash()

                elif player.dead == True:
                    RS = Reset_Slate()
                    reset_group.add(RS)
                    
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
            
            Typed = False
            charactertyped += 1

        if event.type == PLAYERINVFRAMES_EVENT:
            PlayerINV = False
        

    ##Baseparticle Spawn Timer
    if Baseparticleon == True:
        particlesize = random.randint(1,2)
        particle_timer = pygame.time.get_ticks() - now3
        if particle_timer >= PARTICLE_FREQ:
            now3 = pygame.time.get_ticks()
            for number in range(particlesize):
                bp = Baseparticle()
                particles.add(bp)
                all_sprites.add(bp)

    ##Enemy Spawning
    if player.dead == False and Ready == True and BOSS_BATTLE == False and Boss_incoming ==False:
        
        ##Golden Knight spawn Timer
        if Enemieson == True and UntilStart+2000<pygame.time.get_ticks():
            golden_timer = pygame.time.get_ticks() - now4- Timervarier
            if golden_timer >= GOLDEN_FREQ:
                now4 = pygame.time.get_ticks()
                GK = Golden_knight()
                enemies.add(GK)
                all_sprites.add(GK)
                gold_group.add(GK)
                
        ##Teaman spawn Timer
        if Enemieson == True and UntilStart+8000<pygame.time.get_ticks():
            teaman_timer = pygame.time.get_ticks() - now6 - Timervarier
            if teaman_timer >= TEAMAN_FREQ:
                now6 = pygame.time.get_ticks()
                TM = Hatman_tea()
                enemies.add(TM)
                all_sprites.add(TM)
                teaman_group.add(TM)
                DHM = Donthitme()
                all_sprites.add(DHM)
                ##Added to enemies so it is killed in reset
                enemies.add(DHM)

        ##Barondown spawn Timer
        if Enemieson == True and UntilStart+1000<pygame.time.get_ticks():
            barondown_timer = pygame.time.get_ticks() - now7 - Timervarier
            if barondown_timer >= BARONDOWN_FREQ:
                now7 = pygame.time.get_ticks()
                ##Random for either Baron Sidestrike or Baron Downstrike
                BD = random.choice([Baron_Downstriker(),Baron_Sidestriker()])
                enemies.add(BD)
                all_sprites.add(BD)
                baron_group.add(BD)


        ##Spectre spawn Timer
        ##So enemies don't spawn immediately, i added the until start timer
        if Enemieson == True and Ready == True and UntilStart+6000<pygame.time.get_ticks():
            spectre_timer = pygame.time.get_ticks() - now5 - Timervarier
            try: ##Checking whether the spectre is dead or not is inconsequential (On the first time), we are actually looking for a name error to prove his existence
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

                            
    
    ##Misc
    ##Death reset

    try:
        if RS.reset == True:
            ##Screen Clear
            Enemy_wipe(False)
            
            ##Resetting progress
            PS.rect.left = 500
            if BOSS_BATTLE == True:
                PS = Progress_Samurai()
                all_sprites.add(PS)
                HUD.add(PS)

                ##Killing AKB so it remains on top
                AKB.kill()
                HUD.add(AKB)
                all_sprites.add(AKB)

            ##Resetting Timers
            UntilStart = pygame.time.get_ticks()

            ##Resetting Player Values
            Player_reset()

            ##Score reset
            Current_score = 0

            ##Boss Reset + Music Switch
            if BOSS_BATTLE == True or Boss_incoming == True:
                Boss_incoming = False
                BOSS_BATTLE = False
                AceK_theme.stop()
                Base_music.play()

            ##Killing Airship becuase its a bit different (not in enemy group)
            AS.kill()    

    except NameError: pass
    
    ##Boss Battle
    if PS.BOSS_BATTLE_SIGNAL == True and Boss_incoming == False and player.dead == False:
        Boss_incoming = True
        PS.BOSS_BATTLE_SIGNAL = False
        PS.kill()
        
    if BOSS_BATTLE == True:
        if Boss_incoming == True:
            for number in range(1):
                ##number is Y differential
                ##+1 so isn't zero
                CB = Cannonball((number+1)*200)
                
                all_sprites.add(CB)
                enemyprojectile_group.add(CB)
            Boss_incoming = False
    if Boss_incoming == True and BOSS_BATTLE == False:
        if Ready_for_boss == False:

            Base_music.stop()
            AceK_theme.play()            

            ##Initialising Airship
            AS = Air_ship()
            all_sprites.add(AS)

            
            
            Enemy_wipe(True)
            Ready_for_boss = True
            AK = Ace_Knight()
            all_sprites.add(AK)
            Until_draw = pygame.time.get_ticks()
        
        if player.FIGHTREADY == True and AK.FIGHTREADY == True and Until_draw+3000<pygame.time.get_ticks():
            DRAW = True

    ##This is needed, as due to the real AKC being declared in a function, the real AKC variable is not global, so we are seeking it out
    if BOSS_BATTLE == True:
        try:
            enemylist = pygame.sprite.Group.sprites(laugher_group)
            if len(enemylist)>0:
                AKC = enemylist[0]
                Boss_hp = AKC.hp
                if AKC.hp == 0:
                    Base_music.play()
                    AceK_theme.stop()
                    
                    ##BOSS DEATH
                    
                    BOSS_BATTLE = False
                    Boss_incoming  = False
                    Enemy_income_reset = True
                    
                    ##Killing JUST Cannon Balls
                    enemylist = pygame.sprite.Group.sprites(enemyprojectile_group)
                    for number in range(len(enemylist)):
                        enemylist[number].kill()

                    ##This resets all enemy timers, or else they all spawn immediately
                    UntilStart = pygame.time.get_ticks()

                    ##Resetting Progress
                    PS = Progress_Samurai()
                    all_sprites.add(PS)
                    HUD.add(PS)

                    ##Killing AKB so it remains on top
                    AKB.kill()
                    HUD.add(AKB)
                    all_sprites.add(AKB)
                    
        except NameError: pass
        except AttributeError: pass
    
    ##Collisions
    ##if x.rect.left>player.rect.centerx-30 is used for more accurate collisions
            
    hits = pygame.sprite.spritecollide(player, platforms, False)

    if hits:
        GameSTART = True
        Playerfalling  = False
        
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
            if GK.rect.left>player.rect.centerx-30:
                GK.dead = True
                Sword_clash.play()
        else:
            if player.dead == False:
                player.roll()
                Gold_tackleSFX.play()
            player.dead = True

    hits = pygame.sprite.groupcollide(teaman_group,player_group,False,False)
    if hits:
        if player.killing == True:
            if TM.rect.left>player.rect.centerx-30:
                if TM.dead == False: Sword_clash.play()
                TM.dead = True
            
    hits = pygame.sprite.groupcollide(spec_group,player_group,False,False)
    if hits:
        if SP.dead == True:
            pass
        elif player.killing == True:
            if SP.rect.left>player.rect.centerx-90:
                SP.dead = True
                Sword_clash.play()
        elif SP.killing == True:
            if player.dead == False:
                ##Jumping added for dramatic death
                PLAYERJUMP_EVENT = pygame.USEREVENT+1
                Gore_slash.play()
            player.dead = True

    hits = pygame.sprite.groupcollide(baron_group,player_group,False,False)
    if hits:
        if BD.dead == True:
            pass
        elif player.killing == True:
            if BD.rect.left>player.rect.left-20:
                BD.dead = True
                Sword_clash.play()
        else:
            if player.dead == False:
                if player.rect.centerx<BD.rect.centerx+20 and player.rect.centerx>BD.rect.centerx-20:
                    Gore_slash.play()
                    player.dead = True

    hits = pygame.sprite.groupcollide(enemyprojectile_group,player_group,False,False)

    if hits:
        player.roll()
        player.dead = True

    hits = pygame.sprite.groupcollide(rocketplat,player_group,False,False)

    if hits:
        if Playerjumping == False:
            Playerfalling = False
            player.rect.x+=4
            ##308 so it appears to be on top of rocketplat, but doesnt trigger falling
            player.rect.bottom = 308

    hits = pygame.sprite.groupcollide(cork_group,player_group,False,False)
    if hits:
        if player.dead == False:
            player.roll()
            KickSFX.play()
            player.dead = True

    hits = pygame.sprite.groupcollide(lunger_group,player_group,False,False)
    if hits:
        if player.dead == False:
            player.roll()
            Gore_slash.play()
            player.dead = True

    hits = pygame.sprite.groupcollide(laugher_group,player_group,False,False)
    if hits:
        if player.killing == True and AKC.dead == False:
            AKC.dead = True
            Gore_slash.play()
            
    ##Primary collision to stop falling, correction within the class itself
        
    ## 2)Update

    all_sprites.update()
    slice.update()
    platforms.update()

    
    if BGshift == False and Gamebegun == False:
        opening.update()
        
    reset_group.update()
        

    ## 3)Text sorting + Score
    
    TitleMessage = "Press Space To Start"
    Gameover_message = "Press Space To Try Again!"



    HIGHSCR_FILE = open("HIGHSCR.txt","r")
    while True:   
        a = HIGHSCR_FILE.readline()
        if not a: break
        High_score = int(a)

    HIGHSCR_FILE.close()

    if Ready == True and Boss_incoming == False:
        Current_score += BGspeed
        ##So player gets more points during Boss Battles
        if BOSS_BATTLE == True:
            Current_score+=BGspeed
        
    if Current_score>int(High_score):
        HIGHSCR_FILE = open("HIGHSCR.txt","w")
        HIGHSCR_FILE.write(str(Current_score))
        HIGHSCR_FILE.close()

    ##Divided by 10 so it makes more sense it meters
    Score_typed = FONT.render("Current Distance: "+str(Current_score//10)+"m",False,(WHITE))
    High_score_typed = FONT.render("Furthest Distance: "+str(High_score//10)+"m",False,(WHITE)) 


    
    ## 4)Render
    ##screen.fill(BLACK)
    if BGshift == True:
        BGY_loc -=2
        
        if BGY_loc == -200:
            
            BGshift = False
            Gamebegun == True
    screen.blit(Background,(-250,BGY_loc))
    
    if Gamebegun == False:
        ##The title shares BGY_loc as it has movement when the game starts, useful as i wanted the title card to do this to
        screen.blit(Title,(425,(BGY_loc*4)+290))
        particles.draw(screen)

    ##TYPING
    if Typed == False and Gamebegun == False:
        TypingMessage  = TitleMessage
        characters = str(TitleMessage[:charactertyped])
        if len(characters) != TypingMessage:
            Typed = True

    elif Typed == False and player.dead == True:
        TypingMessage  = Gameover_message
        characters = str(TypingMessage[:charactertyped])
        Typed = True

    elif Typed ==False and Gamebegun != False and player.dead == False:
        charactertyped = 0

    TitleMessageTyped= TITLEFONT.render(characters,False,WHITE)
    Gameover_messageTyped= TITLEFONT.render(characters,False,WHITE)

    if Gamebegun == True:
        all_sprites.draw(screen)
        particles.draw(screen)

    elif BGshift == False and Gamebegun == False:
        opening.draw(screen)


    
        screen.blit(Mousereticle,(mx-Mousereticle.get_width()//2,my - Mousereticle.get_height()//2))

        ##Key Rendering
    ##Platforms + Player always in front (sparing HUD)
    player_group.draw(screen)
    platforms.draw(screen)
    

    if Gamebegun == False and BGshift == False:
        AuthorMessage = FONT.render("By Tyler Lynch",False,(WHITE))
        screen.blit(TitleMessageTyped,(425,HEIGHT//1.8))
        screen.blit(AuthorMessage,(WIDTH//2-(130),HEIGHT//1.2))
    else:
        screen.blit(Score_typed,(50,40))
        screen.blit(High_score_typed,(50,90))
        
    if player.dead == True:
        try:
            if RS.reset == False:
                screen.blit(Gameover_messageTyped,(450,HEIGHT//3))
        except NameError:
            if player.dead == True:
                screen.blit(Gameover_messageTyped,(450,HEIGHT//3))

    ##These groups are drawn last so they appear over everything
    reset_group.draw(screen)
    slice.draw(screen)
    
    ##after render flip display
    pygame.display.flip()
    
pygame.quit()
        
