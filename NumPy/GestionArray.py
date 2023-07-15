import numpy as np

arr = np.arange(0, 50, 5)

print(arr) # [ 0  5 10 15 20 25 30 35 40 45]

#Primera posicion
print(arr[0]) # 0

#Quinta posicion
print(arr[4]) # 20

#Ultima posicion
print(arr[-1]) # 45

#Asignacion de un valor
arr[-1] = 99
print(arr) # [ 0  5 10 15 20 25 30 35 40 99]

#Slicing

#Copia completa de principio a fin
print(arr[:]) # [ 0  5 10 15 20 25 30 35 40 99]

#Subarray de los primeros 3 elementos
print(arr[:3]) # [ 0  5 10]

#Modificar rango de forma masiva todos, excepto el primero y el ultimo
arr[1:-1] = 50
print(arr) # [ 0 50 50 50 50 50 50 50 50 99]


#Consideraciones
arr = np.arange(0,30,3)
print(arr) # [ 0  3  6  9 12 15 18 21 24 27]

sub_arr = arr[0:4]
print(sub_arr) # [0 3 6 9]

sub_arr[:] = 99
print(sub_arr) # [99 99 99 99]
print(arr) # [99 99 99 99 12 15 18 21 24 27]

#FIX
arr = np.arange(0,30,3)
print(arr) # [ 0  3  6  9 12 15 18 21 24 27]

sub_arr = arr[0:4].copy() # <----------------------------
print(sub_arr) # [0 3 6 9]

sub_arr[:] = 99
print(sub_arr) # [99 99 99 99]
print(arr) # [ 0  3  6  9 12 15 18 21 24 27]