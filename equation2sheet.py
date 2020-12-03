import numpy as np

def equation(x):
    return 1/x

domain = 0,10
increment = .001

f = open("output.txt", "w")

for x in np.arange(domain[0],domain[1],increment):
    f.write(str(x)+"\t"+str(equation(x))+"\n")
