import pygame
import random
import time
pygame.init()
boing = pygame.mixer.Sound("Boing.wav")
cheer = pygame.mixer.Sound("Cheering.wav")
crunch = pygame.mixer.Sound("Crunch.wav")
width = 800
fire=False
height = 600
switch = False
v1 = False
gameDisplay = pygame.display.set_mode((width,height))
image = pygame.image.load("snake game backround.jpg")
image = pygame.transform.scale(image,(800,600))
image2 = pygame.image.load("Sword.png")
image2 = pygame.transform.scale(image2,(60,40))
icon = pygame.image.load("RishavIcon.jpg")
font =  pygame.font.SysFont(None,25)
white = (255,255,255)
black = (0,0,0)
dM=False
qe=10000
pygame.display.set_caption("Rishav's Game")
pygame.display.set_icon(icon)
we=1000
true=False
sM=False
hacked = False
clock = pygame.time.Clock()
gameLoop = False
score = 0
mC = False
mP = 1
tC =False
tP=1
s="Cool Music.mp3"
changeX = 0
changeY = 0
cross=False
wins1 = 0
wins2 = 0
MM= True
changeX2 = 0
changeY2 = 0
level = (int)(score/10)+1
multiPlayer = False
isk=(int)(score/5)+1
blue = (0,0,255)
color = white
color2 = white
u = 0
competition = False
pl = random.randrange(1,2)
highScore = 0
def dodgeNEat():
    playagain = True
    global highScore
    global pl
    global sM
    global image
    global image2
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
           if score%10==0 and score!=0:
               cheer.play()
           if switch:
               color=(255,255,255)
               color2 = (255,255,255)
           switch=False
           if color==(255,255,255):
               switch=True
               color = random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
               color2 =random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)
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
                   if event.key == pygame.K_TAB:
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
           if (x>=780 or x<=0):
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           if(x2>=780 or x2<=0):
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
                    if sM:
                        gameExit=True
                        fire=False
                        true=False
           if(((x2>= we and x2<= we+20) or (x2+20>= we and x2+20<= we+20))):
                if(((y2>= qe and y2<= qe+20) or (y2+20>= qe and y2+20<= qe+20))):
                    if sM and multiPlayer:
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
                          if(((y>= dd and y<= dd+20) or (y+20>= dd and y+20<= dd+20))):
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
                    if(((y>= d and y<= d+h) or (y+20>= d and y+20<= d+h))):
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
               if(((x2>= c and x2<= c+g) or (x2+20>= c and x2+20<= c+g))):
                    if((y2>= d and y2<= d+h) or (y2+20>= d and y2+20<= d+h)):
                        if(multiPlayer):
                            gameExit = True
                            pygame.mixer.music.pause()
                            boing.play()
                            pygame.mixer.music.unpause()
           if(((x2>=x and x2<=x+20) or (x2+20>=x and x2+20<=x+20))):
               if(((y2>=y and y2<=y+20) or (y2+20>=y and y2+20<=y+20))):
                   if(multiPlayer):
                    gameExit = True
                    pygame.mixer.music.pause()
                    boing.play()
                    pygame.mixer.music.unpause()
           if(score<=10 or score>=20):
               if(competition):
                gameExit = True
                pygame.mixer.music.pause()
                boing.play()
                pygame.mixer.music.unpause()
           if (y>=580 or y<=0):
               gameExit = True
               pygame.mixer.music.pause()
               boing.play()
               pygame.mixer.music.unpause()
           if(y2>=580 or y2<=0):
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
           if button(770,0,30,33,"||",white,775,2):
               paused()
           person = pygame.Rect(x, y, 20, 20)
           pygame.draw.rect(gameDisplay, color , person)
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
            playAgain()
            pygame.display.update()
def mainMenu():
    pygame.draw.rect(gameDisplay, (255,255,255),[0,0,800,600])
    messageOnScreen("Welcome to Dodge N Eat",190,100,(255,0,255),5)
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
               if event.key == pygame.K_s:
                   settings()
        if button(200,250,400,80,"Play (Y)",(0,255,0),350,270) and bob>10:
            gameStart=True
        if button(200,350,400,80,"Settings (S)",(0,0,255),350,370) and bob>100:
            settings()
        if button(200,450,400,80,"Quit (Q)",(255,0,0),350,470) and bob>10:
            quit()
            pygame.quit()
        pygame.display.update()
    dodgeNEat()
def messageOnScreen(msg,x,y,color,size):
    font =  pygame.font.SysFont(None,(int)(size*10))
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
    gameLoop = False
    global win
    global hacked
    global score
    global highScore
    messageOnScreen("Would You Like To Play Again?",300,370,(0,0,255),2.5)
    pygame.display.update()
    while gameLoop == False:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_y:
                   dodgeNEat()
               if event.key == pygame.K_n:
                   mainMenu()
        if button(300,400,200,40,"Yes (Y)",(0,255,0),345,405):
            dodgeNEat()
        if button(300,450,200,40,"No (N)",(255,0,0),355,455):
            mainMenu()
        pygame.display.update()
def fight():
    global pl
    ef= random.randrange(0,300)
    if ef == 1:
        if pl==1:
            pl = 2
        else:
            pl = 1
def settings():
    global image
    global v1
    global multiPlayer
    global competition
    global sM
    global dM
    global mC
    global mP
    global tP
    global tC
    bobIsBoss=True
    qwe=0
    while bobIsBoss:
        gameDisplay.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if multiPlayer:
                        multiPlayer=False
                    else:
                        multiPlayer=True
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
                if event.key == pygame.K_d:
                    if dM:
                        dM=False
                    else:
                        dM=True
                        v1=False
                if event.key == pygame.K_s:
                    if sM:
                        sM=False
                    else:
                        sM=True
                        v1=False
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
        qwe+=1
        if multiPlayer:
            if button(10,10,250,40,"Multiplayer (M)",(0,255,0),30,20) and qwe>30:
                multiPlayer=False
                qwe=0
        else:
            if button(10,10,250,40,"Multiplayer (M)",(255,0,0),30,20)and qwe>30:
                multiPlayer=True
                qwe=0
        if multiPlayer:
            if v1:
                if button(270,10,250,40,"Fight (F)",(0,255,0),290,20) and qwe>30:
                    v1=False
                    qwe=0
            else:
                if button(270,10,250,40,"Fight (F)",(255,0,0),290,20) and qwe>30:
                    v1=True
                    sM=False
                    dM=False
                    competition=False
                    qwe=0
            if mC and mP==2:
                if button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(0,255,0),20,170) and qwe>30:
                    mC=False
                    qwe=0
            else:
                if button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(255,0,0),20,170) and qwe>30:
                    mC=True
                    mP=2
                    tC=False
                    qwe=0
            if tC and tP==2:
                if button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(0,255,0),20,270) and qwe>30:
                    tC=False
                    qwe=0
            else:
                if button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(255,0,0),20,270) and qwe>30:
                    tC=True
                    mC=False
                    tP=2
                    qwe=0
            if competition:
                if button(530,10,250,40,"Score Compete(C)",(0,255,0),540,20) and qwe>30:
                    competition=False
                    qwe=0
            else:
                if button(530,10,250,40,"Score Compete(C)",(255,0,0),540,20) and qwe>30:
                    competition=True
                    v1=False
                    qwe=0
            if not competition and not v1:
                if button(10,60,250,40,"Work Together(W)",(0,255,0),20,70) and qwe>30:
                    competition=True
                    qwe=0
            else:
                if button(10,60,250,40,"Work Together(W)",(255,0,0),20,70) and qwe>30:
                    competition=False
                    v1=False
                    qwe=0
        else:
            v1=False
            competition=False
            if mP==2:
                mC=False
            if tP==2:
                tC=False
            button(270,10,250,40,"Fight (F)",(100,100,100),290,20)
            button(530,10,250,40,"Score Compete(C)",(100,100,100),540,20)
            button(10,60,250,40,"Work Together(W)",(100,100,100),20,70)
            button(10,160,780,40,"Mouse Control(player 2)(in line)(O)",(100,100,100),20,170)
            button(10,260,780,40,"Mouse Control(player 2)(anywhere)(R)",(100,100,100),20,270)
        if dM:
            if button(270,60,250,40,"Duplicate Mode(D)",(0,255,0),272,70) and qwe>30:
                dM=False
                qwe=0
        else:
            if button(270,60,250,40,"Duplicate Mode(D)",(255,0,0),272,70) and qwe>30:
                dM=True
                v1=False
                qwe=0
        if sM:
            if button(530,60,250,40,"Shooting Mode(S)",(0,255,0),532,70) and qwe>30:
                sM=False
                qwe=0
        else:
            if button(530,60,250,40,"Shooting Mode(S)",(255,0,0),532,70) and qwe>30:
                sM=True
                v1=False
                qwe=0
        if mC and mP==1:
            if button(10,110,780,40,"Mouse Control(player 1)(in line)(L)",(0,255,0),20,120) and qwe>30:
                mC=False
                qwe=0
        else:
            if button(10,110,780,40,"Mouse Control(player 1)(in line)(L)",(255,0,0),20,120) and qwe>30:
                mC=True
                mP=1
                tC=False
                qwe=0
        if tC and tP==1:
            if button(10,210,780,40,"Mouse Control(player 1)(anywhere)(A)",(0,255,0),20,220) and qwe>30:
                tC=False
                qwe=0
        else:
            if button(10,210,780,40,"Mouse Control(player 1)(anywhere)(A)",(255,0,0),20,220) and qwe>30:
                tC=True
                mC=False
                tP=1
                qwe=0
        if button(10,550,200,40,"Exit (X)",(255,random.randrange(0,150),random.randrange(0,150)),15,560):
            bobIsBoss=False
            mainMenu()
        pygame.display.update()
def paused():
    pause=True
    pygame.mixer.music.pause()
    pygame.draw.rect(gameDisplay,(255,255,255) , [50,240,730,140])
    messageOnScreen("Paused",350,250,black,2.5)
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
                    dodgeNEat()
        clock.tick(5)
        if button(480,320,210,50,"Main Menu (M)",(255,0,0),481,330):
            pause=False
            pygame.mixer.music.unpause()
            mainMenu()
        if button(270,320,200,50,"Start Over (S)",(0,0,255),280,330):
            pause=False
            pygame.mixer.music.unpause()
            dodgeNEat()
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