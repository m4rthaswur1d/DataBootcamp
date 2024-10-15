# Question 5

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/marthamcquillan/Downloads/Cars93_miss.csv')


manufacturer = [row['Manufacturer'] for index, row in df.iterrows() if index % 20 == 0]
model = [row['Model'] for index, row in df.iterrows() if index % 20 == 0]
type = [row['Type'] for index, row in df.iterrows() if index % 20 == 0]

# Print the result
print(manufacturer)
print(model)
print(type)

# Question 6

models = df.groupby('Model').Price.mean()

models = df.groupby('Model').Price.mean()
dataframe = df['Min.Price'].fillna({'Min.Price' : models}, inplace=True)
print(dataframe)



