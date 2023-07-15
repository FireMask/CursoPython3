import numpy as np

arr_2d = np.array([
    [0,  5,  10],
    [15, 20, 25],
    [30, 35, 40],
])

#Primera fila
print(arr_2d[0]) # [ 0  5 10]

#Primera fila y primera columna
print(arr_2d[0][0]) # 0

#Ultima fila y ultima columna
print(arr_2d[-1][-1]) # 40

#Edicion de la primer columna en la ultima fila\
arr_2d[-1][0] = 99
print(arr_2d)
# [[ 0  5 10]
#  [15 20 25]
#  [99 35 40]]



#Slicing 2D

#Subarray con todas las filas y columnas
print(arr_2d[:,:])
# [[ 0  5 10]
#  [15 20 25]
#  [99 35 40]]

#Subarray de las dos primeras filas
print(arr_2d[:2,:])
# [[ 0  5 10]
#  [15 20 25]]

#Subarray de la primer columna
print(arr_2d[:,:1])
# [[ 0]
#  [15]
#  [99]]

#Edicion masiva de la segunda columna
arr_2d[:,1:2] = 99
print(arr_2d)
# [[ 0 99 10]
#  [15 99 25]
#  [99 99 40]]

#Edicion masiva de la ultima fila
arr_2d[-1,:] = 88
print(arr_2d)
# [[ 0 99 10]
#  [15 99 25]
#  [88 88 88]]


#Fancy Index

#Creamos array 2D de ceros
arr_2d = np.zeros((5,10))
print(arr_2d)
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

#Modificacion masiva de la primera, tercera y ultima fila
arr_2d[[0, 2, -1]] = 5
print(arr_2d)
# [[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]]

#Consulta a voluntar, incluso repitiendo filas
print(arr_2d[[0,1,1,1,0]])
# [[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]]


#Bucles
for fila in arr_2d:
    print(fila)
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

for i, row in enumerate(arr_2d):
    for j, col in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j
print(arr_2d)
# [[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]
#  [10. 11. 12. 13. 14. 15. 16. 17. 18. 19.]
#  [20. 21. 22. 23. 24. 25. 26. 27. 28. 29.]
#  [30. 31. 32. 33. 34. 35. 36. 37. 38. 39.]
#  [40. 41. 42. 43. 44. 45. 46. 47. 48. 49.]]


#Arrays 3D y mas dimensiones
arr_3d = np.array(
    [
        [
            [1, 2],
            [3, 4],
        ],
        [
            [5, 6],
            [7, 8],
        ]
    ]
)
print(arr_3d)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

arr_3d = np.zeros([2,2,2])
print(arr_3d)
# [[[0. 0.]
#   [0. 0.]]

#  [[0. 0.]
#   [0. 0.]]]

arr_4d = np.ones([2,2,2,2])
print(arr_4d)
# [[[[1. 1.]
#    [1. 1.]]

#   [[1. 1.]
#    [1. 1.]]]


#  [[[1. 1.]
#    [1. 1.]]

#   [[1. 1.]
#    [1. 1.]]]]

#Reshape
arr_2d = np.arange(9).reshape(3,3)
print(arr_2d)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# arr_2d = np.arange(9).reshape(3,3,3) # ValueError: cannot reshape array of size 9 into shape (3,3,3)
# print(arr_2d) 

arr_2d = np.arange(27).reshape(3,3,3) # ValueError: cannot reshape array of size 9 into shape (3,3,3)
print(arr_2d) 
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]

#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]

#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]