import numpy as np

arr = np.arange(1, 7).reshape(2, 3)
print(arr)
# [[1 2 3]
#  [4 5 6]]

#Sumatorio
print(arr.sum()) # 21

#Media
print(arr.mean()) # 3.5

#Desviacion estandar
print(arr.std()) # 1.707825127659933

#varianza
print(arr.var()) # 2.9166666666666665


#Metodos de ordenacion
arr = np.random.randint(-10, 10, [3,3])
print(arr)
# [[-3 -3  2]
#  [ 8  4 -8]
#  [ 4 -5 -3]]

#Ordenar horizontalmente
arr.sort()
print(arr)
# [[-3 -3  2]
#  [-8  4  8]
#  [-5 -3  4]]

#Ordenar verticalmente
arr.sort(0)
print(arr)
# [[-8 -3  2]
#  [-5 -3  4]
#  [-3  4  8]]