def ten2twelve(a, base):
    b = int(a)//base; c = (int(a)-b*base)
    if b > base-1: b = ten2twelve(b, base)
    if b == 0: b = ""
    if c > 9:
        return str(b)+chr(87+c).upper()
    return str(b)+str(c)

while True:
    prebase = int(input("from base: "))
    postbase = int(input("to base: "))
    a = input(f"base {prebase}: ")
    print(f"base {postbase}:",ten2twelve(int(a, prebase), postbase))