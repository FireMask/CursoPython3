import numpy as np

arr_1 = np.random.randint(0, 4, [3,3])
print(arr_1)

#Guardado binario-------------------------------------------------
np.save('arr_1.npy', arr_1)

#Carga de archivo binario
arr_1 = np.load('arr_1.npy')
print(arr_1)

arr_2 = np.random.randint(-4, 0, [3,3])

#Guardado varios arrays en un solo archivo binario
np.savez('arrays.npz', arr_1=arr_1, arr_2=arr_2)

arrays = np.load('arrays.npz')
print(arrays['arr_1'])
print(arrays['arr_2'])


#Guardado texto----------------------------------------------------

arr_3 = np.random.randint(-10, 10, [3,3])
np.savetxt('arr_3.txt', arr_3, delimiter=',')
np.loadtxt('arr_3.txt', delimiter=',')
print(arr_3)