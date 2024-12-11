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

# QUESTION 1
# sets variables, the model is going to try to predict if a sample is in the household glass column or not given
# its aluminum content
X = np.array(glass.Al).reshape(-1,1)
y = glass.household

# splits data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state = 42)

# fits logistic regression model to the data
model = LogisticRegression()
model.fit(X_train, y_train)

# predict probabilities from independent variable testing data
probabilities = model.predict_proba(X_test)[:, 1]

# thresholds to experiment with
thresholds = [.4, .5, .6]

# this code iterates through the thresholds and determines the accuracy, precision, and recall of the
# given threshold
for threshold in thresholds:
    predictions = (probabilities >= threshold).astype(int)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)

    print("Threshold =" , threshold, "Accuracy = " ,accuracy, "precision = " ,precision, "recall = " ,recall)

