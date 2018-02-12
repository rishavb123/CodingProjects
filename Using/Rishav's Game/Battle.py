
import pygame  # pygame is a gaming module with things built in to make game coding easier
import random
import time
pygame.init()  # init is short for initialize... it initializes the game and all the modules available for you to use

gameDisplay = pygame.display.set_mode((800,600)) # creates a display and returns a surface object
height = 600
width = 800
score=0
clock = pygame.time.Clock()
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Rishav's Game")
pygame.display.set_icon(icon)
font =  pygame.font.SysFont(None,30)
background = pygame.image.load("Arena.jpg")
background = pygame.transform.scale(background , (800,600))
def type():
    enter = False
    s=""
    while enter == False:
        gameDisplay.fill((255,255,255))
        pygame.draw.line(gameDisplay,(0,0,0), (350,125),(730,125),1)
        messageOnScreen("Cheat Code: ",200,100,(0,0,0),3)
        messageOnScreen("Click enter to skip",350,400,(0,0,0),3)
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
                    s+=chr(event.key)
        messageOnScreen(s,350,100,(0,0,0),3)
        pygame.display.update()
    return s
def battle():
    x=400
    y=300
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
    while gameExit == False:
        sleep=False
        dash = False
        clock.tick(1000000000000)
        level = int(score/10)+1
        gameDisplay.blit(background, (0,0))
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
        if button(770,0,30,33,"||",(255,255,255),775,2):
            paused()
        mr+=1
        ml+=1
        mu+=1
        md+=1
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
            if o<2:
                weapon="none"
            elif o==3:
                weapon="sheild"
            elif o==4 or o==5:
                weapon="freeze"
            elif o>=6 and o<9:
                weapon="gun"
            elif o==9 or o==10:
                weapon="bomb"
            elif o==2:
                weapon="stealth"
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
            if not enemies[sb][3]!="stealth":
                pygame.draw.rect(gameDisplay, (0,0,0),[enemies[sb][0],enemies[sb][1],20,20])
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
            pygame.draw.rect(gameDisplay, (255,0,255) , [x,y,20,20])
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
    playAgain()
def mainMenu():
    pygame.draw.rect(gameDisplay, (255,255,255),[0,0,800,600])
    messageOnScreen("Welcome to Battle",240,100,(255,0,255),5)
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
    battle()
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
def paused():
    pause=True
    pygame.mixer.music.pause()
    pygame.draw.rect(gameDisplay,(255,255,255) , [50,240,730,140])
    messageOnScreen("Paused",350,250,(0,0,0),2.5)
    global MM
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
                    battle()
        clock.tick(5)
        if button(480,320,210,50,"Main Menu (M)",(255,0,0),481,330):
            pause=False
            pygame.mixer.music.unpause()
            mainMenu()
        if button(270,320,200,50,"Start Over (S)",(0,0,255),280,330):
            pause=False
            pygame.mixer.music.unpause()
            battle()
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
                battle()
            if key[pygame.K_n]:
                mainMenu()
        if button(200,350,200,40,"Yes (Y)",(0,255,0),245,355):
            battle()
        if button(410,350,200,40,"No (N)",(255,0,0),455,355):
            mainMenu()
        pygame.display.update()
password=type()
admin=False
if password=="rishavisboss":
    admin=True
mainMenu()
