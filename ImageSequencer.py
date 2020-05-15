import time
import pyautogui

def run():
	n = int(input("Number of files? "))
	p = input("Prefix? ")
	time.sleep(3)
	for i in range(n):
		pyautogui.press("f2")
		pyautogui.write(p+str(i))
		pyautogui.press("enter")
		pyautogui.press("down")
run()
 
