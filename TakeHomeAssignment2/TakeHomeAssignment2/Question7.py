# Question 7

import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)

for index, row in df.iterrows():
    if row.sum() > 100:
        print(row)



