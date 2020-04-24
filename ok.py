import numpy as np
import pygame
import math

# Initialization
    # Physics Constants
g = -100
friction = 100

    # Environment Properties
# pygame.display.get_surface().get_size() # Tuple of width and height of window
# pygame.mouse.get_rel() # Tuple of relative change since last call
# pygame.mouse.get_pos() # Tuple of position of mouse cursor
# pygame.mouse.get_pressed() # Array of booleans: [left click, middle, right]
# In event loop:
# if event.type == pygame.MOUSEBUTTONUP:
#   print("Mouse button released!")

    # Functions
pygame.init()
win = pygame.display.set_mode(size=(500,500))

def gravity(): #finalizations
    global touching
    global pos
    global g
    if touching == 0: # finalized
        # pos[0][1][1] -= g
        pass
    elif touching == 1: # finalized
        pos[1][1][2] -= g*math.cos(pos[1][1][0])/pos[1][0]
    elif touching == 2:
        pass
    elif touching == 3: # finalized
        pass

def isTouching():
    global pinned
    touching = 0
    if pinned:
        touching += 1
    if groundTouch():
        touching += 2

    return touching

def groundTouch():
    return False

def propD(arr):
    for i in range(1, np.size(arr)):
        arr[i-1] += arr[i]
        # arr[i-1] = round(arr[i-1],3)

def cart(point, r, theta):
    return np.array([point[0]+r*math.cos(theta), point[1]+r*math.sin(theta)])

def inRect(mpos):
    pts = corners()
    x = np.array([[9223372036854775807, -1], [-9223372036854775808, -1]],np.float64)
    y = np.array([[-1, 9223372036854775807], [-1, -9223372036854775808]],np.float64)
    for i in range(4):
        if x[0][0] > pts[i][0]:
            x[0] = pts[i]
        if x[1][0] < pts[i][0]:
            x[1] = pts[i]
        if y[0][1] > pts[i][1]:
            y[0] = pts[i]
        if y[1][1] < pts[i][1]:
            y[1] = pts[i]

    for i in range(pygame.display.get_surface().get_width()):
        try:
            pygame.draw.rect(win,(255,0,0),(i,(x[0][1]+(y[0][1]-x[0][1])/(y[0][0]-x[0][0])*(i-x[0][0]))*100,1,1))
            pygame.draw.rect(win,(255,0,0),(i,(y[0][1]+(x[1][1]-y[0][1])/(x[1][0]-y[0][0])*(i-y[0][0]))*100,1,1))
            pygame.draw.rect(win,(255,0,0),(i,(x[0][1]+(y[1][1]-x[0][1])/(y[1][0]-x[0][0])*(i-x[0][0]))*100,1,1))
            pygame.draw.rect(win,(255,0,0),(i,(y[1][1]+(x[1][1]-y[1][1])/(x[1][0]-y[1][0])*(i-y[1][0]))*100,1,1))
        except Exception as e:
            print(e)

    return [(mpos[0] >= x[0][0] and mpos[0] <= x[1][0] and mpos[1] >= y[0][1] and mpos[1] <= y[1][1])
    and (mpos[0] < y[0][0] and mpos[1] > x[0][1]+(y[0][1]-x[0][1])/(y[0][0]-x[0][0])*(mpos[0]-x[0][0])
    or mpos[0] > y[0][0] and mpos[1] > y[0][1]+(x[1][1]-y[0][1])/(x[1][0]-y[0][0])*(mpos[0]-y[0][0]))
    and (mpos[0] < y[1][0] and mpos[1] < x[0][1]+(y[1][1]-x[0][1])/(y[1][0]-x[0][0])*(mpos[0]-x[0][0])
    or mpos[0] > y[1][0] and mpos[1] < y[1][1]+(x[1][1]-y[1][1])/(x[1][0]-y[1][0])*(mpos[0]-y[1][0]))][0]

def corners():
    global pos
    global rot
    global size
    ret = np.array([],int)
    for i in range(4):
        ret = np.append(ret, cart(pos[0][0], size[0]/(2**(1/2)), rot+i*math.pi/2))
    ret.shape = np.size(ret)//2,2
    return ret

def pol(n):
    if n == 0: return 0
    else: return n/abs(n)

    # Object Properties
size = np.array([.5, .5])
pos = np.array([[np.array(pygame.display.get_surface().get_size())/200-size/2,[0,0]],[0,[0,0,0]]])
rot = 0
touching = 0
pinned = False

framerate = 60
clock = pygame.time.Clock()
run = True
while run:
    try:
        friction = 100/((1/1000)*abs(pos[1][1][2]*1000)+1)**7
    except:
        pass
    print(abs(pos[1][1][2]*1000))
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(size=(event.w,event.h),flags=pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    pos[1][1][2] = 0
    touching = isTouching()
    gravity()
    mpos = np.array(pygame.mouse.get_pos())/100
    if pygame.mouse.get_pressed()[0] and not pinned and inRect(mpos):
        pinned = True
        pos[1][0] = ((mpos[0]-pos[0][0][0])**2+(mpos[1]-pos[0][0][1])**2)**(1/2)
        pos[1][1][0] = math.pi-math.atan((mpos[1]-pos[0][0][1])/(mpos[0]-pos[0][0][0]))*pol(pos[0][0][0]-mpos[0])
        pos[1][1][1] -= pos[0][1][0]*math.sin(pos[1][1][0])/pos[1][0]
        pos[1][1][1] -= pos[0][1][1]*math.cos(pos[1][1][0])/pos[1][0]
        rot += pos[1][1][1]
        pos[1][1][2] -= pol(pos[1][1][1])*friction
        pos[1][1][2] /= 10000
        propD(pos[1][1])
        pos[0][0] = cart(mpos, pos[1][0], pos[1][1][0])
    elif pinned:
        mrel = np.array(pygame.mouse.get_rel())*10
        pos[1][1][2] += mrel[0]*math.sin(pos[1][1][0])
        pos[1][1][2] -= mrel[1]*math.cos(pos[1][1][0])
        rot += pos[1][1][1]
        pos[1][1][2] -= pol(pos[1][1][1])*friction
        pos[1][1][2] /= 10000
        propD(pos[1][1])
        pos[0][0] = cart(mpos, pos[1][0], pos[1][1][0])

    pygame.draw.polygon(win,(255,255,255),corners()*100)

    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
