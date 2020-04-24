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

lastSentence = ""
triggers = ["adin","aiden","hayden","ayden","aden","aidan","eden", "aid in"]
def sendReceive(send):
    print("Sending:",send)
    thing = c.chat(send)
    print("Received:", thing)
    pyautogui.write(thing)
    # pyautogui.press('enter')
def read():
    string = t.imToString(68, 997, 68+1090, 997+32)
    string = list(string)
    for i in range(len(string)):
        if "?" in string[i] or "!" in string[i]:
            string[i] = "."
        elif string[i] == "|":
            string[i] = "I"
    string = "".join(string)
    for i in range(len(triggers)):
        string = string.lower().replace(triggers[i],"cleverbot")
    return string.split(". ")[-1]

while True:
    send = read()
    if lastSentence != send:
        if "cleverbot" in send.lower() and "." in send.lower():
            if send == "cleverbot.":
                time.sleep(4)
                send = read()
            sendReceive(send)
    lastSentence = send
c.close()
