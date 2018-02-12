import pygame  # pygame is a gaming module with things built in to make game coding easier
import time
import random
pygame.init()
width = 800
height = 600
score=0
gameDisplay = pygame.display.set_mode((width,height)) # creates a display and returns a surface object
white = (255,255,255)
black = (0,0,0)
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(icon)
gameDisplay.fill(white)
clock = pygame.time.Clock()
font =  pygame.font.SysFont(None,20)
def flappyBird():
    gameExit = False
    global score
    x=400
    y=300
    move=False
    bob=0
    bob2=0
    score = 0
    holes1=[]
    holes2=[]
    tunnels=[]
    backround = pygame.image.load("FlappyBirdBackround.jpg")
    backround = pygame.transform.scale(backround,(800,600))
    bird= pygame.image.load("Bird.png")
    bird = pygame.transform.scale(bird,(20,20))
    for ui in range(20):
        tunnels.append(False)
        holes1.append(0)
        holes2.append(0)
    while gameExit == False:
        clock.tick(1000)
        gameDisplay.blit(backround,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed()[0]==1 or event.type == pygame.KEYDOWN:
                y+=-50
                bob=0
                move=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
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
                    else:
                        gameExit=True
        bob2+=1
        bob+=1
        if button(770,0,30,33,"||",(255,255,255),775,2):
            paused()
        if y>=580 or y<0:
            gameExit=True
        clock.tick(400)
        gameDisplay.blit(bird,(x,y))
        if move:
            y+=200*bob/1500
        messageOnScreen("Score: "+str(score),10,10,(0,0,0),3)
        pygame.display.update()
    playAgain()
def messageOnScreen(msg,x,y,color,size):
    font =  pygame.font.SysFont(None,int(size*10))
    text =  font.render(msg,True,color)
    gameDisplay.blit(text,[x,y])
def mainMenu():
    pygame.draw.rect(gameDisplay, (255,255,255),[0,0,800,600])
    messageOnScreen("Welcome to Flappy Bird",200,100,(255,0,255),5)
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
        if button(200,250,400,80,"Play (Y)",(0,255,0),350,270) and bob>10:
            gameStart=True
        if button(200,350,400,80,"Quit (Q)",(255,0,0),350,370) and bob>10:
            quit()
            pygame.quit()
        pygame.display.update()
    flappyBird()
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
    pygame.draw.rect(gameDisplay,white,(180,180,450,250))
    messageOnScreen("YOU LOSE!",300,200,black,4)
    messageOnScreen("Score: "+str(score),300,250,black,4)
    messageOnScreen("Would you like to play again?",200,300,black,4)
    sg=True
    pygame.display.update()
    while sg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_y]:
                flappyBird()
            if key[pygame.K_n]:
                mainMenu()
        if button(200,350,200,40,"Yes (Y)",(0,255,0),245,355):
            flappyBird()
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
                    flappyBird()
        clock.tick(5)
        if button(480,320,210,50,"Main Menu (M)",(255,0,0),481,330):
            pause=False
            pygame.mixer.music.unpause()
            mainMenu()
        if button(270,320,200,50,"Start Over (S)",(0,0,255),280,330):
            pause=False
            pygame.mixer.music.unpause()
            flappyBird()
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