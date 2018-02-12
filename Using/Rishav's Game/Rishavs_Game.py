import time
import pygame
import random
import math
import os
pygame.init()
width = 800
height = 600
score=0
highScore=0
gameDisplay = pygame.display.set_mode((width,height)) # creates a display and returns a surface object
white = (255,255,255)
black = (0,0,0)
num=1
buttonCooldown=111
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Rishav's Game")
pygame.display.set_icon(icon)
gameDisplay.fill(white)
flashy=False
color = white
clock = pygame.time.Clock()
font =  pygame.font.SysFont(None,20)
boing = pygame.mixer.Sound("Boing.wav")
cheer = pygame.mixer.Sound("Cheering.wav")
crunch = pygame.mixer.Sound("Crunch.wav")
width = 800
fire=False
height = 600
switch = False
v1 = False
dM=False
qe=10000
we=1000
true=False
sM=False
hacked = False
gameLoop = False
mC = False
mP = 1
tC =False
tP=1
boss=False
changeX = 0
changeY = 0
wins1 = 0
wins2 = 0
changeX2 = 0
changeY2 = 0
level = (int)(score/10)+1
multiPlayer = False
story=False
isk=(int)(score/5)+1
blue = (0,0,255)
color2 = white
u = 0
game='dodgeNEat'
admin=False
game_backround=True
image = pygame.image.load("snake game backround.jpg")
image = pygame.transform.scale(image,(800,600))
competition = False
s="Cool Music.mp3"
pl = random.randrange(1,2)
game_settings = 1
part=4
lines=[]
def story_mode():
    global lines
    global color
    global story
    global image
    mouse_pressed=False
    story=True
    global switch
    global part
    if part == 1:
        youtubeIsAwesome=True
        lines=[]
        while youtubeIsAwesome:
            gameDisplay.fill(white)
            messageOnScreen("Draw Yourself here!!",200,10,(0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==13:
                        youtubeIsAwesome=False
            if switch:
                color=(255,255,255)
            switch=False
            if color==(255,255,255):
                switch=True
                color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
            pos=pygame.mouse.get_pos()
            pygame.draw.lines(gameDisplay, (0,0,0), False, ((250,100),(250,500),(550,500),(550,100),(250,100)),10)
            if (pygame.mouse.get_pressed()[0]==1 or pygame.mouse.get_pressed()[2]==1) and not mouse_pressed and 550>pos[0]>260:
                lines.append([])
            if (pygame.mouse.get_pressed()[0]==1 or pygame.mouse.get_pressed()[2]==1) and 500>pos[1]>110 and 550>pos[0]>260:
                mouse_pressed=True
            else:
                mouse_pressed=False
            if mouse_pressed:
                lines[len(lines)-1].append([pos[0],pos[1]])
            draw_character()
            if button(500,520,300,40,"Enter",(255,0,255),510,530,3):
                youtubeIsAwesome=False
            pygame.display.update()
        part+=1
    if part==2:
        gameDisplay.fill(white)
        draw_character()
        pygame.draw.circle(gameDisplay,(102,51,0),(600,250),30)
        pygame.draw.circle(gameDisplay,(0,0,0),(610,270),2)
        pygame.draw.circle(gameDisplay,(0,0,0),(602,252),2)
        pygame.draw.circle(gameDisplay,(0,0,0),(603,260),2)
        pygame.draw.circle(gameDisplay,(0,0,0),(590,230),2)
        pygame.draw.circle(gameDisplay,(0,0,0),(610,232),2)
        pygame.draw.circle(gameDisplay,(0,0,0),(583,270),2)
        messageOnScreen("Yay now I can finally eat my cookie",300,10,(0,0,0))
        pygame.display.update()
        time.sleep(10)
        pygame.draw.rect(gameDisplay,(255,255,255),[290,0,2000,60])
        pygame.draw.rect(gameDisplay,(255,0,0),[650,220,150,60])
        pygame.draw.rect(gameDisplay,(255,0,0),[600,200,70,20])
        pygame.draw.rect(gameDisplay,(255,0,0),[600,280,70,20])
        messageOnScreen("HEY THAT'S MY COOKIE",300,10,(0,0,0))
        pygame.display.update()
        time.sleep(10)
        gameDisplay.fill(white)
        messageOnScreen("Imma find you and kill you for what you have done!",100,10,(0,0,0))
        messageOnScreen("I will get justice. That was going to be a great cookie!",50,70,(0,0,0))
        draw_character()
        pygame.display.update()
        time.sleep(10)
        part+=1
    if part==3:
        gameDisplay.fill(white)
        draw_character()
        messageOnScreen("First I have to get out of this neighborhood!",2,10,(0,0,0))
        messageOnScreen("Cross the roads safely! And I'm still hungry so . . .",2,70,(0,0,0))
        pygame.display.update()
        time.sleep(10)
        global game
        game="crossyRoad"
        crossyRoad()
    if part==4:
        gameDisplay.fill(white)
        messageOnScreen("Those weren't as good as my cookies but it's fine",2,10,(0,0,0))
        messageOnScreen("Now the fastest way to get to his castle is to . . .",2,70,(0,0,0))
        messageOnScreen("TURN INTO A BIRD A FLY WHAT ELSE WOULD IT BE!!! DUH!!!!",0,130,(0,0,0))
        draw_character()
        pygame.display.update()
        time.sleep(10)
        game="flappyBird"
        flappyBird()
    if part==5:
        gameDisplay.fill(white)
        draw_character()
        messageOnScreen("Oh There It Is",2,10,(0,0,0))
        castle=pygame.image.load("castle.jpg")
        castle=pygame.transform.scale(castle,(300,300))
        gameDisplay.blit(castle,(600,200))
        pygame.display.update()
        time.sleep(5)
        messageOnScreen("But I think I see a wall made of bricks blocking it",0,40,(0,0,0))
        messageOnScreen("Let's break it!!!!",0,80,(0,0,0))
        pygame.display.update()
        time.sleep(5)
        game="brickBreaker"
        brickBreaker()
    if part==6:
        gameDisplay.fill(white)
        image=pygame.image.load("Arena.jpg")
        image=pygame.transform.scale(image,(800,600))
        gameDisplay.blit(image,(0,0))
        messageOnScreen("As soon as we are in, there will be at least one guard",2,10,white)
        messageOnScreen("And I may not have powers but he will have some",2,40,white)
        messageOnScreen("I need some powers too, and I gotta remember, DONT DIE!",2,70,white)
        messageOnScreen('But first I gotta navigate through here!',10,100,white)
        draw_character()
        pygame.display.update()
        time.sleep(10)
        os.system('MazeProgram.BAT')
        part+=1
    if part==7:
        game='dodgeNEat'
        global game_backround
        game_backround=False
        dodgeNEat()
    if part==8:
        image=pygame.image.load("Arena.jpg")
        image=pygame.transform.scale(image,(800,600))
        gameDisplay.blit(image,(0,0))
        messageOnScreen("YES I HAVE POWERS, I CAN NOW SHOOT!!!",2,10,white)
        messageOnScreen("HEY I THINK I CAN DASH TOO. TIME TO ATTACK",2,40,white)
        messageOnScreen("OH HERE COME SOME MORE GUARDS",2,70,white)
        draw_character()
        pygame.display.update()
        time.sleep(10)
        game="battle"
        battle()
    if part==9:
        gameDisplay.fill(white)
        image=pygame.image.load("Arena.jpg")
        image=pygame.transform.scale(image,(800,600))
        gameDisplay.blit(image,(0,0))
        messageOnScreen("I'VE BEATEN ALL YOUR PUNY GUARDS NOW FIGHT ME",2,10,white)
        messageOnScreen("YOU SON OF A COOKIE MONSTER",2,40,white)
        messageOnScreen("I'M GETTING MY COOKIE!",2,70,white)
        draw_character()
        pygame.display.update()
        time.sleep(10)
        for uq in range(0,600,1):
            pygame.draw.rect(gameDisplay, (255,0,0),[600,0,200,uq])
            pygame.display.update()
        time.sleep(3)
        boss_fight()
    if part==10:
        game='getthecookie'
        cookie()
    if part==11:
        reading=True
        while reading:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                    pygame.quit()
            if pygame.mouse.get_pressed()[0]==1 or pygame.mouse.get_pressed()[2]==1:
                reading=False
            gameDisplay.fill(black)
            messageOnScreen("Then (s)he died of cookie-needing disease",100,10,(255,255,255))
            messageOnScreen('Remember the cookie-needing disease is a serious disease. It mainly affects people named Rishav. This may have',10,40,(255,255,255),2.0)
            messageOnScreen('just been for fun. But you can take something out of this. Save a life. The next time you see someone with the',10,60,(255,255,255),2.0)
            messageOnScreen('name Rishav, buy them a cookie. Whether it is in the lunch room or anywhere else. Save a life by buying Rishav',10,80,(255,255,255),2.0)
            messageOnScreen('a cookie. PS: BUY ME A COOKIE- Rishav',10,100,white,2.0)
            messageOnScreen('CLICK TO CONTINUE',300,400,white)
            pygame.display.update()
        gameover=pygame.image.load('gameover.jpg')
        gameover=pygame.transform.scale(gameover,(800,600))
        gameDisplay.blit(gameover,(0,0))
        messageOnScreen('Give Rishav cookie to play again',250,320,white,3.0)
        pygame.display.update()
        time.sleep(10)
        story=False
        global boss
        boss=False
        part=1
        mainMenu()
def cookie():
    fighting=True
    global image
    global story
    global part
    global color
    x=100
    health=100
    y=480
    soo=False
    changeX=0
    v0=0
    t=0
    dsd=0
    xp=x
    yp=y
    yu=200
    start_t=0
    bullets=[]
    direction=10
    new=False
    initialT=pygame.time.get_ticks()/1000
    a=-1
    sent=initialT
    laser=False
    las=initialT
    if story:
        image=pygame.image.load("Arena.jpg")
        image=pygame.transform.scale(image,(800,600))
    while fighting:
        tim= pygame.time.get_ticks()/1000.0
        tim=int(tim)
        gameDisplay.blit(image,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and (y==280 or y==380 or y==480):
                    v0=20
                    start_t=tim
                if event.key==32:
                    print x
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            changeX=-5
        elif key[pygame.K_RIGHT]:
            changeX=5
        else:
            changeX=0
        if y>600:
            fighting=False
        if x>=550 and x<=700 and y==280:
            if not soo:
                dsd=x+5
            soo=True
        if soo:
            messageOnScreen("OOOOOPPPPSS!!! NOO COOKIE DONT DIE",100,10,(255,255,255))
            pygame.draw.rect(gameDisplay,(255,0,0),[dsd,285,10,10])
            dsd+=5
        if dsd+10>=700:
            yu+=10
            dsd=909090
        if x==380 and y==480 and changeX>0:
            changeX=0
        if x==530 and y==380 and changeX>0:
            changeX=0
        x+=changeX
        t=tim-start_t
        y-=int(v0*t+.5*a*t**2)
        v0+=a*t
        if x+20>400 and x<700 and y>=380:
            y=380
            if v0<0:
                v0=0
        if x+20>550 and x<700 and y>=280:
            y=280
            if v0<0:
                v0=0
        if yu>600:
            part+=1
            story_mode()
        cookie=pygame.image.load("cookie_in_jail.png")
        cookie=pygame.transform.scale(cookie, (100,100))
        gameDisplay.blit(cookie,(700,yu))
        pygame.draw.rect(gameDisplay,(255,255,255),[100,500,600,100])
        pygame.draw.rect(gameDisplay,(255,255,255),[400,400,300,100])
        pygame.draw.rect(gameDisplay,(255,255,255),[550,300,150,100])
        if health<=0:
            part+=1
            story_mode()
        for boo in bullets:
            pygame.draw.rect(gameDisplay,(255,0,0),[boo[0],boo[1],10,10])
        if 700>x>80 and y>=480:
            y=480
            if v0<0:
                v0=0
        pygame.draw.rect(gameDisplay,color,[x,y,20,20])
        pygame.display.update()
    playAgain()
def boss_fight():
    fighting=True
    global image
    global story
    global part
    global color
    x=100
    health=100
    y=480
    changeX=0
    v0=0
    t=0
    xp=x
    yp=y
    start_t=0
    bullets=[]
    direction=10
    global boss
    boss=True
    new=False
    initialT=pygame.time.get_ticks()/1000
    enemies=[]
    a=-1
    sent=initialT
    laser=False
    las=initialT
    if story:
        image=pygame.image.load("Arena.jpg")
        image=pygame.transform.scale(image,(800,600))
    while fighting:
        tim= pygame.time.get_ticks()/1000.0
        w=10
        e=100*math.cos(w*(tim-initialT))+500
        tim=int(tim)
        gameDisplay.blit(image,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and y==480:
                    v0=20
                    start_t=tim
                if event.key==pygame.K_SPACE:
                    bullets.append([x+5,y+5,direction])
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            changeX=-5
            direction=-10
        elif key[pygame.K_RIGHT]:
            changeX=5
            direction=10
        else:
            changeX=0
        for enemy in enemies:
            if enemy[0]+20>=x and enemy[0]<=x+20:
                if enemy[1]>=y and enemy[1]<=y+20:
                  fighting=False
        if x+20>=e:
            fighting=False
        if y>600:
            fighting=False
        if (tim-initialT)%5==0 and (tim-initialT)!=0 and not laser:
            las = tim
            laser=True
        if laser:
            pygame.draw.line(gameDisplay,(255,0,0), (e,200),(xp,yp),2)
            if xp>=x and xp<=x+20 and yp>=y and yp<=y+20:
                fighting = False
        if (tim-initialT)%3==0 and not new and not laser:
            xp=x
            yp=y
        if (tim-initialT)%1==0 and not new:
            enemies.append([e+20,random.randrange(200,480)])
            new=True
            sent=tim
        if tim!=sent:
            new=False
        if tim!=las:
            laser=False
        for enemy in enemies:
            if enemy[0]!=-222:
                if enemy[0]>x:
                    enemy[0]-=2
                else:
                    enemy[0]+=2
        x+=changeX
        t=tim-start_t
        y-=int(v0*t+.5*a*t**2)
        v0+=a*t
        cookie=pygame.image.load("cookie_in_jail.png")
        cookie=pygame.transform.scale(cookie, (100,100))
        gameDisplay.blit(cookie,(700,200))
        pygame.draw.rect(gameDisplay, (255,0,0),[e,200,80,300])
        pygame.draw.rect(gameDisplay,(255,255,255),[100,500,600,100])
        for boo in bullets:
            boo[0]+=boo[2]
            for su in enemies:
                if boo[0]+10>=su[0] and boo[0]<=su[0]+20:
                    if boo[1]+10>=su[1] and boo[1]<=su[1]+20:
                        boo[0]=-123
                        boo[1]=-123
                        boo[2]=0
                        su[0]=-222
                        su[1]=-222
            if boo[0]+10>e:
                boo[0]=-123
                boo[1]=-123
                boo[2]=0
                health-=1
        pygame.draw.rect(gameDisplay,(255,255,255),[50,20,health*7,20])
        if health<=0:
            part+=1
            story_mode()
        for boo in bullets:
            pygame.draw.rect(gameDisplay,(255,0,0),[boo[0],boo[1],10,10])
        for ui in enemies:
            ui[1]+=4
            if 700>ui[0]>80 and ui[1]>=480:
                ui[1]=480
        if 700>x>80 and y>=480:
            y=480
            if v0<0:
                v0=0
        for enemy in enemies:
            pygame.draw.rect(gameDisplay,(255,0,0),[enemy[0],enemy[1],20,20])
        pygame.draw.rect(gameDisplay,color,[x,y,20,20])
        pygame.display.update()
    playAgain()
def draw_character():
    global lines
    global color
    if color==(255,255,255):
        color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
    for y in range(len(lines)):
        points=lines[y]
        if len(points)>1:
            pygame.draw.lines(gameDisplay,color, False, points,2)
def mainMenu():
    gameStart=False
    global image
    global story
    global buttonCooldown
    global game
    gameDisplay.blit(image, (0,0))
    story=False
    messageOnScreen("Welcome to Rishav's Game",200,100,(255,0,255),5)
    while  not gameStart:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    gameStart = True
                    mainGame()
                if event.key == pygame.K_q:
                    quit()
                    pygame.quit()
                if event.key == pygame.K_g:
                    gameModes()
                    gameStart=True
                if event.key == pygame.K_s:
                    settings()
                if event.key == pygame.K_m:
                    gameStart=True
                    story_mode()
        if button(200,150,400,70,"Play (Y)",(0,255,0),350,170,4):
            gameStart=True
            mainGame()
        if button(200,450,400,70,"Quit (Q)",(255,0,0),350,470,4):
            pygame.quit()
            quit()
        if button(200,225,400,70,"Games (G)",(0,0,255),300,245,4):
            gameStart=True
            gameModes()
        if button(200,375,400,70,"Story Mode (M)",(255,0,255),320,395):
            gameStart=True
            story_mode()
        if button(200,300,400,70,"Settings (S)",(0,0,255),320,320,4):
            settings()
        buttonCooldown+=1
        pygame.display.update()
def gameModes():
    godie=True
    global image
    global game
    global buttonCooldown
    gameDisplay.blit(image, (0,0))
    messageOnScreen("Games",350,25,(255,0,255),5)
    messageOnScreen("_______",350,25,(255,0,255),5)
    while godie:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game = 'flappyBird'
                    godie=False
                if event.key == pygame.K_x:
                    godie=False
                if event.key == pygame.K_b:
                    game = 'battle'
                    godie=False
                if event.key == pygame.K_m:
                    game = 'MazeFight'
                    godie=False
                if event.key == pygame.K_r:
                    game = 'brickBreaker'
                    godie = False
                if event.key == pygame.K_c:
                    game = 'crossyRoad'
                    godie = False
                if event.key == pygame.K_d:
                    game = 'dodgeNEat'
                    godie=False
       if button(220,80,400,70,"Flappy Bird (F)","FLAPPYBIRD.jpg",320,100,4):
           game="flappyBird"
           godie=False
       if button(220,155,400,70,"Battle Mode (B)","Arena.jpg",320,175,color=white):
           game = 'battle'
           godie=False
       if button(220,230,400,70,"Brick Breaker (R)","brick-breaker-image.jpg",320,250,color=white):
           game='brickBreaker'
           godie=False
       if button(220,305,400,70,"Crossy Road (C)","crossyroadimage.jpg",320,325,color = (255,0,255)):
           game = 'crossyRoad'
           godie=False
       pos=pygame.mouse.get_pos()
       if 620> pos[0] > 220 and 450> pos[1] > 380:
           pygame.draw.rect(gameDisplay, (225,225,225), [220,380,400,70])
       else:
           pygame.draw.rect(gameDisplay,(255,255,255),[220,380,400,70])
       if button(220,380,400,70,"Dodge N Eat (D)","evilwhiteblock.jpg",320,400,color=(100,200,255)):
           game = 'dodgeNEat'
           godie = False
       if button(220,455,400,70,'Two Player Maze Fight(M)',"maze0.jpg",240,475,color=white):
           game='MazeFight'
           godie=False
       if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560,4):
            mainMenu()
       #FIX THIS PART SO THAT YOU DON'T HAVE TO DOUBLE CLICK BUTTONS
       buttonCooldown+=1
       pygame.display.update()
    mainMenu()
def screen_type(x,y,color=(0,0,0),size=4,string='none'):
    enter = False
    s=""
    while enter == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 8:
                    temp=""
                    for weu in range(len(s)-1):
                        temp+=s[weu]
                    s=temp
                elif event.key == 13:
                    enter=True
                else:
                    if string=='none':
                        s+=chr(event.key)
                    elif string == 'num':
                        if event.key>=48 and event.key<=57:
                            s+=chr(event.key)
        messageOnScreen(s,x,y,color,size)
        pygame.display.update()
    return s
def settings():
    global game
    global buttonCooldown
    global highScore
    if game == 'dodgeNEat':
        game_settings = dodge_n_eat_settings()
    elif game =="brickBreaker":
        game_settings = brick_breaker_settings()
    else:
        game_settings = none()
    bOBISAWESOME=True
    while bOBISAWESOME:
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    bOBISAWESOME=False
                if event.key == pygame.K_b:
                    background_settings()
                if event.key == pygame.K_c:
                    color_settings()
                if event.key == pygame.K_m:
                    music_settings()
                if event.key == pygame.K_h:
                    highScore=0
                if event.key == pygame.K_a:
                    admin_settings()
                if event.key == pygame.K_x:
                    bOBISAWESOME=False
        # Backround, Color, Music, high SCore reset
        messageOnScreen("Settings",10,10,(255,255,255),2.5)
        messageOnScreen("________",10,10,(255,255,255),2.5)
        if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560,4):
            bOBISAWESOME=False
        if button(10,50,780,30,"Background Settings (B)",(0,0,255),20,60,2.5):
            background_settings()
        if button(10,90,780,30,"Color Settings (C)",(0,0,255),20,100,2.5):
            color_settings()
        if button(10,130,780,30,"Music Settings (M)",(0,0,255),20,140,2.5):
            music_settings()
        if highScore>0:
            if button(10,170,780,30,"Reset Highest Score (H)",(255,255,255),20,180,2.5):
                highScore=0
        else:
            button(10,170,780,30,"Reset Highest Score (H)",(100,100,100),20,180,2.5)
        if button(10,210,780,30,"Admin Settings (A)",(0,0,255),20,220,2.5):
            admin_settings()
        game_settings.settings()
        buttonCooldown+=1
        pygame.display.update()
    mainMenu()
def music_settings():
    global s
    xe = pygame.mixer.music.get_volume()*600+100
    global buttonCooldown
    bobbobo = True
    while bobbobo:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_1:
                   if(s!="Cool Music.mp3"):
                       s="Cool Music.mp3"
                       music()
                       bobbobo=False
               if event.key == pygame.K_2:
                   if(s!="Cool Music2.mp3"):
                       s="Cool Music2.mp3"
                       music()
                       bobbobo=False
               if event.key == pygame.K_4:
                   if not s=="I got a pea.mp3":
                       s="I got a pea.mp3"
                       music()
                       bobbobo=False
               if event.key == pygame.K_3:
                   if(s!="Cool Music3.mp3"):
                       s="Cool Music3.mp3"
                       music()
                       bobbobo=False
               if event.key== pygame.K_5:
                   if(s!="Minions Banana Song.mp3"):
                       s="Minions Banana Song.mp3"
                       music()
                       bobbobo=False
               if event.key == pygame.K_6:
                   if s!="Pranav Singing.mp3":
                       s="Pranav Singing.mp3"
                       music()
                       bobbobo=False
               if event.key == pygame.K_7:
                   s="none"
                   pygame.mixer.music.stop()
                   bobbobo=False
        arr = ["Cool Music.mp3","Cool Music2.mp3","Cool Music3.mp3","Just a Little Surprise.mp3","Minions Banana Song.mp3","Pranav Singing.mp3","SPMEXY DUEL.mp3","none"]
        yee=0
        gameDisplay.blit(image,[0,0])
        for wer in arr:
            qun=False
            if button(10,yee*60+10,780,50,wer+" ("+str(yee+1)+")",white,30,yee*60+20,2.5):
                if s!=wer:
                    s=wer
                    qun=True
                if s=='none':
                    pygame.mixer.music.stop()
                elif qun:
                    music()
                bobbobo=False
            yee+=1
        messageOnScreen("Volume",300,480,white)
        messageOnScreen("______",300,480,white)
        pygame.draw.rect(gameDisplay,(0,0,0),[100,510,600,30])
        pygame.draw.rect(gameDisplay,(255,255,255),[105,515,xe-90,20])
        pygame.draw.rect(gameDisplay, (255,255,255),[xe,500,20,50])
        mouse_pos = pygame.mouse.get_pos()[0]
        mouse_posY = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0]==1 and mouse_pos>=100 and mouse_pos<=700 and mouse_posY>500 and mouse_posY<550:
            xe=mouse_pos
        pygame.mixer.music.set_volume((xe-100)/600.0)
        buttonCooldown+=1
        pygame.display.update()
def background_settings():
    global image
    global game_backround
    global buttonCooldown
    its_awesome = True
    arr = ["Arena.jpg","Block.jpg","snake game backround.jpg","RishavIcon.jpg","FLAPPYBIRD.jpg","crossyroadimage.jpg","brick-breaker-image.jpg","BrickBreakerBackground.png","FlappyBirdBackround.jpg"]
    arr2 = ["apple.jpg","coolCat.jpg","flash.png","ghost.jpg","hog.png","marbles.jpg","skull.jpg","wolf.jpg","Zoom.png"]
    while its_awesome:
        gameDisplay.blit(image,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                for w in range(49,58):
                    if event.key == w:
                        image=pygame.image.load(arr[w-49])
                        image = pygame.transform.scale(image, [800,600])
                        game_backround=False
                        its_awesome=False
                for w in range(97,106):
                    if event.key == w:
                        image=pygame.image.load(arr2[w-97])
                        image = pygame.transform.scale(image, [800,600])
                        its_awesome=False
                        game_backround=False
                if event.key == pygame.K_z:
                    game_backround=True
                    settings()
        for er in range(0,len(arr)):
            if button(er*90,10,80,60,"("+str(er+1)+")",arr[er],25+er*90,25,color=(255,0,255)):
                image=pygame.image.load(arr[er])
                image = pygame.transform.scale(image, [800,600])
                its_awesome=False
                game_backround=False
        for er2 in range(0,len(arr2)):
            if button(er2*90,80,80,60,"("+chr(er2+97)+")",arr2[er2],25+er2*90,95,color=(255,0,255)):
                image=pygame.image.load(arr2[er2])
                image = pygame.transform.scale(image, [800,600])
                its_awesome=False
                game_backround=False
        if button(0,150,800,60,"Defualt for Games (z)",(255,255,255),10,160):
            game_backround=True
            settings()
        if not its_awesome:
            gameDisplay.blit(image,[0,0])
        pygame.display.update()
        buttonCooldown+=1
        if not its_awesome:
            time.sleep(2)
def color_settings():
    global switch
    gameDisplay.blit(image,[0,0])
    pygame.display.update()
    global color
    notDone=True
    while notDone:
        gameDisplay.fill(white)
        messageOnScreen("Choose an rgb value (255,255,255 for changing)",50,100,(255,0,255))
        messageOnScreen("R:",50,200,(255,0,0))
        rcolor=screen_type(100,200,(255,0,0),4,'num')
        messageOnScreen("G:",50,300,(0,255,0))
        gcolor=screen_type(100,300,(0,255,0),4,'num')
        messageOnScreen("B:",50,400,(0,0,255))
        bcolor=screen_type(100,400,(0,0,255),4,'num')
        color=(int(rcolor),int(gcolor),int(bcolor))
        if color[0]>255 or color[0]<0 or color[1]>255 or color[1]<0 or color[2]>255 or color[2]<0:
            messageOnScreen("Invalid Input",10,550,(255,0,0))
            pygame.display.update()
            time.sleep(1)
        else:
            notDone=False
    global switch
    if color==white:
        switch=True
    else:
        switch=False
    pygame.draw.rect(gameDisplay, color ,[400,200,200,200])
    pygame.display.update()
    time.sleep(2)
def admin_settings():
    password('bobi sav vesome')
def mainGame():
    if game=='flappyBird':
        flappyBird()
    elif game=='getthecookie':
        cookie()
    elif game=='battle':
        battle()
    elif game=='crossyRoad':
        crossyRoad()
    elif game=='brickBreaker':
        brickBreaker()
    elif game=='dodgeNEat':
        dodgeNEat()
    elif game=='MazeFight':
        gameDisplay.fill(black)
        pygame.display.update()
        os.system('Whackathon.BAT')
        mainMenu()
    elif game=='Maze':
        gameDisplay.fill(black)
        pygame.display.update()
        os.system('MazeProgram.BAT')
        mainMenu()
def flappyBird():
    gameExit = False
    global score
    global game_backround
    x=400
    y=300
    move=False
    bob=0
    bob2=0
    score = 0
    holes1=[]
    holes2=[]
    tunnels=[]
    global buttonCooldown
    global image
    if game_backround:
        image = pygame.image.load("FlappyBirdBackround.jpg")
        image = pygame.transform.scale(image,(800,600))
    bird= pygame.image.load("Bird.png")
    bird = pygame.transform.scale(bird,(20,20))
    for ui in range(20):
        tunnels.append(False)
        holes1.append(0)
        holes2.append(0)
    while gameExit == False:
        clock.tick(1000)
        gameDisplay.blit(image,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed()[0]==1 or event.type == pygame.KEYDOWN:
                y+=-50
                bob=0
                move=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and admin:
                    score+=1
                if event.key==pygame.K_p:
                    paused()
        if bob2%(50)==0 and move:
            for uiw in range(0,len(tunnels)-1):
                tunnels[uiw]=tunnels[uiw+1]
                holes1[uiw]=holes1[uiw+1]
                holes2[uiw]=holes2[uiw+1]
            if (bob2/(50))%7==0:
                tunnels[len(tunnels)-1]=True
                holes1[len(tunnels)-1]=random.randrange(40,250)
                holes2[len(tunnels)-1]=random.randrange(100-(int)(score),300-(int)(score)*3)
            else:
                tunnels[len(tunnels)-1]=False
                holes1[len(tunnels)-1]=0
                holes2[len(tunnels)-1]=0
        for iuo in range(len(tunnels)):
            if tunnels[iuo]:
                pygame.draw.rect(gameDisplay, (0,100,0), [iuo*40,0,40,holes1[iuo]])
                pygame.draw.rect(gameDisplay, (0,100,0), [iuo*40-10,holes1[iuo]-20,60,20])
                pygame.draw.rect(gameDisplay,(0,100,0),[iuo*40,holes1[iuo]+holes2[iuo],40,600-(holes1[iuo]+holes2[iuo])])
                pygame.draw.rect(gameDisplay, (0,100,0), [iuo*40-10,holes1[iuo]+holes2[iuo],60,20])
                if x+20>=iuo*40 and x<=(iuo+1)*40:
                    if y>=holes1[iuo] and y+20<=holes1[iuo] + holes2[iuo]:
                        score+=1/100.0
                    elif not admin:
                        gameExit=True
        bob2+=1
        bob+=1
        if button(770,0,30,33,"||",(255,255,255),775,2,4):
            paused()
        if y>=580 or y<0  and not admin:
            gameExit=True
        clock.tick(400)
        gameDisplay.blit(bird,(x,y))
        if move:
            y+=200*bob/1500
        buttonCooldown+=1
        global part
        global story
        if score>=15.0 and story:
            part+=1
            story_mode()
        messageOnScreen("Score: "+str(score),10,10,(0,0,0),3)
        pygame.display.update()
    playAgain()
def battle():
    x=400
    y=300
    global color
    global image
    global game_backround
    if game_backround:
        image = pygame.image.load("Arena.jpg")
        image = pygame.transform.scale(image , (800,600))
    global score
    frozenNum=0
    global admin
    frozen=False
    ammo=10
    if admin:
        ammo = 999999999
    score = 0
    shoo=[]
    shield=[]
    frozebobNum=0
    changeX=0
    bob=0
    changeY=0
    broken=False
    brokenNum=5001
    enemies=[]
    frozebob=False
    mr=0
    ml=0
    mu=0
    md=0
    bullet = []
    gameExit = False
    global buttonCooldown
    while gameExit == False:
        clock.tick(5000000)
        sleep=False
        dash = False
        global switch
        global story
        global part
        if score>10 and story:
            part+=1
            story_mode()
        cheer = pygame.mixer.Sound("Cheering.wav")
        if switch:
            color=(255,255,255)
        switch=False
        if color==(255,255,255):
           switch=True
           color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
        level = int(score/10)+1
        gameDisplay.blit(image, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and not frozen:
                    changeX=6
                    changeY=0
                    if mr<30 and not mr==0:
                        for er in range(200):
                            x+=1
                            for b in range(len(enemies)):
                                if x+20>=enemies[b][0] and x<=enemies[b][0]+20:
                                    if y+20>=enemies[b][1] and y<=enemies[b][1]+20:
                                        if enemies[b][3]=="freeze":
                                            frozebob=True
                                            frozebobNum=0
                                        if enemies[b][3]=="gun":
                                            ammo+=5
                                        if enemies[b][3]=="sheild":
                                            if brokenNum>500:
                                                brokenNum = 0
                                        if enemies[b][3]=="bomb":
                                            pygame.draw.circle(gameDisplay, (255,0,0), (enemies[b][0]+10,enemies[b][1]+10),150)
                                            if (x - enemies[b][0]-10)**2 + (y - enemies[b][1]-10)**2 <= 150**2 and not admin and not broken:
                                                gameExit=True
                                            for uta in range(0,len(enemies),1):
                                                if (enemies[uta][0] - enemies[b][0]-10)**2 + (enemies[uta][1] - enemies[b][1]-10)**2 <= 150**2 and uta!=b:
                                                    enemies[uta]=[-11111,-11111,0,"dead"]
                                            pygame.display.update()
                                            sleep=True
                                        dash=True
                                        enemies[b]=[12901903,10239,0,"dead"]
                    mr=0
                    ml=200
                    mu=200
                    md=200
                if event.key == pygame.K_LEFT and not frozen:
                    changeX=-6
                    changeY=0
                    if ml<30 and not ml==0:
                        for er in range(200):
                            x-=1
                            for b in range(len(enemies)):
                                if x+20>=enemies[b][0] and x<=enemies[b][0]+20:
                                    if y+20>=enemies[b][1] and y<=enemies[b][1]+20:
                                        if enemies[b][3]=="freeze":
                                            frozebob=True
                                            frozebobNum=0
                                        if enemies[b][3]=="gun":
                                            ammo+=5
                                        if enemies[b][3]=="sheild":
                                            if brokenNum>500:
                                                brokenNum = 0
                                        if enemies[b][3]=="bomb":
                                            pygame.draw.circle(gameDisplay, (255,0,0), (enemies[b][0]+10,enemies[b][1]+10),150)
                                            if (x - enemies[b][0]-10)**2 + (y - enemies[b][1]-10)**2 <= 150**2 and not admin and not broken:
                                                gameExit=True
                                            for uta in range(0,len(enemies),1):
                                                if (enemies[uta][0] - enemies[b][0]-10)**2 + (enemies[uta][1] - enemies[b][1]-10)**2 <= 150**2 and uta!=b:
                                                    enemies[uta]=[-11111,-11111,0,"dead"]
                                            pygame.display.update()
                                            sleep=True
                                        enemies[b]=[12901903,10239,0,"dead"]
                                        dash=True
                    mr=200
                    ml=0
                    mu=200
                    md=200
                if event.key == pygame.K_UP and not frozen:
                    changeY=-6
                    changeX=0
                    if mu<30 and not mu==0:
                        for er in range(200):
                            y-=1
                            for b in range(len(enemies)):
                                if x+20>=enemies[b][0] and x<=enemies[b][0]+20:
                                    if y+20>=enemies[b][1] and y<=enemies[b][1]+20:
                                        if enemies[b][3]=="freeze":
                                            frozebob=True
                                            frozebobNum=0
                                        if enemies[b][3]=="gun":
                                            ammo+=5
                                        if enemies[b][3]=="sheild":
                                            if brokenNum>500:
                                                brokenNum = 0
                                        if enemies[b][3]=="bomb":
                                            pygame.draw.circle(gameDisplay, (255,0,0), (enemies[b][0]+10,enemies[b][1]+10),150)
                                            if (x - enemies[b][0]-10)**2 + (y - enemies[b][1]-10)**2 <= 150**2 and not admin and not broken:
                                                gameExit=True
                                            for uta in range(0,len(enemies),1):
                                                if (enemies[uta][0] - enemies[b][0]-10)**2 + (enemies[uta][1] - enemies[b][1]-10)**2 <= 150**2 and uta!=b:
                                                    enemies[uta]=[-11111,-11111,0,"dead"]
                                            pygame.display.update()
                                            sleep=True
                                        enemies[b]=[12901903,10239,0,"dead"]
                                        dash=True
                    mr=200
                    ml=200
                    mu=0
                    md=200
                if event.key == pygame.K_DOWN and not frozen:
                    changeY=6
                    changeX=0
                    if md<30 and not md==0:
                        for er in range(200):
                            y+=1
                            for b in range(len(enemies)):
                                if x+20>=enemies[b][0] and x<=enemies[b][0]+20:
                                    if y+20>=enemies[b][1] and y<=enemies[b][1]+20:
                                        if enemies[b][3]=="freeze":
                                            frozebob=True
                                            frozebobNum=0
                                        if enemies[b][3]=="gun":
                                            ammo+=5
                                        if enemies[b][3]=="sheild":
                                            if brokenNum>500:
                                                brokenNum = 0
                                        if enemies[b][3]=="bomb":
                                            pygame.draw.circle(gameDisplay, (255,0,0), (enemies[b][0]+10,enemies[b][1]+10),150)
                                            if (x - enemies[b][0]-10)**2 + (y - enemies[b][1]-10)**2 <= 150**2 and not admin and not broken:
                                                gameExit=True
                                            for uta in range(0,len(enemies),1):
                                                if (enemies[uta][0] - enemies[b][0]-10)**2 + (enemies[uta][1] - enemies[b][1]-10)**2 <= 150**2 and uta!=b:
                                                    enemies[uta]=[-11111,-11111,0,"dead"]
                                            pygame.display.update()
                                            sleep=True
                                        enemies[b]=[12901903,10239,0,"dead"]
                                        dash=True
                    mr=200
                    ml=200
                    mu=200
                    md=0

                if event.key == 303:
                    changeX=0
                    changeY=0
                if event.key == pygame.K_TAB and admin:
                    score+=3
                if event.key == pygame.K_SPACE and ammo>0:
                    u=5
                    w=0
                    ammo-=1
                    if changeX>0:
                        u=10.0
                        w=0.0
                    elif changeX<0:
                        u=-10.0
                        w=0.0
                    elif changeY>0:
                        u=0.0
                        w=10.0
                    elif changeY<0:
                        u=0.0
                        w=-10.0
                    shoo.append([x+7.5,y+7.5,u,w])
                if event.key == pygame.K_p:
                       paused()
        if button(770,0,30,33,"||",(255,255,255),775,2,4):
            paused()
        mr+=1
        ml+=1
        mu+=1
        md+=1
        buttonCooldown+=1
        messageOnScreen("Score: "+str(score),10,10,(255,255,255),3)
        messageOnScreen("Ammo: "+str(ammo),10,30,(255,255,255),3)
        if bob%(150/level)==0 and not bob==0:
            r=random.randrange(0,4)
            o=random.randrange(0,11)
            if r==0:
                qw=0
                er=random.randrange(0,580)
            elif r==1:
                qw=780
                er=random.randrange(0,580)
            elif r==2:
                qw=random.randrange(0,780)
                er=0
            else:
                qw=random.randrange(0,780)
                er = 580
            if o==2:
                weapon="stealth"
            elif o==3:
                weapon="sheild"
            elif o==4 or o==5:
                weapon="freeze"
            elif o>=6 and o<9:
                weapon="gun"
            elif o==9 or o==10:
                weapon="bomb"
            else:
                weapon = 'none'
            speed=random.randrange(1,5)
            enemies.append([qw,er,speed,weapon])
            if o <=2 or o==4 or o==5 or o==9 or o==10:
                bullet.append([-1212,-1212])
                shield.append(6)
            elif o==3:
                shield.append(0)
                bullet.append([-1212,-1212])
            elif o>=6 and o<9:
                bullet.append([enemies[len(enemies)-1][0],enemies[len(enemies)-1][1]])
                shield.append(6)
        x+=changeX/2.0
        y+=changeY/2.0
        for rb in range(len(shoo)):
            if shoo[rb]!=(12901903,10239,1239,1293):
                shoo[rb][0]+=shoo[rb][2]*level
                shoo[rb][1]+=shoo[rb][3]*level
                pygame.draw.rect(gameDisplay,(255,0,0),[shoo[rb][0],shoo[rb][1],5,5])
        for ui in range(len(bullet)):
            if x+20>=bullet[ui][0] and x<=bullet[ui][0]+20:
                if y+20>=bullet[ui][1] and y<=bullet[ui][1]+20 and not dash and not broken and not admin:
                    gameExit=True
            for rbw in range(len(shoo)):
                if shoo[rbw][0]+5>=bullet[ui][0] and shoo[rbw][0]<=bullet[ui][0]+10:
                    if shoo[rbw][1]+5>=bullet[ui][1] and shoo[rbw][1]<=bullet[ui][1]+10:
                        shoo[rbw]=(12901903,10239,1239,1293)
                        bullet[ui]=[923874827,2348]
        for sb in range(len(enemies)):
            if bullet[sb][0]>790 and enemies[sb][3]=="gun":
                bullet[sb]=[enemies[sb][0]+5,enemies[sb][1]+5]
            bullet[sb][0]+=5
            if enemies[sb][3]=="stealth":
                pygame.draw.lines(gameDisplay, (0,0,0), False, ((enemies[sb][0],enemies[sb][1]),(enemies[sb][0]+20,enemies[sb][1]),(enemies[sb][0]+20,enemies[sb][1]+20),(enemies[sb][0],enemies[sb][1]+20),(enemies[sb][0],enemies[sb][1])), 3)
            else:
                pygame.draw.rect(gameDisplay, (255,255,255),[enemies[sb][0],enemies[sb][1],20,20])
            if enemies[sb][3]=="gun":
                pygame.draw.rect(gameDisplay, (255,0,0),[enemies[sb][0]+5,enemies[sb][1],10,20])
                pygame.draw.rect(gameDisplay,(0,255,0),[bullet[sb][0],bullet[sb][1],10,10])
            if enemies[sb][3]=="sheild":
                pygame.draw.rect(gameDisplay, (255,shield[sb]*40,shield[sb]*40),[enemies[sb][0],enemies[sb][1],20,20])
            if enemies[sb][3]=="freeze":
                pygame.draw.circle(gameDisplay, (175,238,238), (enemies[sb][0]+10,enemies[sb][1]+10),80)
                pygame.draw.rect(gameDisplay, (0,191,255),[enemies[sb][0],enemies[sb][1],20,20])
            if enemies[sb][3]=="bomb":
                pygame.draw.rect(gameDisplay, (196,62,62),[enemies[sb][0],enemies[sb][1],20,20])
            if not frozebob or enemies[sb][3]=="freeze":
                if enemies[sb][0]<x:
                    enemies[sb][0]+=enemies[sb][2]
                elif enemies[sb][0]>x:
                    enemies[sb][0]-=enemies[sb][2]
                if enemies[sb][1]>y:
                    enemies[sb][1]-=enemies[sb][2]
                elif enemies[sb][1]<y:
                    enemies[sb][1]+=enemies[sb][2]
            else:
                pygame.draw.rect(gameDisplay, (0,191,255),[enemies[sb][0],enemies[sb][1],20,20])
            if (x - enemies[sb][0]-10)**2 + (y - enemies[sb][1]-10)**2 < 80**2 and enemies[sb][3]=="freeze":
                frozen=True
                enemies[sb][3]="none"
                frozenNum=0
            for ab in range(len(shoo)):
                if shoo[ab][0]+5>=enemies[sb][0] and shoo[ab][0]<=enemies[sb][0]+20:
                    if shoo[ab][1]+5>=enemies[sb][1] and shoo[ab][1]<=enemies[sb][1]+20:
                        if enemies[sb][3]=="gun":
                            enemies[sb][3]="none"
                            ammo+=5
                        elif enemies[sb][3]=="sheild":
                            if shield[sb]<6:
                                shield[sb]+=1
                            else:
                                enemies[sb]=[-11111,-11111,0,"none"]
                                if brokenNum>500:
                                    brokenNum = 0
                        elif enemies[sb][3]=="freeze":
                            enemies[sb][3]="none"
                            frozebob=True
                            frozebobNum=0
                        elif enemies[sb][3]=="bomb":
                            pygame.draw.circle(gameDisplay, (255,random.randrange(0,100),random.randrange(0,100)), (enemies[sb][0]+10,enemies[sb][1]+10),150)
                            if (x - enemies[sb][0]-10)**2 + (y - enemies[sb][1]-10)**2 <= 150**2 and not admin and not broken:
                                gameExit=True
                            for uta in range(len(enemies)):
                                if (enemies[uta][0] - enemies[sb][0]-10)**2 + (enemies[uta][1] - enemies[sb][1]-10)**2 < 150**2 and uta!=sb:
                                    enemies[uta]=[-11111,-11111,0,"dead"]
                            enemies[sb]=[-11111,-11111,0,"dead"]
                            pygame.display.update()
                            sleep=True
                        elif enemies[sb][3]=="stealth":
                            enemies[sb][3]="none"
                        elif enemies[sb][3]=="none":
                            enemies[sb]=[-11111,-11111,0,"dead"]
                        shoo[ab]=(12901903,10239,1239,1293)
            if x+20>=enemies[sb][0] and x<=enemies[sb][0]+20:
                if y+20>=enemies[sb][1] and y<=enemies[sb][1]+20 and not admin and not dash and not broken:
                    gameExit=True
        brokenNum+=1
        if x<0:
            x=0
        if x>780:
            x=780
        if frozen:
            changeY=0
            changeX=0
            frozenNum+=1
        if frozenNum>100:
            frozen=False
            frozenNum=0
        if frozebob:
            frozebobNum+=1
        if frozebobNum>200:
            frozebob=False
        if y<0:
            y=0
        if y>580:
            y=580
        if not frozen:
            pygame.draw.rect(gameDisplay, (color) , [x,y,20,20])
        else:
            pygame.draw.rect(gameDisplay, (0,191,255) , [x,y,20,20])
        if brokenNum<250:
            broken=True
            pygame.draw.rect(gameDisplay, (67,222,130), [x,y,20,20])
        elif brokenNum>250 and brokenNum<500 and brokenNum/50%2==0:
            pygame.draw.rect(gameDisplay, (67,222,130), [x,y,20,20])
        elif brokenNum>500:
            broken=False
        score+=.005
        pygame.display.update()
        if sleep:
            time.sleep(.1)
        bob+=1
    score-=.005
    playAgain()
def crossyRoad(sco=0):
    x = 400
    y = 560
    global width
    global highScore
    global height
    global color
    global switch
    cheer = pygame.mixer.Sound("Cheering.wav")
    if switch:
       color=(255,255,255)
    switch=False
    if color==(255,255,255):
       switch=True
       color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
    green = random.randrange(0,255),255,random.randrange(0,21)
    i=0
    pos=[]
    posW=[]
    roads=[]
    ran=[]
    apples=[[0 for bob in range(width/20)] for bob2 in range(600/20)]
    for hop in range(len(apples)):
        for op in range(len(apples[hop])):
            qwer=random.randrange(0,125)
            if qwer == 1:
                apples[hop][op]=True
            else:
                apples[hop][op]=False
    for jop in range(width/20):
        pos.append(0)
        posW.append(0)
    for bob in range(width/20):
        q=random.randrange(1,4)
        if len(roads)>3:
            if q==1 and (not roads[len(roads)-1] or not roads[len(roads)-2] or not roads[len(roads)-3]):
                roads.append(True)
                ran.append(random.randrange(3,8))
            else:
                ran.append(random.randrange(3,8))
                roads.append(False)
        else:
            if q==1:
                roads.append(True)
                ran.append(random.randrange(3,8))
            else:
                ran.append(random.randrange(3,8))
                roads.append(False)
    roads[0]=True
    roads[560/20]=False
    water=[]
    ranW=[]
    for bb in range(width/20):
        q=random.randrange(1,6)
        if q==1 and not roads[bb]:
            if water[bb-1]:
                ranW.append(ranW[bb-1])
            elif water[bb-2] and roads[bb-1]:
                ranW.append(ranW[bb-2])
            else:
                ranW.append(random.randrange(3,8))
            water.append(True)
        else:
            ranW.append(random.randrange(3,8))
            water.append(False)
    water[560/20]=False
    gameExit = False
    global score
    score=sco
    while gameExit == False:
        broken = True
        gameDisplay.fill((255,255,255))
        cars=[]
        if switch:
           color=(255,255,255)
        switch=False
        if color==(255,255,255):
           switch=True
           color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
        logs=[]
        if score>highScore:
            highScore=score
        if (x>width-20 or x<0 or y>680) and not admin:
            gameExit=True
        for bob in range(width/20):
            if roads[bob]:
                cars.append(pygame.Rect(pos[bob],bob*20,20,20))
            else:
                cars.append(pygame.Rect(pos[bob],bob*20,0,0))
        for bob in range(width/20):
            if water[bob]:
                logs.append(pygame.Rect(posW[bob],bob*20,50,20))
            else:
                logs.append(pygame.Rect(posW[bob],bob*20,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x+=20
                if event.key == pygame.K_LEFT:
                    x-=20
                if event.key ==pygame.K_UP:
                    y-=20
                if event.key == pygame.K_DOWN:
                    y+=20
        for bo in range(len(roads)):
            if roads[bo]:
                pygame.draw.rect(gameDisplay, (211,211,211),(0,bo*20,width,20))
                pygame.draw.rect(gameDisplay, (255,255,255), cars[bo])
            elif water[bo]:
                pygame.draw.rect(gameDisplay, (0,0,255),(0,bo*20,width,20))
                pygame.draw.rect(gameDisplay, (165,42,42), logs[bo])
            else:
                pygame.draw.rect(gameDisplay, (green),(0,bo*20,width,20))
        cheer = pygame.mixer.Sound("Cheering.wav")
        if y==-20:
            cheer.play()
            crossyRoad(score)
        for u in range(len(roads)):
            if roads[u]:
                broken = True
                pos[u]+=ran[u]*5.7
                for yu in range(0,i+1):
                    if pos[u]>=ran[u]*50-ran[u]*50*yu:
                        pygame.draw.rect(gameDisplay,(255,255,255), (pos[u]-ran[u]*50*(yu+1),u*20,20,20))
                    if yu==u:
                        i+=1
                    if(((x>=pos[u]-ran[u]*50*(yu+1) and x<=pos[u]-ran[u]*50*(yu+1)+20) or (x+20>=pos[u]-ran[u]*50*(yu+1) and x+20<=pos[u]-ran[u]*50*(yu+1)+20))):
                        if y==u*20  and not admin:
                            gameExit=True
                    if pos[u]-ran[u]*50*(yu+1)<=800:
                        broken = False
        for w in range(len(water)):
            if water[w]:
                posW[w]+=ranW[w]*2.0
            if posW[w]>800:
                posW[w]=-6*ranW[w]
            if y == w*20 and water[w]:
                if x+20>=posW[w] and x<=posW[w]+50:
                    x+=ranW[w]*2.0
                elif (x+20<posW[w] or x>posW[w]+50)  and not admin:
                    gameExit=True
        if broken:
            pygame.draw.rect(gameDisplay,(255,255,255),(0,0,800,600))
            pygame.display.update()
            time.sleep(3)
            crossyRoad()
        for poh in range(len(apples)):
            for po in range(len(apples[poh])):
                if apples[poh][po]:
                    pygame.draw.rect(gameDisplay,(255,0,0),(po*20,poh*20, 20,20))
                    if(((x>=po*20 and x<=po*20+20) or (x+20>=po*20 and x+20<=po*20+20))):
                        if y==poh*20:
                            apples[poh][po]=False
                            score+=1
        pygame.draw.rect(gameDisplay, color, (x,y,20,20))
        messageOnScreen("Score "+str(score),10,10,(0,0,0),3)
        messageOnScreen("Highest Score:"+str(highScore),10,30,(255,0,255),3)
        pygame.display.update()
        global story
        global part
        if score==10 and story:
            part+=1
            story_mode()
    playAgain()
def brickBreaker():
    global color
    global num
    global game_backround
    global flashy
    global switch
    global image
    cheer = pygame.mixer.Sound("Cheering.wav")
    block = pygame.image.load("block.jpg")
    if game_backround:
        image = pygame.image.load("BrickBreakerBackground.png")
        image = pygame.transform.scale(image,(800,600))
    block = pygame.transform.scale(block,(30/num,30/num))
    radius=10
    width = 150
    white = (255,255,255)
    gameWidth = 800
    gameHeight = 600
    black = (0,0,0)
    clock = pygame.time.Clock()
    font =  pygame.font.SysFont(None,50)
    gameExit = False
    global win
    Blocks=[[0 for xa in range(27*num)]for ya in range(13*num)]
    for ds in range(len(Blocks)):
        for dj in range(len(Blocks[ds])):
            ax=random.randrange(0,2)
            if ax==1:
                Blocks[ds][dj]=True
            else:
                Blocks[ds][dj]=False
    x=gameWidth/2-width/2
    y=gameHeight-100
    bx=x+width/2
    sd=False
    by=y-3*radius
    changeX=0
    changeBX=0
    height = 20
    bobob = False
    global buttonCooldown
    global score
    if num==1:
        score=0
    changeBY=0
    icon = pygame.image.load("RishavIcon.jpg")
    pygame.display.set_caption("Rishav's Game")
    pygame.display.set_icon(icon)
    while gameExit == False:
        if switch:
           color=(255,255,255)
        switch=False
        if color==(255,255,255):
            switch=True
            color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
        if image==pygame.image.load("BrickBreakerBackground.png"):
            clock.tick(1000)
        gameDisplay.blit(image , [0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                if not bobob:
                    bobob = True
                    changeBY=-9
                    changeBX=-9
                changeX=-15
            elif key[pygame.K_p]:
                paused()
            elif key[pygame.K_RIGHT]:
                if not bobob:
                    bobob=True
                    changeBY=-9
                    changeBX=9
                changeX=15
            else:
                changeX=0
            if key[pygame.K_SPACE] and admin:
                sd=True
        if (x>=gameWidth-width and changeX>0) or (x<=0 and changeX<0):
            changeX=0
        if by+2*radius>=y and by+2*radius<=y+height and bx+2*radius>=x and bx<=x+width:
            if changeX>0:
                changeBX=9
            elif changeX<0:
                changeBX=-9
            changeBY*=-1
            by-=5
        if bx<=0 or bx+2*radius>=gameWidth:
            changeBX*=-1
        if by<=0:
            by=3
            changeBY*=-1
        if by+2*radius>gameHeight  and not admin:
            gameExit=True
        x+=changeX
        by+=changeBY
        bx+=changeBX
        if button(770,0,30,33,"||",(255,255,255),775,2,4):
            paused()
        buttonCooldown+=1
        if by<390 and bx>0 and bx<1350:
            if Blocks[by/(30/num)-1][bx/(30/num)-1]:
                changeBY*=-1
                if Blocks[by/(30/num)-1][bx/(30/num)-1]:
                    score+=.1
                    Blocks[by/(30/num)-1][bx/(30/num)-1]=False
            if Blocks[by/(30/num)][bx/(30/num)-1]:
                changeBY*=-1
                if Blocks[by/(30/num)][bx/(30/num)-1]:
                    score+=.1
                    Blocks[by/(30/num)][bx/(30/num)-1]=False
            if Blocks[by/(30/num)-1][bx/(30/num)]:
                changeBY*=-1
                if Blocks[by/(30/num)-1][bx/(30/num)]:
                    score+=.1
                    Blocks[by/(30/num)-1][bx/(30/num)]=False
            if Blocks[by/(30/num)][bx/(30/num)]:
                changeBY*=-1
                if Blocks[by/(30/num)][bx/(30/num)]:
                    score+=.1
                    Blocks[by/(30/num)][bx/(30/num)]=False
        for d1 in range(len(Blocks)):
            for d2 in range(len(Blocks[d1])):
                if Blocks[d1][d2]:
                    if flashy:
                        pygame.draw.rect(gameDisplay, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (d2*30/num,d1*30/num,30/num,30/num))
                    else:
                        gameDisplay.blit(block,(d2*30/num,d1*30/num))
        person = pygame.draw.rect(gameDisplay, white, (x,y,width,height))
        ball = pygame.draw.circle(gameDisplay, color, (bx,by),radius)
        for qe in range(0,len(Blocks)):
            for ry in range(0,len(Blocks[qe])):
                if sd:
                    Blocks[qe][ry]=False
        win=True
        for qwe in range(0,len(Blocks)):
            for rty in range(0,len(Blocks[qwe])):
                if Blocks[qwe][rty]:
                    win = False
        if win:
            if num==1:
                global part
                global story
                if story:
                    part+=1
                    story_mode()
                num+=2
            else:
                num+=3
            brickBreaker()
        pygame.display.update()
    text =  font.render("YOU WIN!",True,black)
    gameDisplay.blit(text,[300,300])
    pygame.display.update()
    num=1
    playAgain()
def dodgeNEat():
    playagain = True
    global highScore
    global game_backround
    global pl
    global sM
    global image
    if game_backround:
        image = pygame.image.load("snake game backround.jpg")
        image = pygame.transform.scale(image,(800,600))
    image2 = pygame.image.load("Sword.png")
    image2 = pygame.transform.scale(image2,(60,40))
    global isk
    global score
    pl = random.randrange(1,2)
    while playagain == True:
        x = 400
        y = 300
        x2 = 300
        y2 = 300
        hack = False
        a=random.randrange(0,780)
        b=random.randrange(0,580)
        c=random.randrange(0,78)*10
        d=random.randrange(0,58)*10
        changeX =0
        changeY =0
        changeX2=0
        changeY2=0
        pl = random.randrange(1,2)
        Cchange=0
        Dchange=0
        global part
        global story
        if(competition):
            score = 15
        else:
            score=0
        global mP
        global mC
        global level
        global color
        gameDisplay.fill(white)
        gameExit = False
        while gameExit == False:
           global switch
           cheer = pygame.mixer.Sound("Cheering.wav")
           if score>=12 and story:
                part+=1
                story_mode()
           if score%10==0 and score!=0:
               cheer.play()
           if switch:
               color=(255,255,255)
           switch=False
           if color==(255,255,255):
               switch=True
               color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == 27:
                       pygame.quit()
                       quit()
                   if event.key == pygame.K_p:
                       paused()
                   if event.key == pygame.K_RIGHT:
                       if(level != 1):
                            changeX= 10*level/2
                       else:
                            changeX = 10
                       changeY = 0
                   if event.key == pygame.K_d:
                       if(level != 1):
                            changeX2 = 10*level/2
                       else:
                            changeX2 = 10
                       changeY2 = 0
                   if event.key == pygame.K_LEFT:
                       if(level != 1):
                            changeX= -10*level/2
                       else:
                            changeX = -10
                       changeY = 0
                       pause = False
                   if event.key == pygame.K_a:
                       if(level != 1):
                            changeX2= -10*level/2
                       else:
                            changeX2 = -10
                       changeY2 = 0
                   if event.key == pygame.K_UP:
                       if(level != 1):
                            changeY= -10*level/2
                       else:
                            changeY = -10
                       changeX = 0
                       pause = False
                   if event.key == pygame.K_w:
                       if(level != 1):
                            changeY2= -10*level/2
                       else:
                            changeY2 = -10
                       changeX2 = 0
                   if event.key == pygame.K_DOWN:
                       if(level != 1):
                            changeY= 10*level/2
                       else:
                            changeY = 10
                       changeX = 0
                       pause = False
                   if event.key == pygame.K_s:
                       if(level != 1):
                            changeY2= 10*level/2
                       else:
                            changeY2 = 10
                       changeX2 = 0
                   if event.key == pygame.K_TAB and admin:
                       score+=1
                       hack = True
                       Cchange=0
                       Dchange=0
               if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()
           if tC:
               if tP==1:
                    if pygame.mouse.get_pos()[0]>x+20:
                        if(level != 1):
                            changeX= 10*level/2
                        else:
                            changeX = 10
                        changeY = 0
                    if pygame.mouse.get_pos()[0]<x:
                        if(level != 1):
                            changeX= -10*level/2
                        else:
                            changeX = -10
                        changeY = 0
                    if pygame.mouse.get_pos()[1]<y:
                        if(level != 1):
                            changeY= -10*level/2
                        else:
                            changeY = -10
                        changeX = 0
                    if pygame.mouse.get_pos()[1]>y+50:
                        if(level != 1):
                            changeY= 10*level/2
                        else:
                            changeY = 10
                        changeX = 0
               if tP==2:
                    if pygame.mouse.get_pos()[0]>x2+20:
                        if(level != 1):
                            changeX2= 10*level/2
                        else:
                            changeX2 = 10
                        changeY2 = 0
                    if pygame.mouse.get_pos()[0]<x2:
                        if(level != 1):
                            changeX2= -10*level/2
                        else:
                            changeX2 = -10
                        changeY2 = 0
                    if pygame.mouse.get_pos()[1]<y2:
                        if(level != 1):
                            changeY2= -10*level/2
                        else:
                            changeY2 = -10
                        changeX2 = 0
                    if pygame.mouse.get_pos()[1]>y2+22:
                        if(level != 1):
                            changeY2= 10*level/2
                        else:
                            changeY2 = 10
                        changeX2 = 0

           if mC:
               if mP==1:
                    if pygame.mouse.get_pos()[0]>x+20 and pygame.mouse.get_pos()[1]<y+50 and pygame.mouse.get_pos()[1]>y-50:
                        if(level != 1):
                            changeX= 10*level/2
                        else:
                            changeX = 10
                        changeY = 0
                    if pygame.mouse.get_pos()[0]<x and pygame.mouse.get_pos()[1]<y+50 and pygame.mouse.get_pos()[1]>y-50:
                        if(level != 1):
                            changeX= -10*level/2
                        else:
                            changeX = -10
                        changeY = 0
                    if pygame.mouse.get_pos()[1]<y and pygame.mouse.get_pos()[0]<x+50 and pygame.mouse.get_pos()[0]>x-50:
                        if(level != 1):
                            changeY= -10*level/2
                        else:
                            changeY = -10
                        changeX = 0
                    if pygame.mouse.get_pos()[1]>y+50 and pygame.mouse.get_pos()[0]<x+50 and pygame.mouse.get_pos()[0]>x-50:
                        if(level != 1):
                            changeY= 10*level/2
                        else:
                            changeY = 10
                        changeX = 0
               if mP==2:
                    if pygame.mouse.get_pos()[0]>x2+20 and pygame.mouse.get_pos()[1]<y2+50 and pygame.mouse.get_pos()[1]>y2-50:
                        if(level != 1):
                            changeX2= 10*level/2
                        else:
                            changeX2 = 10
                        changeY2 = 0
                    if pygame.mouse.get_pos()[0]<x2 and pygame.mouse.get_pos()[1]<y2+50 and pygame.mouse.get_pos()[1]>y2-50:
                        if(level != 1):
                            changeX2= -10*level/2
                        else:
                            changeX2 = -10
                        changeY2 = 0
                    if pygame.mouse.get_pos()[1]<y2 and pygame.mouse.get_pos()[0]<x2+50 and pygame.mouse.get_pos()[0]>x2-50:
                        if(level != 1):
                            changeY2= -10*level/2
                        else:
                            changeY2 = -10
                        changeX2 = 0
                    if pygame.mouse.get_pos()[1]>y2+50 and pygame.mouse.get_pos()[0]<x2+50 and pygame.mouse.get_pos()[0]>x2-50:
                        if(level != 1):
                            changeY2= 10*level/2
                        else:
                            changeY2 = 10
                        changeX2 = 0

           e = random.randrange(1,4)
           f = random.randrange(1,6)
           fight()
           if(f == 1):
               if(e == 1):
                   Cchange=10*(int)(score/10)
                   Dchange=0
               if(e == 2):
                   Cchange=-10*(int)(score/10)
                   Dchange=0
               if(e == 3):
                   Dchange=10*(int)(score/10)
                   Cchange=0
               if(e == 4):
                   Dchange=-10*(int)(score/10)
                   Cchange=0
           if(e==0):
               Cchange=0
               Dchange=0
           if (x>=780 or x<=0) and not admin:
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           if(x2>=780 or x2<=0) and not admin:
               if(multiPlayer):
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           global we
           global qe
           global true
           global pop
           global fire
           global dM
           if story:
               dM=True
               sM=True
           if competition or v1:
               dM=False
               sM=False
           if sM and not fire:
               we=c
               qe=d
               true=True
               if qe>y and true:
                   pop=True
               elif true:
                   pop=False
           if true:
               if pop:
                   qe-=20
                   fire=True
                   pygame.draw.rect(gameDisplay,(0,0,0) , [we,qe, 20, 20])
                   pygame.display.update()
               else:
                   qe+=20
                   fire=True
                   pygame.draw.rect(gameDisplay,(0,0,0) , [we,qe, 20, 20])
                   pygame.display.update()
           if(((x>= we and x<= we+20) or (x+20>= we and x+20<= we+20))):
                if(((y>= qe and y<= qe+20) or (y+20>= qe and y+20<= qe+20))):
                    if sM and not admin:
                        gameExit=True
                        fire=False
                        true=False
           if(((x2>= we and x2<= we+20) or (x2+20>= we and x2+20<= we+20))):
                if(((y2>= qe and y2<= qe+20) or (y2+20>= qe and y2+20<= qe+20))):
                    if sM and multiPlayer and not admin:
                        gameExit=True
                        fire=False
                        true=False
           isk=(int)(score/5)+1
           if dM:
               for xyu in range(0,isk,1):
                  if xyu!=0:
                      if(xyu%4==0):
                         dc=c+20*4*(xyu/4)
                         dd=d+20*4*(xyu/4)
                      if(xyu%4==1):
                         dc=c-20*4*(xyu/4+1)
                         dd=d+20*4*(xyu/4+1)
                      if(xyu%4==2):
                         dc=c-20*4*(xyu/4+1)
                         dd=d-20*4*(xyu/4+1)
                      if(xyu%4==3):
                         dc=c+20*4*(xyu/4+1)
                         dd=d-20*4*(xyu/4+1)
                      pygame.draw.rect(gameDisplay,(255,255,255) , [dc,dd,20,20])
                      if(((x>= dc and x<= dc+20) or (x+20>= dc and x+20<= dc+20))):
                          if(((y>= dd and y<= dd+20) or (y+20>= dd and y+20<= dd+20))) and not admin:
                              gameExit=True
               pygame.display.update()
           level = (int)(score/10)+1
           if (we>=780 or we<=0):
                true=False
                fire=False
           if(qe>=580 or qe<=0):
               true=False
               fire=False
           g=20*(level-1)
           h=20
           if(level == 1):
               g=20
           if(((x>= a and x<= a+20) or (x+20>= a and x+20<= a+20))):
                if(((y>= b and y<= b+20) or (y+20>= b and y+20<= b+20))):
                   a=random.randrange(0,780)
                   b=random.randrange(0,580)
                   score+=1
                   pygame.mixer.music.pause()
                   if not v1:
                    crunch.play()
                   pygame.mixer.music.unpause()
           if v1:
               if pl==1:
                   changeX*=1.025
                   changeY*=1.025
               elif pl==2:
                   changeX2*=1.025
                   changeY2*=1.025
           if not v1:
               if(((x>= c and x<= c+g) or (x+20>= c and x+20<= c+g))):
                    if(((y>= d and y<= d+h) or (y+20>= d and y+20<= d+h))) and not admin:
                       gameExit = True
                       pygame.mixer.music.pause()
                       boing.play()
                       pygame.mixer.music.unpause()
           if(((x2>= a and x2<= a+20) or (x2+20>= a and x2+20<= a+20))):
                if(((y2>= b and y2<= b+20) or (y2+20>= b and y2+20<= b+20))):
                   if multiPlayer:
                       a=random.randrange(0,780)
                       b=random.randrange(0,580)
                       pygame.mixer.music.pause()
                       if not v1:
                        crunch.play()
                       pygame.mixer.music.unpause()
                       if(competition):
                           score-=1
                       else:
                           score+=1
           if not v1:
               if(((x2>= c and x2<= c+g) or (x2+20>= c and x2+20<= c+g))) and not admin:
                    if((y2>= d and y2<= d+h) or (y2+20>= d and y2+20<= d+h)):
                        if(multiPlayer):
                            gameExit = True
                            pygame.mixer.music.pause()
                            boing.play()
                            pygame.mixer.music.unpause()
           if(((x2>=x and x2<=x+20) or (x2+20>=x and x2+20<=x+20))):
               if(((y2>=y and y2<=y+20) or (y2+20>=y and y2+20<=y+20))) and not admin:
                   if(multiPlayer):
                    gameExit = True
                    pygame.mixer.music.pause()
                    boing.play()
                    pygame.mixer.music.unpause()
           if(score<=10 or score>=20) and not admin:
               if(competition):
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           global buttonCooldown
           if (y>=580 or y<=0) and not admin:
               gameExit = True
               pygame.mixer.music.pause()
               boing.play()
               pygame.mixer.music.unpause()
           if(y2>=580 or y2<=0) and not admin:
               if multiPlayer:
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           if (c>=780 or c<=0):
                c=a
                d=b
           if(d>=580 or d<=0):
               c=a
               d=b
           if(u!=0):
               changeX*=((1+u/50.0)**u)
               changeY*=((1+u/50.0)**u)
               Dchange*=((1+u/50.0)**u)
               Cchange*=((1+u/50.0)**u)
               changeX2*=((1+u/50.0)**u)
               changeY2*=((1+u/50.0)**u)
           elif(u==0):
               changeX*=(1+u/50.0)
               changeY*=(1+u/50.0)
               changeX2*=(1+u/50.0)
               changeY2*=(1+u/50.0)
               Dchange*=(1+u/50.0)
               Cchange*=(1+u/50.0)
           d+=Dchange
           c+=Cchange
           x+= changeX
           y+= changeY
           x2+= changeX2
           y2+= changeY2
           if(Cchange!=0):
               g=20*(level-1)
               h=20
           if Dchange!=0:
               g=20
               h=20*(level-1)
           if(score>highScore and hack== False and competition == False and v1==False):
               highScore=score
           clock.tick(30)
           gameDisplay.fill(white)
           gameDisplay.blit(image,(0,0))
           if button(770,0,30,33,"||",white,775,2,4):
               paused()
           person = pygame.Rect(x, y, 20, 20)
           pygame.draw.rect(gameDisplay, color , person)
           buttonCooldown+=1
           if not v1:
               pygame.draw.rect(gameDisplay,(255,0,0) , [a,b, 20, 20])
           if(multiPlayer):
               person2 = pygame.Rect(x2, y2, 20, 20)
               pygame.draw.rect(gameDisplay, color2 , person2)
           global wins2
           global wins1
           if v1:
               if pl == 1:
                   gameDisplay.blit(image2,(x-25,y-10))
               elif pl == 2:
                   gameDisplay.blit(image2,(x2-25,y2-10))
           if not v1:
               pygame.draw.rect(gameDisplay,(255,255,255) , [c,d,g,h])
               messageOnScreen("Score: "+str(score),10,10,(255,0,255),2.5)
               if(competition == False):
                   messageOnScreen("Level: "+str(level),10,40,(255,0,255),2.5)
                   messageOnScreen("Highest Score:"+str(highScore),10,70,(255,0,255),2.5)
               elif competition:
                   messageOnScreen("Player 1 wins: "+str(wins1),10,40,(255,0,255),2.5)
                   messageOnScreen("Player 2 wins: "+str(wins2),10,70,(255,0,255),2.5)
           elif v1:
               messageOnScreen("Player "+str(pl)+" is attacking",10,10,(255,0,255),2.5)
               messageOnScreen("Player 1 wins: "+str(wins1),10,40,(255,0,255),2.5)
               messageOnScreen("Player 2 wins: "+str(wins2),10,70,(255,0,255),2.5)
           pygame.display.update()
        if playagain == True:
            pygame.draw.rect(gameDisplay,(255,255,255) , [270,200,300,300])
            if(competition):
                if(score<=10):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                elif(score>=20):
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
                elif(((x2>=x and x2<=x+20) or (x2+20>=x and x2+20<=x+20)))and(((y2>=y and y2<=y+20) or (y2+20>=y and y2+20<=y+20))):
                    if competition:
                        if score>15:
                            messageOnScreen("Player 1 wins",300,270,(0,0,255),2.5)
                        elif score<15:
                            messageOnScreen("Player 2 wins",300,270,(0,0,255),2.5)
                    if not competition or score==15:
                        messageOnScreen("You Both Lose!",300,270,(0,0,255),2.5)
                elif(((x2>= c and x2<= c+g) or (x2+20>= c and x2+20<= c+g)))and((y2>= d and y2<= d+h) or (y2+20>= d and y2+20<= d+h)):
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
                elif(((x>= c and x<= c+g) or (x+20>= c and x+20<= c+g)))and (((y>= d and y<= d+h) or (y+20>= d and y+20<= d+h))):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                elif(y2>=560 or y2<=20):
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
                elif(y>=560 or y<=20):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                elif(x>=760 or x<=20):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                else:
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
            elif(v1):
                if(y2>=560 or y2<=20):
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
                elif(y>=560 or y<=20):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                elif(x>=760 or x<=20):
                    wins2+=1
                    messageOnScreen("Player two wins",300,270,(0,0,255),2.5)
                elif(x2>=760 or x2<=20):
                    wins1+=1
                    messageOnScreen("Player one wins",300,270,(0,0,255),2.5)
                elif(((x2>=x and x2<=x+20) or (x2+20>=x and x2+20<=x+20)))and(((y2>=y and y2<=y+20) or (y2+20>=y and y2+20<=y+20))):
                    messageOnScreen("Player "+str(pl)+" wins",300,270,(0,0,255),2.5)
                    if pl==1:
                        wins1+=1
                    if pl ==2:
                        wins2+=1
            else:
                messageOnScreen("You Lose!",300,270,(0,0,255),2.5)
            if not v1 and not competition:
                messageOnScreen("Score: "+str(score),300,320,(0,0,255),2.5)
            if(score == highScore and hack ==False and competition==False and v1 == False):
                cheer.play()
            if(hack and not v1):
                messageOnScreen("You Hacked!",300,470,(0,0,255),2.5)
            playAgain2()
            pygame.display.update()
def paused():
    pause=True
    pygame.mixer.music.pause()
    pygame.draw.rect(gameDisplay,(255,255,255) , [50,240,730,140])
    messageOnScreen("Paused",350,250,(0,0,0),2.5)
    pygame.display.update()
    global buttonCooldown
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    for ut in range(3,0,-1):
                        pygame.draw.rect(gameDisplay,(255,255,255), [390,90+(3-ut)*40,20,30])
                        messageOnScreen(str(ut),395,100+(3-ut)*40,(0,0,0),2.5)
                        pygame.display.update()
                        pygame.mixer.Sound("beep.wav").play()
                        time.sleep(1)
                    for john in range(1,20):
                        messageOnScreen("Start!",random.randrange(0,750),random.randrange(0,550),(255,0,255),john)
                        time.sleep(.1)
                        pygame.display.update()
                    pygame.mixer.Sound("beep2.wav").play()
                    time.sleep(1)
                    pygame.mixer.music.unpause()
                    pause=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_m:
                    pause=False
                    pygame.mixer.music.unpause()
                    mainMenu()
                elif event.key==pygame.K_s:
                    pause = False
                    pygame.mixer.music.unpause()
                    mainGame()
        clock.tick(500)
        buttonCooldown+=1
        if button(480,320,210,50,"Main Menu (M)",(255,0,0),481,330,4):
            pause=False
            pygame.mixer.music.unpause()
            mainMenu()
        if button(270,320,200,50,"Start Over (S)",(0,0,255),280,330,4):
            pause=False
            pygame.mixer.music.unpause()
            mainGame()
        if button(60,320,200,50,"Continue (C)",(0,255,0),70,330,4):
            for ut in range(3,0,-1):
                pygame.draw.rect(gameDisplay,(255,255,255), [390,90+(3-ut)*40,20,30])
                messageOnScreen(str(ut),395,100+(3-ut)*40,(0,0,0),2.5)
                pygame.display.update()
                pygame.mixer.Sound("beep.wav").play()
                time.sleep(1)
            for john in range(1,20):
                messageOnScreen("Start!",random.randrange(0,750),random.randrange(0,550),(255,0,255),john)
                time.sleep(.1)
                pygame.display.update()
            pygame.mixer.Sound("beep2.wav").play()
            time.sleep(1)
            pygame.mixer.music.unpause()
            pause=False
        pygame.display.update()
def password(password):
    enter = False
    global admin
    global buttonCooldown
    s=""
    while enter == False:
        gameDisplay.fill((255,255,255))
        pygame.draw.line(gameDisplay,(0,0,0), (350,125),(730,125),1)
        messageOnScreen("Cheat Code: ",200,100,(0,0,0),3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 8:
                    temp=""
                    for weu in range(len(s)-1):
                        temp+=s[weu]
                    s=temp
                elif event.key == 13:
                    enter=True
                elif (event.key>=32 and event.key<=126):
                    s+=chr(event.key)
        messageOnScreen(s,350,100,(0,0,0),3)
        if button(350,400,300,40,"Skip or Enter (enter)",(255,0,255),370,410,3):
            enter=True
        buttonCooldown+=1
        pygame.display.update()
    admin=False
    if s==password:
        admin=True
def messageOnScreen(msg,x,y,color,size=4.0):
    font =  pygame.font.SysFont(None,int(size*10))
    text =  font.render(msg,True,color)
    gameDisplay.blit(text,[x,y])
def button(x,y,lengthX,lengthY,text,rect,textX,textY,textSize=4.0,color=(0,0,0)):
    pos = pygame.mouse.get_pos()
    picture='bob'
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y:
        if type(rect)==tuple:
            if rect[0]<246:
                rect1=rect[0]+50
            else:
                rect1=rect[0]-50
            if rect[1]<246:
                rect2=rect[1]+50
            else:
                rect2=rect[1]-50
            if rect[2]<246:
                rect3=rect[2]+50
            else:
                rect3=rect[2]-50
            rect=(rect1,rect2,rect3)
    global buttonCooldown
    if type(rect)==str:
        picture=pygame.image.load(rect)
        picture = pygame.transform.scale(picture,(lengthX,lengthY))
        if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y:
            if type(rect)==str:
                dark = pygame.Surface((picture.get_width(), picture.get_height()), flags=pygame.SRCALPHA)
                dark.fill((30, 30, 30, 0))
                picture.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        gameDisplay.blit(picture, (x,y))
    else:
        rectangle=pygame.Rect(x,y,lengthX,lengthY)
        pygame.draw.rect(gameDisplay, rect, rectangle)

    messageOnScreen(text,textX,textY, color ,textSize)
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y and (pygame.mouse.get_pressed()[2]==1 or pygame.mouse.get_pressed()[0] == 1) and buttonCooldown>30:
        buttonCooldown=0
        return True
    else:
        return False
def fight():
    global pl
    ef= random.randrange(0,300)
    if ef == 1:
        if pl==1:
            pl = 2
        else:
            pl = 1
def playAgain():
    global score
    pygame.draw.rect(gameDisplay,white,(180,180,450,250))
    messageOnScreen("YOU LOSE!",300,200,black,4)
    messageOnScreen("Score: "+str(score),300,250,black,4)
    messageOnScreen("Would you like to play again?",200,300,black,4)
    sg=True
    global boss
    global buttonCooldown
    pygame.display.update()
    while sg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_y]:
                if boss:
                    boss_fight()
                else:
                    mainGame()
            if key[pygame.K_n]:
                mainMenu()
        if button(200,350,200,40,"Yes (Y)",(0,255,0),245,355,4):
            if boss:
                boss_fight()
            else:
                mainGame()
        if button(410,350,200,40,"No (N)",(255,0,0),455,355,4):
            mainMenu()
        buttonCooldown+=1
        pygame.display.update()
def playAgain2():
    gameLoop = False
    global win
    global hacked
    global score
    global highScore
    global buttonCooldown
    messageOnScreen("Would You Like To Play Again?",300,370,(0,0,255),2.5)
    pygame.display.update()
    while gameLoop == False:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_y:
                   mainGame()
               if event.key == pygame.K_n:
                   mainMenu()
        if button(300,400,200,40,"Yes (Y)",(0,255,0),345,405,4):
            mainGame()
        if button(300,450,200,40,"No (N)",(255,0,0),355,455,4):
            mainMenu()
        buttonCooldown+=1
        pygame.display.update()
def music():
    global s
    pygame.mixer.music.load(s)
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(.1)
class dodge_n_eat_settings():
    def settings(self):
        global buttonCooldown
        global multiPlayer
        global v1
        global competition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if multiPlayer:
                        multiPlayer=False
                        competition=False
                        v1=False
                    else:
                        multiPlayer=True
                if event.key == pygame.K_g:
                    self.game_modes()
                if event.key == pygame.K_o:
                    self.control_settings()
                if event.key == pygame.K_d:
                    self.difficulty_settings()
        if multiPlayer:
            if button(10,250,780,30,"Multiplayer (P)",(0,255,0),20,260,2.5):
                multiPlayer=False
                v1=False
                competition=False
        else:
            if button(10,250,780,30,"Multiplayer (P)",(255,0,0),20,260,2.5):
                multiPlayer=True
        if button(10,290,780,30,"Game Modes (G)",(0,0,255),20,300,2.5):
            self.game_modes()
        if button(10,330,780,30,"Control Settings (O)",(0,0,255),20,340,2.5):
            self.control_settings()
        if button(10,370,780,30,"Difficulty Level (D)",(0,0,255),20,380,2.5):
            self.difficulty_settings()
        buttonCooldown+=1
        pygame.display.update()
    def control_settings(self):
        global tC
        global tP
        global mC
        global mP
        global buttonCooldown
        global multiPlayer
        bobIsBoss=True
        while bobIsBoss:
            gameDisplay.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        bobIsBoss=False
                        mainMenu()
                    if event.key == pygame.K_o:
                        if mC and mP==2:
                            mC=False
                        else:
                            mC=True
                            mP=2
                            tC=False
                    if event.key == pygame.K_r:
                        if tC and tP==2:
                            tC=False
                        else:
                            tC=True
                            mC=False
                            tP=2
                    if event.key == pygame.K_l:
                        if mC and mP==1:
                            mC=False
                        else:
                            mC=True
                            mP=1
                            tC=False
                    if event.key == pygame.K_a:
                        if tC and tP==1:
                            tC=False
                        else:
                            tC=True
                            mC=False
                            tP=1
            buttonCooldown+=1
            if multiPlayer:
                if mC and mP==2:
                    if button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(0,255,0),20,170,4) :
                        mC=False
                else:
                    if button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(255,0,0),20,170,4):
                        mC=True
                        mP=2
                        tC=False
                if tC and tP==2:
                    if button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(0,255,0),20,270,4):
                        tC=False
                else:
                    if button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(255,0,0),20,270,4):
                        tC=True
                        mC=False
                        tP=2
            else:
                if mP==2:
                    mC=False
                if tP==2:
                    tC=False
                button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(100,100,100),20,170,4)
                button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(100,100,100),20,270,4)
            if mC and mP==1:
                if button(10,110,780,40,"Mouse Control(player 1)(in line)(L)",(0,255,0),20,120,4):
                    mC=False
            else:
                if button(10,110,780,40,"Mouse Control(player 1)(in line)(L)",(255,0,0),20,120,4):
                    mC=True
                    mP=1
                    tC=False
            if tC and tP==1:
                if button(10,210,780,40,"Mouse Control(player 1)(anywhere)(A)",(0,255,0),20,220,4):
                    tC=False
                    qwe=0
            else:
                if button(10,210,780,40,"Mouse Control(player 1)(anywhere)(A)",(255,0,0),20,220,4):
                    tC=True
                    mC=False
                    tP=1
            if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560,4):
                bobIsBoss=False
                mainMenu()
            pygame.display.update()
    def difficulty_settings(self):
        global u
        bobISboss=True
        global buttonCooldown
        while bobISboss:
            gameDisplay.fill(black)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_a:
                       u = 4
                       bobISboss=False
                   if event.key == pygame.K_x:
                       mainMenu()
                   if event.key == pygame.K_e:
                       u = 0
                       bobISboss=False
                   if event.key == pygame.K_n:
                       u = 1
                       bobISboss=False
                   if event.key == pygame.K_h:
                       u = 2
                       bobISboss=False
                   if event.key == pygame.K_i:
                       u = 3
                       bobISboss=False
            if button(10,10,300,50,"Easy (e)",white,20,20):
                u=0
                bobISboss=False
            if button(10,70,300,50,"Normal (n)",white,20,80):
                u=1
                bobISboss=False
            if button(10,130,300,50,"Hard (h)",white,20,140):
                u=2
                bobISboss=False
            if button(10,190,300,50,"Insane (i)",white,20,200):
                u=3
                bobISboss=False
            if button(10,250,300,50,"Are you CRAZY? (a)",white,20,260):
                u=4
                bobISboss=False
            if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560,4):
                bobISboss=False
                mainMenu()
            buttonCooldown+=1
            pygame.display.update()
    def game_modes(self):
        global dM
        global competition
        global v1
        global sM
        global buttonCooldown
        global multiPlayer
        bobIsBoss=True
        while bobIsBoss:
            gameDisplay.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        bobIsBoss=False
                        mainMenu()
                    if event.key == pygame.K_f:
                        if v1:
                            v1=False
                        else:
                            v1=True
                            sM=False
                            dM=False
                            competition=False
                    if event.key == pygame.K_c:
                        if competition:
                            competition=False
                        else:
                            competition=True
                            v1=False
                    if event.key == pygame.K_w:
                        if not competition and not v1:
                            competition=True
                        else:
                            competition=False
                            v1=False
                    if event.key == pygame.K_d and not v1:
                        if dM:
                            dM=False
                        else:
                            dM=True
                            v1=False
                    if event.key == pygame.K_s and not v1:
                        if sM:
                            sM=False
                        else:
                            sM=True
                            v1=False
            buttonCooldown+=1
            if multiPlayer:
                if v1:
                    if button(10,110,780,40,"Fight (F)",(0,255,0),272,120,4):
                        v1=False
                else:
                    if button(10,110,780,40,"Fight (F)",(255,0,0),272,120,4):
                        v1=True
                        sM=False
                        dM=False
                        competition=False
                if competition:
                    if button(10,160,780,40,"Score Compete(C)",(0,255,0),272,170,4):
                        competition=False
                else:
                    if button(10,160,780,40,"Score Compete(C)",(255,0,0),272,170,4):
                        competition=True
                        v1=False
                if not competition and not v1:
                    if button(10,210,780,40,"Work Together(W)",(0,255,0),272,220,4):
                        competition=True
                else:
                    if button(10,210,780,40,"Work Together(W)",(255,0,0),272,220,4):
                        competition=False
                        v1=False
            else:
                v1=False
                competition=False
                button(10,110,780,40,"Fight (F)",(100,100,100),272,120,4)
                button(10,160,780,40,"Score Compete(C)",(100,100,100),272,170,4)
                button(10,210,780,40,"Work Together(W)",(100,100,100),272,220,4)
            if not v1:
                if dM:
                    if button(10,10,780,40,"Duplicate Mode(D)",(0,255,0),272,20,4):
                        dM=False
                else:
                    if button(10,10,780,40,"Duplicate Mode(D)",(255,0,0),272,20,4):
                        dM=True
                        v1=False
                if sM:
                    if button(10,60,780,40,"Shooting Mode(S)",(0,255,0),272,70,4):
                        sM=False
                else:
                    if button(10,60,780,40,"Shooting Mode(S)",(255,0,0),272,70,4):
                        sM=True
                        v1=False
            else:
                button(10,10,780,40,"Duplicate Mode(D)",(100,100,100),272,20,4)
                button(10,60,780,40,"Shooting Mode(S)",(100,100,100),272,70,4)
                dM=False
                sM=False
            if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560,4):
                bobIsBoss=False
                mainMenu()
            pygame.display.update()
class none():
    def settings(self):
        pass
class brick_breaker_settings():
    def settings(self):
        global flashy
        if flashy:
            if button(10,250,780,30,"Flashy (f)",(0,255,0),20,260,2.5):
                flashy=False
        else:
            if button(10,250,780,30,"Flashy (f)",(255,0,0),20,260,2.5):
                flashy= True
music()
mainMenu()
