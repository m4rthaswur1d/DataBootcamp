# QUESTION 2
# Now we're going to look at more columns (all of them) and use logistic regression to analyze them

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

glass = pd.read_csv('glass.csv')
print(glass.head())

# this block of code maps types 5, 6, and 7 to a new column called household which is
# what we're interested in. the 0's and 1's determine if each type of glass is intended
# for household purposes
glass['household'] = glass.Type.map({1:0, 2:0, 3:0, 5:1, 6:1, 7:1})
glass.household.value_counts()


elements = ['RI', 'Na', 'Mg', 'Si', 'K', 'Ca', 'Ba', 'Fe']
for element in elements:
    X = np.array(glass[element]).reshape(-1, 1)
    y = glass.household

    # split the data into training and testing data sets by 30%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict probabilities
    probabilities = model.predict_proba(X_test)[:, 1]  # Probability of belonging to the household class

    # choose thresholds
    thresholds = [0.1, .15, .2, .25, .3, .35, .4, .45]


    # Evaluate different thresholds
    for threshold in thresholds:
        predictions = (probabilities >= threshold).astype(int)

        # this code iterates through the thresholds and determines the accuracy, precision, and recall of the
        # given threshold
        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)

        print("Threshold =", threshold, "Accuracy = ", accuracy, "precision = ", precision, "recall = ", recall)


# Question 3
X = glass.drop(columns=['Type', 'household'])
y = glass['household']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

numeric =  X.select_dtypes(include=['float64']).columns
categorical = X.select_dtypes(include=['object']).columns

