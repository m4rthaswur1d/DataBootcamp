# Question 4

import numpy as np

iris_2d = np.genfromtxt('Question4_Iris', delimiter=',', dtype='float' , usecols=[0, 1, 2, 3])

for x in iris_2d[:, 0]:
    if x < 5.0:
        print(x)

for y in iris_2d[:, 2]:
    if y > 1.5:
        print(y)