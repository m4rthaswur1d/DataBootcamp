# Numpy Question 1

import numpy as np

x = np.array(([3, 4, 5], [6, 7, 11]))
y = np.array(([5, 11, 12], [4, 14, 15]))

vertical = np.vstack((x, y))
horizontal = np.hstack((x, y))


# Numpy Question 2

def Question2(x, y):
    for element1 in x.flat:
        for element2 in y.flat:
            if element1 == element2:
                print(element1)


Question2(x, y)

# Numpy Question 3

for element in x.flat:
    if element >= 7:
        print(element)



