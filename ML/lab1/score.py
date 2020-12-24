import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


data = pd.read_csv("/home/meteora/USTH/ML/lab1/data/student_scores.csv")

# display, uncomment plt.show to see the figure
data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
# plt.show()

# get X to a col vector while y is row vector
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

# split data into 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# print trained model info
print(regressor.intercept_)
print(regressor.coef_)

# cal predicted value with trained model
y_pred = regressor.predict(X_test)

# print diff between predict and actual
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# print error
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))