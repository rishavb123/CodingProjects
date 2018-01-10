import pygame
import time
pygame.init()
gameDisplay=0
def initialize_window():
    global gameDisplay
    gameDisplay = pygame.display.set_mode((1000,800)) # creates a display and returns a surface object
    gameDisplay.fill((255,255,255))
def displayer(name):
    image = pygame.image.load(name)
    image = pygame.transform.scale(image,(1000,800))
    gameDisplay.blit(image,(0,0))
    pygame.display.update()
    time.sleep(10)
    quit()
    pygame.quit()
