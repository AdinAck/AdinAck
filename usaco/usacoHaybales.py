f = open("haybales.in", "r")
n,q = f.readline().split(" ")
h = sorted([int(i) for i in f.readline()[:-1].split(" ")])
print(h)
b = [i.split(" ") for i in f.read().split("\n")]
o = open("haybales.out", "w")
for i in range(len(b)-1):
    x,y = int(b[i][0]),int(b[i][1])
    blip = -1
    bloop = -2
    for j in range(len(h)):
        if h[j] == x:
            blip = j
            break
        if h[j] > x:
            blip = j
            break
    for j in range(len(h)):
        if h[j] == y:
            bloop = j
            break
        if h[j] > y:
            bloop = j-1
            break
    print(blip,bloop+1)
    o.write(str(bloop+1-blip)+"\n")
o.close()
