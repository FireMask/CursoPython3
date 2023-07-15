import numpy as np

#Numero decimal entre 0 y 1
print(np.random.rand()) # 0.9017255678793108

#Array 1D de decimales entre 0 y 1
print(np.random.rand(4)) # [0.26151543 0.66733974 0.70724755 0.81141435]

#Array 3D de decimales entre 0 y N
print(np.random.uniform(10, size=[2,2,2]))
# [[[4.98214771 7.27892074]
#   [1.89034144 7.09389246]]

#  [[3.56506393 1.91864999]
#   [4.15422722 8.74770969]]]

#Array 4D de decimales entre -N y M
print(np.random.uniform(-10, 10, size=[2,2,2,2]))
# [[[[-8.16332924 -8.12426657]
#    [-1.60182503 -1.93248278]]

#   [[ 0.94419453  3.38677827]
#    [-1.59284599  1.14190708]]]


#  [[[-9.86426726 -7.06628868]
#    [-8.90482127  5.6807693 ]]

#   [[-4.08952639 -6.6417443 ]
#    [ 9.3568404  -0.64015427]]]]

#Numero entero entre 0 y N
print(np.random.randint(10)) #8

#Array de enteros entre 0 y N
print(np.random.randint(10, size=[3,2]))
# [[4 0]
#  [1 9]
#  [1 5]]

#Array de enteros entre N y M
print(np.random.randint(-10, 10, size=[3,2]))
# [[  6   6]
#  [ -9  -3]
#  [ -6 -10]]

#Array uniforme con curva gaussiana
print(np.random.normal(size=20))
# [-0.68075177  1.9622063  -0.18522521 -1.40364779  0.06038315 -1.15438055
#  -1.04161305 -1.09195794 -1.90162361  0.85216992 -0.58475256  1.53789674
#   0.67399318 -0.10591911  0.67459307 -1.19153121 -0.39723666 -1.42343104
#   0.8230998  -0.36100738]



#Permutaciones --------------------------------------------------------------------
arr = np.arange(10)
np.random.shuffle(arr)
print(arr) # [8 1 4 3 6 9 2 7 0 5]
np.random.shuffle(arr)
print(arr) # [3 5 9 0 4 6 2 8 1 7]

print(np.random.permutation(15)) # [12  1 14  5  4 11  6  3  7  0  9 13  2  8 10]