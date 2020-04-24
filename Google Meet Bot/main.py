import pyautogui
# import cleverbot as c
import Tesseract as t
# c.open()
while True:
    string = t.imToString(428, 754, 428+1090, 754+292)
    print("Sending",string.split(". ")[-1])
    # print("Received",c.chat(string))
# c.close()
