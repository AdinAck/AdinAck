import numpy as np
import pygame

pygame.init()

win = pygame.display.set_mode(size=(500,500))

size = 50,50
pos = np.array(pygame.display.get_surface().get_size())//2 - np.array(size)//2
rect = np.concatenate((pos,size))

posChange = np.array([0,0])

run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pos[1] < pygame.display.get_surface().get_size()[1]-size[1]:
        posChange[1] += 1
    else:
        pos[1] = pygame.display.get_surface().get_size()[1]-size[1]
        posChange[1] = 0

    pos += posChange
    rect = np.concatenate((pos,size))
    pygame.draw.rect(win,(255,255,255),rect)

    pygame.display.update()
    pygame.time.delay(int(1000*(1/60)))

pygame.quit()
