import pygame  # pygame is a gaming module with things built in to make game coding easier
import random
import time
pygame.init()  # init is short for initialize... it initializes the game and all the modules available for you to use

gameDisplay = pygame.display.set_mode((800,600)) # creates a display and returns a surface object
height = 600
font =  pygame.font.SysFont(None,40)
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Rishav's Game")
pygame.display.set_icon(icon)
width = 800
highScore=0
b=1
score=0
def button(x,y,lengthX,lengthY,text,color,textX,textY):
    pos = pygame.mouse.get_pos()
    rectangle=pygame.Rect(x,y,lengthX,lengthY)
    pygame.draw.rect(gameDisplay, color, rectangle)
    messageOnScreen(text,textX,textY, (0,0,0) ,4)
    pygame.display.update()
    if x+lengthX> pos[0] > x and y+lengthY> pos[1] > y and pygame.mouse.get_pressed()[0] == 1:
        return True
    else:
        return False
def crossyRoad():
    x = 400
    y = 560
    global width
    global highScore
    global height
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
    while gameExit == False:
        broken = True
        gameDisplay.fill((255,255,255))
        cars=[]
        logs=[]
        if score>highScore:
            highScore=score
        if x>width-20 or x<0 or y>680:
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
            crossyRoad()
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
                        if y==u*20:
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
                elif x+20<posW[w] or x>posW[w]+50:
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
        pygame.draw.rect(gameDisplay, (0,0,0), (x,y,20,20))
        messageOnScreen("Score "+str(score),10,10,(0,0,0),3)
        messageOnScreen("Highest Score:"+str(highScore),10,30,(255,0,255),3)
        pygame.display.update()
    playAgain()
def mainMenu():
    pygame.draw.rect(gameDisplay, (255,255,255),[0,0,800,600])
    messageOnScreen("Welcome to Crossy Road",200,100,(255,0,255),5)
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
    crossyRoad()
    crossyRoad()
def messageOnScreen(msg,x,y,color,size):
    font =  pygame.font.SysFont(None,size*10)
    text =  font.render(msg,True,color)
    gameDisplay.blit(text,[x,y])
def playAgain():
    global score
    pygame.draw.rect(gameDisplay,(255,255,255),(180,180,450,250))
    messageOnScreen("YOU LOSE!",300,200,(0,0,0),4)
    messageOnScreen("Score: "+str(score),300,250,(0,0,0),4)
    messageOnScreen("Would you like to play again?",200,300,(0,0,0),4)
    sg=True
    pygame.display.update()
    score=0
    while sg:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_y]:
                crossyRoad()
            if key[pygame.K_n]:
                mainMenu()
        if button(200,350,200,40,"Yes (Y)",(0,255,0),245,355):
            crossyRoad()
        if button(410,350,200,40,"No (N)",(255,0,0),455,355):
            mainMenu()
mainMenu()

