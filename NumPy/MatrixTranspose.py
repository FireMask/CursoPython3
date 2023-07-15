import numpy as np

# Array Transpuesto
# Un array transpuesto es el reflejo de otro, de manera que las columnas se vuelven filas y las filas, columnas.

arr = np.array([
    [1,2,3],
    [4,5,6]]
)

print(arr)
# [[1 2 3]
#  [4 5 6]]
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]
print(arr.T.T)
# [[1 2 3]
#  [4 5 6]]

#Intercambiar filas por columnas
print(arr.swapaxes(0,1)) # print(arr.swapaxes(1,0))
# [[1 4]
#  [2 5]
#  [3 6]]