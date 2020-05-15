def convert():
    try:
        f = open("equations.txt","r")
    except:
        f = open("equations.txt","w")
    lines = f.read().splitlines()
    print(lines)
    equationPermutations = []#[None]len(lines)2
    for line in lines:
        line = line+" "
        #line = "k = 1/2mv " #make sure space is at end of equations
        lastSpace = -1
        equalIndex = line.find("=")
        for c in range(len(line)):
            if line[c] == " ":
                lastSpace = c
            if line[c].isalpha():
                coef1 = line[lastSpace+1:c]
                nextSpace = c
                print(line[nextSpace],line[nextSpace] != " ","wwww")
                while line[nextSpace] != " ":
                    nextSpace+=1
                print(line[nextSpace],line[nextSpace] != " ","wwww222")
                print(line[nextSpace],"dasdsa")
                coef2 = line[c+1:nextSpace]
                reciprical = ""
                print(coef1,coef2,"32323232")
                if len(coef1) != 0 or len(coef2) != 0:
                    if len(coef1) == 0:
                        coef1 = ""
                    if len(coef2) == 0:
                        coef2 = ""
                    reciprical = "(1/("+coef1+coef2+"))*"
                left = ""
                right = ""
                print(coef1,coef2,line[c])
                if c < equalIndex:
                    if lastSpace >1:
                        left = "-("+line[0:lastSpace+1]+")"
                    if nextSpace - equalIndex >1:
                        right = "-("+line[nextSpace:equalIndex-1]+")"
                    equationPermutations.append([str(line[c]),reciprical+"("+line[equalIndex+2:-1]+left+right+")"])
                else:
                    if equalIndex-lastSpace >1:
                        left = "-("+line[equalIndex+1:lastSpace+1]+")"
                    if len(line)-nextSpace >2:
                        print(len(line),nextSpace,"adadada")
                        right = "-("+line[nextSpace+1:-1]+")"
                    equationPermutations.append([str(line[c]),reciprical+"("+line[0:equalIndex-1]+left+right+")"])
    print(equationPermutations)
    return equationPermutations
