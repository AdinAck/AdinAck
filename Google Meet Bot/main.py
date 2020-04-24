import cleverbot as c
import Tesseract as t
c.open()
string = t.imToString(396, 240, 396+417, 240+42)
print("Sending",string)
print("Received",c.chat(string))
c.close()
