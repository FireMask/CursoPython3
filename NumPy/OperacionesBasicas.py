import numpy as np

# Suma

# Dos arrays
array_1 = np.array([1,2,3,4])
array_2 = np.array([5,6,7,8])
print(array_1 + array_2) # [ 6  8 10 12]

array_3 = np.array([9,10])
# print(array_2 + array_3) # ValueError: operands could not be broadcast together with shapes (4,) (2,)


# Resta (Las matrices deben tener las mismas dimensiones)
print(array_1 - array_1) # [0 0 0 0]


# Producto
print(array_1 * array_2) # [ 5 12 21 32]

print(array_1 * 10) # [10 20 30 40]
print(array_1 * np.array(10)) # [10 20 30 40]


# Division
print(array_1 / array_2) # [0.2        0.33333333 0.42857143 0.5       ]
print(array_1 / 2) # [0.5 1.  1.5 2. ]

print(1 / array_1)      # [1.         0.5        0.33333333 0.25      ]
print(array_1 ** -1.)   # [1.         0.5        0.33333333 0.25      ]


#Potencia
print(array_1 ** array_2) # [    1    64  2187 65536]


# Operaciones en arrays 2D
array_5 = np.array([
    [1,2],
    [3,4]
])
array_6 = np.array([
    [5,6],
    [7,8]
])

print(array_5 + array_6)
# [[ 6  8]
#  [10 12]]

print(array_5 * 3)
# [[ 3  6]
#  [ 9 12]]

print(array_5)
# [[1 2]
#  [3 4]]
print(array_5 * np.array([5,10]))
# [[ 5 20]
#  [15 40]]

# print(array_5 * np.array([5,10,15]))
#ValueError: operands could not be broadcast together with shapes (2,2) (3,)