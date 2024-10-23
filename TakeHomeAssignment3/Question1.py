import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataLocal.csv')


df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')
df['weekday'] = df['hour_beginning'].dt.day_name()


days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


mean_results = pd.DataFrame(columns=['weekday', 'Pedestrians'])


for day in days_of_week:
    filtered_df = df[df['weekday'] == day]
    mean_values = filtered_df.mean(numeric_only=True)
    mean_values['weekday'] = day
    mean_results = mean_results._append(mean_values, ignore_index=True)


mean_results.rename(columns={'count': 'Pedestrians'}, inplace=True)



plt.figure(figsize=(12, 6))
plt.plot(mean_results['weekday'], mean_results['Pedestrians'], marker='o', color='pink')
plt.title('Pedestrian Counts Per Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()








