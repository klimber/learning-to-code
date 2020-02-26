from sklearn import datasets
from sklearn import svm
from matplotlib import pyplot as plt
import numpy as np

#Este dataset contém imagens de baixa resolução de números escritos à mão
digits = datasets.load_digits() 

#Como este é um dataset completo, ele possui os dados de imagens já preparados
print(digits.data)

#E os números verdadeiros para estas imagens
print(digits.target)

#É possível ver as imagens em formato de matriz
print(digits.images[0])

svm.SVC(ga)
clf = svm.SVC(gamma = 0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])

print(digits.images.shape)

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)

x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

#Caso os dados não estejam no formato adequando, é possível transformá-los usando
data = digits.images.reshape((digits.images.shape[0], -1))