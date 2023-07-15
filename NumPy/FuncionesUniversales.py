import numpy as np

#Operaciones
    #Matematicas
    #Trigonometricas
    #Comparativas
    #Flotantes
    #Intercambio de bits

arr_1 = np.arange(1,6)
arr_2 = np.array([-3,7,3,13,0])

#Matematicas

#Suma
print(np.add(arr_1, arr_2)) # [-2  9  6 17  5]

#Resta
print(np.subtract(arr_2, arr_1)) # [-4  5  0  9 -5]

#Raiz cuadrada
print(np.sqrt(arr_1)) # [1.         1.41421356 1.73205081 2.         2.23606798]

#Potencia
print(np.power(arr_1, 2)) # [-4  5  0  9 -5]

#Signo
print(np.sign(arr_1)) # [1 1 1 1 1]


#Trigonometricas

#Seno
print(np.sin(arr_1))
# [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]

#Coseno
print(np.cos(arr_1))
# [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]

#Tangente
print(np.tan(arr_1))
# [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]

#Grados a radianes
print(np.deg2rad(arr_1))
# [0.01745329 0.03490659 0.05235988 0.06981317 0.08726646]

#Radianes a grados
print(np.rad2deg(arr_1))
# [ 57.29577951 114.59155903 171.88733854 229.18311805 286.47889757]


#Comparativas

#Maximo
print(np.maximum(arr_1, arr_2))
# [ 1  7  3 13  5]

#Minimo
print(np.minimum(arr_1, arr_2))
# [-3  2  3  4  0]

#Igual que
print(np.equal(arr_1, arr_2))
# [False False  True False False]

#Mayor que
print(np.greater(arr_1, arr_2))
# [ True False False False  True]


#Flotantes

#Array de prueba
arr_3 = np.array([3.14, 2.57, -6.4, 0.47, 5.5])

#Valor absoluto
print(np.fabs(arr_3))
# [3.14 2.57 6.4  0.47 5.5 ]

#Techo
print(np.ceil(arr_3))
# [ 4.  3. -6.  1.  6.]

#Suelo
print(np.floor(arr_3))
# [ 3.  2. -7.  0.  5.]

#Redondeo
print(np.round(arr_3))
# [ 3.  3. -6.  0.  6.]


#Intercambio de bits (bitshift)

#AND-----------------------------------------------------
print(np.binary_repr(13))       # 13d == 00001101b
print(np.binary_repr(17))       # 17d == 00010001b
print(np.bitwise_and(13, 17))   # 1d  == 00000001b

print(np.bitwise_and([14,3], 13)) # [12  1]
print(np.bitwise_and([11,7], [4,25])) # [0 1]
print(np.bitwise_and([True, True], [False, True])) # [False  True]

#Se puede usar & como atajo
x1 = np.array([2, 5, 255])
x2 = np.array([3, 14, 16])
print(x1 & x2) # [ 2  4 16]

#OR-----------------------------------------------------
print(np.binary_repr(13))       # 13d == 00001101b
print(np.binary_repr(17))       # 17d == 00010001b
print(np.bitwise_or(13, 17))    # 29d == 00011101b

print(np.bitwise_or([14,3], 13)) # [15 15]
print(np.bitwise_or([11,7], [4,25])) # [15 31]
print(np.bitwise_or([True, True], [False, True])) # [ True  True]

#Se puede usar | como atajo
x1 = np.array([2, 5, 255])
x2 = np.array([3, 14, 16])
print(x1 | x2) # [  3  15 255]

#XOR-----------------------------------------------------
print(np.binary_repr(13))       # 13d == 00001101b
print(np.binary_repr(17))       # 17d == 00010001b
print(np.bitwise_xor(13, 17))   # 28d == 00011100b

print(np.bitwise_xor([14,3], 13)) # [ 3 14]
print(np.bitwise_xor([11,7], [4,25])) # [15 30]
print(np.bitwise_xor([True, True], [False, True])) # [ True False]

#Se puede usar | como atajo
x1 = np.array([2, 5, 255])
x2 = np.array([3, 14, 16])
print(x1 ^ x2) # [  1  11 239]

#Invert-----------------------------------------------------
# bitwise_not is an alias for invert:
print(np.bitwise_not is np.invert) # True

print(np.binary_repr(13))                   # 13d  == 00001101b
x = np.invert(np.array(13, dtype=np.uint8)) # 242d == 11110010b   
print(x) # 242

# The result depends on the bit-width:
print(np.binary_repr(13))                   # 00013d == 0000000000001101b
x = np.invert(np.array(13, dtype=np.uint16))# 65522d == 1111111111110010b
print(x) # 65522

# Al usar enteros con signo los resultados son los dos complementos del resultado para los sin signo
print(np.binary_repr(13))                       #  13d == 00001101b
print(np.invert(np.array([13], dtype=np.int8))) # -14d == 11110010b

# The ~ operator can be used as a shorthand for np.invert on ndarrays.
print(np.invert(np.array([True, False]))) # [False  True]
x1 = np.array([True, False])
print(~x1) # [False  True]

#Left Shift -----------------------------------------------------
print(np.binary_repr(5))    # 05d == 00101b
print(np.left_shift(5, 2))  # 20d == 10100b

print(np.left_shift(5, [1,2,3])) # [10 20 40]
print(np.binary_repr(5))    # 05d == 000101b
print(np.binary_repr(10))   # 10d == 001010b
print(np.binary_repr(20))   # 20d == 010100b
print(np.binary_repr(40))   # 40d == 101000b

# The << operator can be used as a shorthand for np.left_shift on ndarrays.
x1 = 5
x2 = np.array([1, 2, 3])
print(x1 << x2) # [10 20 40]

#Right Shift -----------------------------------------------------
print(np.binary_repr(10))    # 10d == 01010b
print(np.right_shift(10, 1))  # 05d == 00101b

print(np.right_shift(10, [1,2,3])) # [5, 2, 1]
print(np.binary_repr(10))  # 10d == 01010b
print(np.binary_repr(5))   # 05d == 00101b
print(np.binary_repr(2))   # 02d == 00010b
print(np.binary_repr(1))   # 01d == 00001b

# The << operator can be used as a shorthand for np.left_shift on ndarrays.
x1 = 10
x2 = np.array([1, 2, 3])
print(x1 >> x2) # [5, 2, 1]

#Pack Bits -----------------------------------------------------
a = np.array(
[
    [
        [1,0,1],
        [0,1,0]
    ],
    [
        [1,1,0],
        [0,0,1]
    ]
])
print(np.packbits(a, axis=-1))
# [
#     [
#         [160] # 1010 0000
#         [ 64] # 0100 0000
#     ]
#     [
#         [192] # 1100 0000
#         [ 32] # 0010 0000
#     ]
# ] dtype=uint8