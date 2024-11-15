# libraries to be used
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler

import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", 101)

# will use z-score standardization because the data appears to be in a bell curve :)
# replace null values with means. I decided to use means not medians because the data follows a bell curve

data = pd.read_csv('.idea/employee.csv')
data.loc[data['hours_per_week'].isna(), 'hours_per_week'] = data['hours_per_week'].mean()
data.loc[data['telecommute_days_per_week'].isna(), 'telecommute_days_per_week'] = data['telecommute_days_per_week'].mean()

# making a data frame from the independent variables using pandas, i'm only using columns with numerical values
# that the model can be trained on, even though others could be seen as important. these values chosen below
# follow a bell curve. even if I was able to convert certain values like "yes or no" into 1s and 0s it would not
# follow a bell curve and be impossible/not useful to train a model on this data.

df = pd.DataFrame(data)
x_cols = ['hours_per_week', 'telecommute_days_per_week', 'job_years']
x_df = df[x_cols]

# this block of code converts the data into normal distribution that can be used more effectively
scaler = StandardScaler()
standardized_data_x = scaler.fit_transform(x_df)
standardized_df_x = pd.DataFrame(standardized_data_x, columns=x_cols)
print(standardized_df_x)

# same for to process the dependent variable, salary
y_cols = ['salary']
y_df = df[y_cols]
scaler = StandardScaler()

scaler = StandardScaler()
standardized_data_y = scaler.fit_transform(y_df)
standardized_df_y = pd.DataFrame(standardized_data_y, columns=y_cols)
print(standardized_df_y)

# initializes the model, lets it know the train and test data frames. i decided to make the test size 20% of the given data
# in employee.csv because then the rest can be used to see how effective the model is (the test data)
X_train, X_test, y_train, y_test = train_test_split(standardized_df_x, standardized_df_y, test_size=0.2, random_state=42)

# linear regression line on the data that's being trained... self explanatory
reg = LinearRegression()
reg.fit(X_train, y_train)
print(reg.coef_)
print(reg.intercept_)

# trains the data to be used to then predict for the test data
X_train
y_train

# calculates mean square error
mean_squared_error(y_train, reg.predict(X_train))/np.mean(y_train)

# y_predict right here is the most important line of code. this is what we're looking for. it predicts the output, salar from
# the trained model of X. this is a function that gives us what this whole program is looking for ^-^
y_predict = reg.predict(X_test)

# uses mean squared error function for the predicted data
mse = mean_squared_error(y_predict, y_test)/np.mean(y_test)
print("Mean Squared Error:", mse)







