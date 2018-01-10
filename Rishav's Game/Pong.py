
import pygame  # pygame is a gaming module with things built in to make game coding easier
import time
import random
pygame.init()  # init is short for initialize... it initializes the game and all the modules available for you to use

gameDisplay = pygame.display.set_mode((800,600)) # creates a display and returns a surface object
gameDisplay.fill((255,255,255))
height = 600
players=4
clock=pygame.time.Clock()
icon = pygame.image.load("RishavIcon.jpg")
pygame.display.set_caption("Pong")
pygame.display.set_icon(icon)
width = 800
gameExit = False
y1=y2=by=270
changeBY=changeBX=.1
x3=x4=bx=360
change1=change2=change3=change4=0
while gameExit == False:
    gameDisplay.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit= True
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            change1=-1
        elif key[pygame.K_s]:
            change1=1
        else:
            change1=0
        if key[pygame.K_UP]:
            change2=-1
        elif key[pygame.K_DOWN]:
            change2=1
        else:
            change2=0
        if players>2:
            if key[pygame.K_COMMA]:
                change3=-1.5
            elif key[pygame.K_PERIOD]:
                change3=1.5
            else:
                change3=0
        if players>3:
            if key[pygame.K_g]:
                change4=-1.5
            elif key[pygame.K_h]:
                change4=1.5
            else:
                change4=0
    ball = pygame.draw.circle(gameDisplay, (0,0,0), (int(bx),int(by)),10)
    bx+=changeBX
    by+=changeBY
    if bx+10>=x4 and bx<=x4+80 and by>=570:
        changeBY*=-1
    if bx<=30 and by+10>=y1 and by<=y1+80:
        changeBX*=-1
    if bx>=770 and by+10>=y2 and by<=y2+80:
        changeBX*=-1
    if bx+10>=x3 and bx<=x3+80 and by<=30:
        changeBY*=-1
    if y1<0:
        y1=0
    if y1>540:
        y1=540
    if y2<0:
        y2=0
    if y2>540:
        y2=540
    if x3<0:
        x3=0
    if x3>720:
        x3=720
    if x4<0:
        x4=0
    if x4>720:
        x4=720
    y1+=change1
    y2+=change2
    x3+=change3
    x4+=change4
    pygame.draw.rect(gameDisplay,(0,0,0),[0,y1,20,60])
    pygame.draw.rect(gameDisplay,(0,0,0),[780,y2,20,60])
    if players>2:
        pygame.draw.rect(gameDisplay,(0,0,0),[x3,0,80,20])
    if players>3:
        pygame.draw.rect(gameDisplay,(0,0,0),[x4,580,80,20])
    pygame.display.update()
pygame.quit()  # de-initializes the pygame module
quit()  # quits the window
