
import pygame  # pygame is a gaming module with things built in to make game coding easier
import random
import time
import ImageDownloader

pygame.init()  # init is short for initialize... it initializes the game and all the modules available for you to use

gameDisplay = pygame.display.set_mode((800,600)) # creates a display and returns a surface object
height = 600
width = 800
num=1
color = (255,0,0)
score=0
flashy=False
clock = pygame.time.Clock()
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Brick Breaker")
pygame.display.set_icon(icon)
font =  pygame.font.SysFont(None,30)
def brickBreaker():
    global color
    global num
    global flashy
    image = pygame.image.load("block.jpg")
    background = pygame.image.load("BrickBreakerBackground.png")
    background = pygame.transform.scale(background,(800,600))
    image = pygame.transform.scale(image,(30/num,30/num))
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
    global score
    if num==1:
        score=0
    changeBY=0
    icon = pygame.image.load("RishavIcon.jpg")
    pygame.display.set_caption("Rishav's Game")
    pygame.display.set_icon(icon)
    while gameExit == False:
        clock.tick(1000)
        gameDisplay.blit(background , [0,0])
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
            if key[pygame.K_SPACE]:
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
        if by+2*radius>gameHeight:
            gameExit=True
        x+=changeX
        by+=changeBY
        bx+=changeBX
        if button(770,0,30,33,"||",(255,255,255),775,2):
            paused()
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
                        gameDisplay.blit(image,(d2*30/num,d1*30/num))
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
def mainMenu():
    global flashy
    pygame.draw.rect(gameDisplay, (255,255,255),[0,0,800,600])
    messageOnScreen("Welcome to Brick Breaker",190,100,(255,0,255),5)
    gameStart = False
    pygame.display.update()
    bob=0
    while not gameStart:
        bob+=1
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                   quit()
                   pygame.quit()
               if event.key == pygame.K_y:
                   gameStart=True
               if event.key == pygame.K_f:
                   flashy=True
               if event.key == pygame.K_b:
                   flashy=False
        if button(200,250,400,80,"Play (Y)",(0,255,0),350,270) and bob>10:
            gameStart=True
        if not flashy:
            if button(200,350,400,80,"Flashy? (F)",(0,0,255),350,370) and bob>100:
                flashy=True
                bob=0
        else:
            if button(200,350,400,80,"Blocks? (B)",(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),350,370) and bob>100:
                flashy=False
                bob=0
        if button(200,450,400,80,"Quit (Q)",(255,0,0),350,470) and bob>10:
            quit()
            pygame.quit()
        pygame.display.update()
    brickBreaker()
def messageOnScreen(msg,x,y,color,size):
    font =  pygame.font.SysFont(None,int(size*10))
    text =  font.render(msg,True,color)
    gameDisplay.blit(text,[x,y])
def button(x,y,lengthX,lengthY,text,color,textX,textY):
    pos = pygame.mouse.get_pos()
    rectangle=pygame.Rect(x,y,lengthX,lengthY)
    pygame.draw.rect(gameDisplay, color, rectangle)
    messageOnScreen(text,textX,textY, (0,0,0) ,4)
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y and pygame.mouse.get_pressed()[0] == 1:
        return True
    else:
        return False
def playAgain():
    global score
    pygame.draw.rect(gameDisplay,(255,255,255),(180,180,450,250))
    messageOnScreen("YOU LOSE!",300,200,(0,0,0),4)
    messageOnScreen("Score: "+str(score),300,250,(0,0,0),4)
    messageOnScreen("Would you like to play again?",200,300,(0,0,0),4)
    sg=True
    pygame.display.update()
    while sg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_y]:
                brickBreaker()
            if key[pygame.K_n]:
                mainMenu()
        if button(200,350,200,40,"Yes (Y)",(0,255,0),245,355):
            brickBreaker()
        if button(410,350,200,40,"No (N)",(255,0,0),455,355):
            mainMenu()
        pygame.display.update()
def paused():
    pause=True
    pygame.mixer.music.pause()
    pygame.draw.rect(gameDisplay,(255,255,255) , [50,240,730,140])
    messageOnScreen("Paused",350,250,(0,0,0),2.5)
    pygame.display.update()
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
                    brickBreaker()
        clock.tick(5)
        if button(480,320,210,50,"Main Menu (M)",(255,0,0),481,330):
            pause=False
            pygame.mixer.music.unpause()
            mainMenu()
        if button(270,320,200,50,"Start Over (S)",(0,0,255),280,330):
            pause=False
            pygame.mixer.music.unpause()
            brickBreaker()
        if button(60,320,200,50,"Continue (C)",(0,255,0),70,330):
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
mainMenu()