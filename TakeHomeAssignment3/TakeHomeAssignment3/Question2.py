import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('dataLocal.csv')

# Tells computer that the format of hour_beginning is in dates and times and shows what the format looks
# like so that the computer will be able to extract information from this column.
data['hour_beginning'] = pd.to_datetime(data['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')

# Creates variable sorted by location (Brooklyn Bridge) and year (2019).
brooklyn_bridge_2019 = data[(data['location'] == 'Brooklyn Bridge') & (data['hour_beginning'].dt.year == 2019)]

# This for loop encodes the data into a new variable with numerical values associated with the weather column,
# it's sorting by different string possibilities in 'weather_summary'.
for weather in brooklyn_bridge_2019.columns:
    numerical_weather = pd.get_dummies(brooklyn_bridge_2019['weather_summary'], prefix='weather')

# Using pandas to concatenate the encoded weather column with the pedestrian data from constraints of Brooklyn Bridge
# and 2019.
final_data = pd.concat([numerical_weather, brooklyn_bridge_2019['Pedestrians']], axis=1)

# Calls correlation matrix
corr_matrix = final_data.corr()

# Information about matrix design/heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.75)
plt.title('Correlation Matrix of Weather and Pedestrian Counts')
plt.show()




