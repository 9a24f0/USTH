import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_excel("data/Exercise.xlsx",
                     sheet_name="Interest rates and home prices",
                     header=4, nrows=16, usecols=[1, 2])

x = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

# print trained model info
print(regressor.intercept_)
print(regressor.coef_)

# cal predicted value with trained model
y_pred = regressor.predict(x_test)

# print trained model info
print(regressor.intercept_)
print(regressor.coef_)

# cal predicted value with trained model
y_pred = regressor.predict(x_test)

# print diff between predict and actual
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# print error
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.plot(x, y, 'o', x_test, y_pred, '-')
plt.show()