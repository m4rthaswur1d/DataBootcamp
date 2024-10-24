import pandas as pd

data = pd.read_csv('dataLocal.csv')

# Defines function to categorize hours into times of day
def time_of_day(hour):
    if 6 <= hour < 11:
        return 'morning'
    elif 11 <= hour < 18:
        return 'afternoon'
    elif 18 <= hour < 23:
        return 'evening'
    else:
        return 'night'

# Convert 'hour_beginning' to the datetime format to be able to extract the hour (in the next line), sets up
# code and lets computer know that we will be dealing with this data in a certain format
data['hour_beginning'] = pd.to_datetime(data['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')

# Extract hour from 'hour_beginning' to apply the function
data['time_of_day'] = data['hour_beginning'].dt.hour.apply(time_of_day)

# Group by the time of day and add up all the pedestrian counts for each time of day
counts_per_time_of_day = data.groupby('time_of_day')['Pedestrians'].sum()

# Print results
print(counts_per_time_of_day)

