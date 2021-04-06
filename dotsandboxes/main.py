import numpy as np
import pygame as pg

class Player:
    def __init__(self, color):
        self.color = color
        self.count = 0

def click(*coords):
    global currentPlayer
    board[coords] = currentPlayer
    currentPlayer += 1
    if currentPlayer == len(players):
        currentPlayer = 0

def resize():
    global winSize, scale, pad

    winSize = win.get_size()
    scale = ((s*3)//(WIDTH*4) if (s := min(winSize)) == winSize[0] else (s*3)//(HEIGHT*4))
    pad = scale//10

players = [Player((255,0,0)), Player((0,255,0)), Player((0,0,255))]
currentPlayer = 0

WIDTH = 3
HEIGHT = 3

board = np.zeros((HEIGHT+1,WIDTH+1,2))-1
closed = np.ones((HEIGHT, WIDTH, 3))*255
pg.init()

win = pg.display.set_mode(size=(720,720), flags=pg.RESIZABLE)

resize()

start = 0,0
run = True
while run:
    # Reset per-loop variables
    leftClick = False
    madeBox = False

    # Get events
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.VIDEORESIZE:
            resize()
        if event.type == pg.MOUSEBUTTONDOWN:
            start = mousePos
        if event.type == pg.MOUSEBUTTONUP and mousePos == start:
            leftClick = True

    win.fill((30,30,30))

    # grab key and mouse presses
    keys = pg.key.get_pressed()
    mouseButtons = pg.mouse.get_pressed()
    mousePos = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]

    for x in range(WIDTH+1):
        for y in range(HEIGHT+1):
            if y < HEIGHT and x < WIDTH:
                color = closed[y,x]//2 if not np.all(closed[y,x] == 255) else closed[y,x]
                pg.draw.rect(win, color, (winSize[0]//2-scale*WIDTH//2+scale*x, winSize[1]//2-scale*HEIGHT//2+scale*y, scale, scale))
                if np.all(closed[y,x] == 255) and board[y,x,0] != -1 and board[y,x,1] != -1 and board[y+1,x,1] != -1 and board[y,x+1,0] != -1:
                    madeBox = True
                    closed[y,x] = players[currentPlayer-1].color
                    players[currentPlayer-1].count += 1

            if y < HEIGHT:
                color = players[int(board[y,x,0])].color if board[y,x,0] != -1 else (255,255,255)
                vert = pg.Rect(winSize[0]//2-scale*WIDTH//2+scale*x-pad//2, winSize[1]//2-scale*HEIGHT//2+scale*y+pad//2, pad, scale-pad)
                if vert.collidepoint(mousePos) and board[y,x,0] == -1:
                    if color == (255,255,255):
                        color = [150]*3
                    if leftClick:
                        click(y,x,0)

                pg.draw.rect(win, color, vert)

            if x < WIDTH:
                color = players[int(board[y,x,1])].color if board[y,x,1] != -1 else (255,255,255)
                horz = pg.Rect(winSize[0]//2-scale*WIDTH//2+scale*x+pad//2, winSize[1]//2-scale*HEIGHT//2+scale*y-pad//2, scale-pad, pad)
                if horz.collidepoint(mousePos) and board[y,x,1] == -1:
                    if color == (255,255,255):
                        color = [150]*3
                    if leftClick:
                        click(y,x,1)

                pg.draw.rect(win, color, horz)

            pg.draw.rect(win, (0,0,0), (winSize[0]//2-scale*WIDTH//2+scale*x-pad//2, winSize[1]//2-scale*HEIGHT//2+scale*y-pad//2, pad, pad))

    if madeBox:
        # Player got a box
        if currentPlayer != 0:
            currentPlayer -= 1
        else:
            currentPlayer = len(players)-1

    if sum([player.count for player in players]) == WIDTH*HEIGHT:
        print(f"Player {sorted(range(len(players)), key=lambda i: players[i].count)[0]} wins!")
        run = False

    pg.display.update()

pg.quit()
exit()
