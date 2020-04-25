import time
import pyautogui
import cleverbot as c
import Tesseract as t

c.open()

input()

pyautogui.moveTo(1627, 992)
time.sleep(.5)
pyautogui.click()
time.sleep(.5)
pyautogui.moveTo(1800, 124)
pyautogui.click()
pyautogui.moveTo(1630, 1010)
time.sleep(.5)
pyautogui.click()

lastCaption = ""
triggers = ["adin","aiden","hayden","ayden","aden","aidan","eden", "aid in"]
def sendReceive(send):
    print("Sending:",send)
    thing = c.chat(send)
    print("Received:", thing)
    pyautogui.write(thing)
    pyautogui.press('enter')
def read(x1,y1,x2,y2):
    thing = t.imToString(x1,y1,x2,y2)
    thing = list(thing.split("\n"))
    a = []
    for string in thing:
        for i in range(len(string)):
            if "?" in string[i] or "!" in string[i]:
                string[i] = "."
            elif string[i] == "|":
                string[i] = "I"
        string = "".join(string)
        for i in range(len(triggers)):
            string = string.lower().replace(triggers[i],"cleverbot")
        a.extend(string.split(". "))
    return a

while True:
    # Read live captions
    thing = read(68, 997, 68+1090, 997+32)
    for caption in thing:
        if lastCaption != caption:
            if "cleverbot" in send.lower() and "." in send.lower():
                if caption == "cleverbot.":
                    time.sleep(4)
                    caption = read(68, 997, 68+1090, 997+32)
                sendReceive(caption)
        lastCaption = caption

    # Read chat
    thing2 = read(1613, 160, 1902, 1000)
    for chat in thing2:
        if lastChat != chat:
            if "cleverbot" in send.lower() and "." in send.lower():
                if chat == "cleverbot.":
                    time.sleep(4)
                    chat = read(1613, 160, 1902, 1000)
                sendReceive(chat)
        lastChat = chat
c.close()
