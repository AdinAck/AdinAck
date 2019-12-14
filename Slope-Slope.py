from fractions import Fraction; a = [0,0]; b = [0,0]
a[0] = input("Slope of line of reflection: "); a[1] = input("Slope of line being reflected: ")
for j in range(2):
    if "/" in a[j]:
        for i in range(len(a[j])):
            if "/" in a[j][i]: x = a[j][:i]; y = a[j][i+1:]
        b[j] = float(x)/float(y)
    else: b[j] = float(a[j])
print("m3: "+str(Fraction(((2*b[0])/((1/b[0])+b[0])-(b[1]/((1/b[0])+b[1])))/(2/((1/b[0])+b[0])-(1/((1/b[0])+b[1])))).limit_denominator()))
