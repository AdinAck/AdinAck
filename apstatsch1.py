import matplotlib.pyplot as plt
import mplcursors

class Person:
    def __init__(self, group, rate):
        self.group, self.rate = group, rate

a = [
    Person('p', 69.169),
    Person('f', 99.692),
    Person('p', 70.169),
    Person('c', 80.369),
    Person('c', 87.446),
    Person('p', 75.985),
    Person('f', 83.400),
    Person('f', 102.154),
    Person('p', 86.446),
    Person('f', 80.277),
    Person('c', 90.015),
    Person('c', 99.046),

    Person('p', 68.862),
    Person('c', 87.231),
    Person('p', 64.169),
    Person('c', 91.754),
    Person('c', 87.785),
    Person('f', 91.354),
    Person('f', 100.877),
    Person('c', 77.800),
    Person('p', 97.538),
    Person('p', 85.000),
    Person('f', 101.062),
    Person('f', 97.046),

    Person('c', 84.738),
    Person('c', 84.877),
    Person('p', 58.692),
    Person('p', 79.662),
    Person('p', 69.231),
    Person('c', 73.277),
    Person('c', 84.523),
    Person('c', 70.877),
    Person('f', 89.815),
    Person('f', 98.200),
    Person('f', 76.908),
    Person('p', 69.538),

    Person('c', 75.477),
    Person('c', 62.646),
    Person('p', 70.077),
    Person('f', 88.015),
    Person('f', 81.600),
    Person('f', 86.985),
    Person('f', 92.492),
    Person('p', 72.262),
    Person('p', 65.446)
]

# for i in ['c', 'p', 'f']:
#     print(sorted([p.rate for p in a if p.group == i]))

names = ['c', 'p', 'f']
c = [p.rate for p in a if p.group == 'c']
p = [p.rate for p in a if p.group == 'p']
f = [p.rate for p in a if p.group == 'f']

plt.figure(figsize=(9, 3))

plt.subplot(131)
# plt.hist(c, bins=5)
plt.boxplot(c, vert=False)
plt.title("Control")
plt.subplot(132)
# plt.hist(p, bins=5)
plt.boxplot(p, vert=False)
plt.title("With Pet")
plt.subplot(133)
# plt.hist(f, bins=5)
plt.boxplot(f, vert=False)
plt.title("With Friend")
# plt.suptitle('People')

mplcursors.cursor(hover=True)
plt.show()
