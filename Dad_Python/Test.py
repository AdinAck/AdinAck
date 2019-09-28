import numpy as np

# If statements
a = "hello."
b = "goodbye!"

if ("!" in a or "." in a) and ("." in b or "!" in b):
    print("howdy doo!")

# For loops

a = np.array(["a", "b", "c", "d"])
np.size(a, 0)
for i in range(np.size(a, 0)):
    print(a[i])
