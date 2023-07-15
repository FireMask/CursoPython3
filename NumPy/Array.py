import numpy as np

#Crear un arreglo a partir de una lista
array = np.array([1, 2, 3, 4, 5])

print(type(array)) # <class 'numpy.ndarray'>
print(array) # [1 2 3 4 5]
print(array.ndim) # 1 (Numero de dimensiones)
print(array.shape) # (5,)

array = np.array(
    [
        [1,2,3,4,5],
        [1,2,3,4,5]
    ]
)
print(array.ndim) # 2 (Numero de dimensiones)
print(array.shape) # (2, 5) (2 filas, 5 columnas)

array = np.array([1, 2, 3, 4, 5])
print(array.dtype) # int32

array = np.array([1, 2, 3, 4, 5, 6.1416])
print(array.dtype) # float64

array = np.array(["Hola", "que", "tal"])
print(array.dtype) # <U4

array = np.array(["Hola", 123, 3.1416])
print(array.dtype) # <U32