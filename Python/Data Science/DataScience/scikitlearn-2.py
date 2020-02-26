from sklearn import datasets
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris_X = datasets.load_iris().data
iris_y = datasets.load_iris().target
# Split iris data in train and test data
# A random permutation, to split the data randomly
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

# Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train) 

knn.predict(iris_X_test)

iris_y_test
