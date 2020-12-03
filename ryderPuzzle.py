import os
import pyautogui
import random
import numpy as np

def printMaze(maze, seen, ypos, xpos):
    os.system('cls')
    for i in range(np.size(maze, 0)):
        for j in range(np.size(maze, 1)):
            if (np.size(maze, 0)-i,j) == (ypos,xpos):
                print("O ", end='')
            elif (np.size(maze, 0)-i,j) in seen:
                print("# ", end='')
            else:
                print("  ",end='')
        print()

# Puzzle
def puzzle(code):

    maze = np.array([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                     [1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1],
                     [1,0,1,1,1,0,1,0,0,0,2,0,0,0,0,0,0,0,0,1],
                     [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
                     [1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,2,1,1,1],
                     [1,0,0,0,0,0,0,2,1,2,1,0,0,0,0,1,0,0,3,1],
                     [1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,2,2,1],
                     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

    while True:
        r1, r2 = random.randint(0,np.size(maze, 0)-1), random.randint(0,np.size(maze, 1)-1)
        if maze[r1,r2] == 0:
            xpos = r2
            ypos = r1
            break

    seen = [(ypos, xpos)]
    printMaze(maze, seen, ypos, xpos)

    while True:
        move = pyautogui.confirm(text='Choose direction', title='', buttons=['Up', 'Down', 'Left', 'Right'])
        if move == "Up":
            i = 1
            j = 0
        elif move == "Down":
            i = -1
            j = 0
        elif move == "Left":
            i = 0
            j = -1
        elif move == "Right":
            i = 0
            j = 1

        if maze[ypos+i,xpos+j] == 0:
            xpos += j
            ypos += i
            seen.append((ypos,xpos))
            printMaze(maze, seen, ypos, xpos)
            continue
        elif maze[ypos+i,xpos+j] == 2:
            os.system('cls')
            pyautogui.alert(text='You hit a spike! Now you don\'t remember anything!', title='Error')
            xpos = 1
            ypos = 1
            seen = [(ypos, xpos)]
            printMaze(maze, seen, ypos, xpos)
            continue
        elif maze[ypos+i,xpos+j] == 3:
            pyautogui.alert(text='You have successfully completed the maze!\nThe 4 digit code is {}'.format(code), title='Success')
            break



# Login
code = random.randint(1000,9999)
msg = "Please enter password:"
i = 0
while True:
    login = pyautogui.password(text=msg, title="Login")

    if i == 2:
        pyautogui.alert(text='You have run out of attempts, resetting.', title='Login')
        break
    if login == str(code):
        pyautogui.alert(text='Code accepted, you did it.\nBe proud of yourself.', title='Login')
        break
    else:
        i += 1
        msg = "{} attempts remain.\nPlease enter password:".format(3-i)
        if pyautogui.confirm(text='The password was incorrect, would you like to solve the security challenge to retreive the password?', title='Incorrect Login', buttons=['Yes', 'No']) == "Yes":
            pyautogui.alert(text='You are about to be put in a maze.\nGrab a piece of paper to write things down.\nI\'m gonna be honest, this won\'t be easy.', title='Info')
            puzzle(code)
