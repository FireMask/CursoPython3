import numpy as np

#Array de ceros
array = np.zeros(3)
print(array) # [0. 0. 0.]

array = np.zeros([3,3])
print(array)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

#Array de unos
array = np.ones([3,3])
print(array)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

#Array de identidad
array = np.eye(3)
print(array)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

#Array de rangos

# Rango de 0 a 4
array = np.arange(4)
print(array) # [0 1 2 3]

# Rango de 0 a 4 decimal
array = np.arange(4.)
print(array) # [0. 1. 2. 3.]

# Rango de -3 a 3 [-3,3)
array = np.arange(-3, 4)
print(array) # [-3 -2 -1  0  1  2]

# Rango de 20 numeros a partir de 0 cada 5 numeros
array = np.arange(0, 20, 5)
print(array) # [ 0  5 10 15]