import numpy as np 
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits #load digit images dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

digits = load_digits()
logisticRegr = LogisticRegression()


# # Visualize data from 0 to 4 (5 elements)
# plt.figure(figsize=(20,4))
# for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
#     plt.subplot(1, 5, index + 1)
#     plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
#     plt.title('Training: %i\n' % label, fontsize = 20)
# plt.show()

# Split train and test
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

# Train model
logisticRegr.fit(x_train, y_train)

predictions = logisticRegr.predict(x_test)

score = logisticRegr.score(x_test, y_test)
print(score)