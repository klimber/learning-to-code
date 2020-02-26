from sklearn import datasets
from sklearn import linear_model
import numpy as np

diabetes = datasets.load_diabetes()

diabetes_X_train = diabetes.data[:-20]
diabetes_y_train = diabetes.target[:-20]
diabetes_X_test = diabetes.data[-20:]
diabetes_y_test = diabetes.target[-20:]

regLinear = linear_model.LinearRegression()
regLinear.fit(diabetes_X_train, diabetes_y_train)

print(regLinear.coef_)

print(regLinear.predict(diabetes_X_test))
print(diabetes_y_test)

np.mean((regLinear.predict(diabetes_X_test) - diabetes_y_test)**2)

regLinear.score(diabetes_X_test, diabetes_y_test)