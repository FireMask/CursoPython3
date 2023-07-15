import numpy as np

arr = np.random.randint(0, 10, 30)

print(arr) # [8 8 7 3 0 8 9 9 4 3 8 6 3 0 7 0 2 1 0 9 0 9 8 4 4 8 4 1 6 0]

#Filtro unique
print(np.unique(arr)) # [0 1 2 3 4 6 7 8 9]

#Filtro en 1D
print(np.in1d([-1, 4, 8, 12], arr)) # [False  True  True False]

#Filtro where
arr_1 = np.random.uniform(-5, 5, size=[3,2])
print(arr_1)

arr_2 = np.where(arr_1 < 0, 0, arr_1)
# [[-1.50356853  2.64946346]
#  [ 3.29573212 -4.87699134]
#  [ 3.87049329  2.11934248]]
print(arr_2)
# [[0.         2.64946346]
#  [3.29573212 0.        ]
#  [3.87049329 2.11934248]]
arr_2 = np.where(arr_2 > 0, 0, arr_2)
print(arr_2)
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]

#Filtros boleanos
arr_bool = np.array([True, True, True, False])

#Comprobar si todos los elementos del array son True
print(arr_bool.all()) # False

#Comprobar si al menos un elemento del array es True
print(arr_bool.any()) # True

arr_bool_2d = np.array(
    [
        [False, True],
        [False, True],
        [False, True]
    ]
)

#Comprobar si alguna de las columnas es todo True
print(arr_bool_2d.all(0)) # [False  True]

#Comprobar si alguna de las filas tiene algun True
print(arr_bool_2d.any(1)) # [ True  True  True]