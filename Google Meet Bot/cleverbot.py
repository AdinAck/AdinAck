import cleverbotfree.cbfree
import sys
cb = cleverbotfree.cbfree.Cleverbot()

def open():
    try:
        cb.browser.get(cb.url)
    except:
        cb.browser.close()
        sys.exit()

def chat(userInput):
    try:
        cb.get_form()
    except:
        sys.exit()
    cb.send_input(userInput)
    bot = cb.get_response()
    a = []
    p = 0
    for i in range(len(bot)):
        if " " in bot[i]:
            a.append(bot[p:i+1])
            p = i+1
    a.append(bot[p:])
    for i in range(len(a)):
        if "cleverbot" in a[i].lower():
            a[i] = "Artin"

    return "".join(a)

def close():
    cb.browser.close()
