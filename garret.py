import numpy as np
import pygame
import math

# Variables
g = 1
friction = 0.75

def getCorners():
    return np.array()

def winSize():
    return np.array(pygame.display.get_surface().get_size())

def getGravity():
    return (winSize()//displaySize)[1]*g

pygame.init()

displaySize = np.array([500,500])
win = pygame.display.set_mode(size=displaySize,flags=pygame.RESIZABLE)

size = np.array([50,50])
pos = np.array(pygame.display.get_surface().get_size())//2 - np.array(size)//2
screen = np.array(pygame.display.get_surface().get_size())
rect = np.concatenate((pos,size))
posChange = np.array([0,0])
r = 0
temp = True
center = pos+size//2
run = True
dist = []
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(size=(event.w,event.h),flags=pygame.RESIZABLE)
            scaleRatio = ((winSize()[0]**2+winSize()[1]**2)**(1/2))/((displaySize[0]**2+displaySize[1]**2)**(1/2))
            posRatio = winSize()/displaySize
            pos = pos*posRatio
            size = size*scaleRatio
            displaySize = winSize()
            ratioApplied = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(event)
            temp = True

    if pos[1] < pygame.display.get_surface().get_size()[1]-size[1]:
        posChange[1] += getGravity()
    else:
        pos[1] = pygame.display.get_surface().get_size()[1]-size[1]
        posChange[1] = posChange[1]*(-friction)

    rect = np.array([pos,[pos[0]+size[0],pos[1]],[pos[0]+size[1],pos[1]+size[1]],[pos[0],pos[1]+size[1]]])
    rect.shape = np.size(rect)//2,2
    print(np.max(rect[:,1]))
    pos += posChange
    center = pos+size//2
    if pygame.mouse.get_pressed()[0]:

            # r += .1
            posChange[1] = 0
            if temp:
                temp = False
                print("hi")
                start = np.array(pygame.mouse.get_pos())-center
            center = np.array(pygame.mouse.get_pos())-start
            pos = center-size//2



    for i in range(np.size(rect,0)):
        rect[i] -= center
        rect[i] = rect[i].dot(np.array([[math.cos(r),-math.sin(r)],[math.sin(r),math.cos(r)]]))
        rect[i] += center
    pygame.draw.polygon(win,(255,255,255),rect)

    pygame.display.update()
    pygame.time.delay(int(1000*(1/60)))

pygame.quit()
