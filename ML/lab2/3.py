import numpy as np 
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits #load digit images dataset
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

digits = load_digits()
gnb = GaussianNB()
mlpc = MLPClassifier()

# Split data and test
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

# Train model
gnb.fit(x_train, y_train)
mlpc.fit(x_train, y_train)

# Predictions
gnb_pred = gnb.predict(x_test)
mlpc_pred = mlpc.predict(x_test)

# Score
print("Guassian Näive Bayes:", gnb.score(x_test, y_test))
print("MLPClassifier:", mlpc.score(x_test, y_test))