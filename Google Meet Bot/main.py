import cleverbot as c
import Tesseract as t
c.open()
string = t.imToString()
print("Sending",string)
print("Received",c.chat(string))
c.close()
