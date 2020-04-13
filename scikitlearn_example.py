import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

x_value, y_value = datasets.load_diabetes(return_X_y=True)
x_value = x_value[:, np.newaxis, 2]

x_train, x_test, y_train, y_test = train_test_split(x_value, y_value, test_size=0.31)

regression_example = linear_model.LinearRegression()
regression_example.fit(x_train, y_train)

gen_prediction = regression_example.predict(x_test)
