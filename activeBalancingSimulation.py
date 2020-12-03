import math

class Cell:
    def __init__(self, charged, capacity):
        self.charged = charged
        self.capacity = capacity

    @property
    def voltage(self):
        return ((4.2-3.4)/self.capacity)*self.charged+3.4

    def charge(self, amount):
        self.charged += amount

class Cap:
    def __init__(self, capacitance, ESR):
        self.c = capacitance
        self.r = ESR
        self.q = 0

    @property
    def v(self):
        return self.q/self.c

    def connect(self,cell,time):
        transferred = self.c*(self.v-cell.voltage)*math.e**(-time/(self.r*self.c))+self.c*(cell.voltage-self.v)
        cell.charge(-transferred/3600)
        self.q += transferred

cell1 = Cell(3.95,5)
cell2 = Cell(3.70,5)
cell3 = Cell(4.01,5)
cell4 = Cell(4.05,5)
cell5 = Cell(4.01,5)
cell6 = Cell(3.99,5)
cell7 = Cell(4.02,5)
cells = [cell1,cell2,cell3,cell4,cell5,cell6,cell7]

cap1 = Cap(.00096, .1)

frequency = 1000
error = .01

f = open("log.txt", "w")

i = 0
while True:
    cellvoltages = [cell.voltage for cell in cells]
    cellSortMin = [cell for cell in cells if cell.voltage == min(cellvoltages)]
    cellSortMax = [cell for cell in cells if cell.voltage == max(cellvoltages)]
    for j in range(1001):
        cap1.connect(cellSortMin[0], (1/frequency)/2)
        cap1.connect(cellSortMax[0], (1/frequency)/2)
    # cap1.connect(cell1, (1/frequency)/2)
    # cap2.connect(cell3, (1/frequency)/2)
    # cap3.connect(cell3, (1/frequency)/2)
    #
    # cap1.connect(cell2, (1/frequency)/2)
    # cap2.connect(cell2, (1/frequency)/2)
    # cap3.connect(cell4, (1/frequency)/2)
    # diffs = []
    # for j in range(3):
    #     diffs.append(abs([i.voltage for i in cells][j]-[i.voltage for i in cells][j+1]))
    # inUse = []
    # for k in range(3):
    #     biggest = diffs.index(sorted(diffs,reverse=True)[k])
    #     if cells[biggest] not in inUse and cells[biggest+1] not in inUse:
    #         caps[biggest].connect(cells[biggest], (1/frequency)/2)
    #         caps[biggest].connect(cells[biggest+1], (1/frequency)/2)
    #         inUse.extend([cells[biggest],cells[biggest+1]])

    if not i % 100000:
        print()
        print(f"time: {i*(1/frequency)} seconds.")
        for cell in cells:
            print(cell.voltage)
        f.write(",".join([str(cell.voltage) for cell in cells])+"\n")
        if max([i.voltage for i in cells])-min([i.voltage for i in cells]) < error:
            print(f"Done, took {i*(1/frequency)} seconds.")
            break
    i += j
f.close()
