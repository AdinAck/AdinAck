import numpy as np
import pygame
import math

# Variables
g = 1
friction = 0.75

def winSize():
    return np.array(pygame.display.get_surface().get_size())

def getGravity():
    return (winSize()//displaySize)[1]*g

def cart(point, r, theta):
    return np.array([point[0]+r*math.cos(theta), point[1]+r*math.sin(theta)])

pygame.init()

displaySize = np.array([500,500])
win = pygame.display.set_mode(size=displaySize,flags=pygame.RESIZABLE)
framerate = 60
clock = pygame.time.Clock()
pos = np.array([200,200])
size = np.array([50,50])
screen = np.array(pygame.display.get_surface().get_size())

posChange = np.array([0,0])
r = 0
temp = True
run = True
angle = 0
center = displaySize//2
rect = np.array([cart(center,size[0]//2,angle),cart(center,size[0]//2,angle+90),cart(center,size[0]//2,angle+180),cart(center,size[0]//2,angle+270)])
pinnedPoint = center
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(size=(event.w,event.h),flags=pygame.RESIZABLE)
            scaleRatio = ((winSize()[0]**2+winSize()[1]**2)**(1/2))/((displaySize[0]**2+displaySize[1]**2)**(1/2))
            posRatio = winSize()/displaySize
            center = center*posRatio
            size = size*scaleRatio
            g *= scaleRatio
            displaySize = winSize()
            ratioApplied = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(event)
            temp = True

    if center[1] < pygame.display.get_surface().get_size()[1]-size[1]:
        posChange[1] += getGravity()
    else:
        center[1] = pygame.display.get_surface().get_size()[1]-size[1]
        posChange[1] = round(posChange[1]*-friction,3)
        posChange[0] = round(posChange[0]*friction,3)

    def f(x,y,pos1,pos2):
        slope = (pos2[1]-pos1[1])/(pos2[0]-pos1[0])
        return slope*(x-pos1[0])+pos1[1],slope*(y-pos1[1])+pos1[0]

    center +=posChange
    if pygame.mouse.get_pressed()[0]:
        angle = .1
        posChange = np.array(pygame.mouse.get_rel())
        if temp:
            temp = False
            diff = np.array(pygame.mouse.get_pos())-center

        center = pygame.mouse.get_pos()+diff
        for i in range(np.size(rect,0)):
            rect[i] -= np.array(pygame.mouse.get_pos())
            rect[i] = rect[i].dot(np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]]))
            rect[i] += np.array(pygame.mouse.get_pos())
    else:
        rect = np.array([cart(center,size[0]//2,angle),cart(center,size[0]//2,angle+math.pi/2),cart(center,size[0]//2,angle+math.pi),cart(center,size[0]//2,angle+(math.pi*3)/2)])
    rect.shape = np.size(rect)//2,2
    print(rect)
    print(center)
    pygame.draw.polygon(win,(255,255,255),rect)
    pygame.draw.circle(win,(255,255,0),(int(center[0]),int(center[1])),3)
    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
