import urllib
import Image_Displayer
import pygame
import requests


def download_web_image(url,name):
    full_name = str(name)+'.'+url[len(url)-3]+url[len(url)-2]+url[len(url)-1]
    urllib.urlretrieve(url, full_name)
    Image_Displayer.initialize_window()
    Image_Displayer.displayer(full_name)

def type():
    enter = False
    s=""
    while enter == False:
        Image_Displayer.gameDisplay.fill((255,255,255))
        pygame.draw.line(Image_Displayer.gameDisplay,(0,0,0), (350,125),(730,125),1)
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

def messageOnScreen(msg,x,y,color,size):
    font =  pygame.font.SysFont(None,int(size*10))
    text =  font.render(msg,True,color)
    Image_Displayer.gameDisplay.blit(text,[x,y])
url = str(raw_input("Url: "))
Image_Displayer.initialize_window()
download_web_image(url,type())
