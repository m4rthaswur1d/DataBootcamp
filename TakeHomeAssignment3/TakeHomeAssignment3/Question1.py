import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataLocal.csv')

# Tells computer about format of column hour_beginning and that it must extract a specific value from this
# format, the day name.
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df['weekday'] = df['hour_beginning'].dt.day_name()

# Initializes days of week that will be used in plot
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Initializes data frame that will be used to calculate mean values for pedestrian counts.
mean_results = pd.DataFrame(columns=['weekday', 'Pedestrians'])

# This for loop iterates through weekdays to calculate mean pedestrian counts
for day in days_of_week:
    filtered_df = df[df['weekday'] == day]
    mean_values = filtered_df.mean(numeric_only=True)
    mean_values['weekday'] = day
    mean_results = mean_results._append(mean_values, ignore_index=True)


# Creates plot with information about plot like color, markings, axis names, and size
plt.figure(figsize=(10, 6))
plt.plot(mean_results['weekday'], mean_results['Pedestrians'], marker='o', color='teal')
plt.title('Pedestrian Counts Per Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()








