import sys
import data_retrieval
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import joblib

# Retrieve and clean dataset
data = data_retrieval.retrieve_data()

# Split up data into features and labels
x = data[0] # M -> 1, B -> 0
y = data[1]

# Split the dataset into training (80%) and testing (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.8)

# Build the classifier
classifier = tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)

# Make Prediction
# predictions = classifier.predict(x_test)
# print(accuracy_score(y_test,predictions))

# Save the model to disk
joblib.dump(classifier, 'classifier.joblib')