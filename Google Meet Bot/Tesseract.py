import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab

def imToString():
    pytesseract.pytesseract.tesseract_cmd ='Tesseract/tesseract.exe'
    cap = ImageGrab.grab(bbox =(396, 240, 396+417, 240+42))
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY),
            lang ='eng')
    return tesstr
