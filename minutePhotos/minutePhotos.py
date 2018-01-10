import cv2
import os
import time

cam = cv2.VideoCapture(0)

def getPhoto():
    tf, frame = cam.read()
    if not tf:
        return tf
    return frame

def gitPush(message):
    os.system('git add -A')
    os.system('git commit -m "'+message+'"')
    os.system('git push')

def save(img):
    cv2.imwrite('minutePhotos/contents/image.jpg',img)

while True:
    save(getPhoto())
    gitPush('minuteImage Push')