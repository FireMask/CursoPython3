import numpy as np
import pandas as pd

array = np.random.uniform(-10, 10, size=[4,4])

df = pd.DataFrame(array, index=['A', 'B', 'C', 'D'], columns=['W', 'X', 'Y', 'Z'])

print(df)
#           W         X         Y         Z
# A  3.714738  4.588527  5.557886  7.255742
# B -1.246925  4.749149 -4.819347 -2.980105
# C -5.905175 -8.254379 -1.349752  2.285101
# D  6.817707  9.060194  1.925654 -2.900373

print(df['X'])
# A    4.588527
# B    4.749149
# C   -8.254379
# D    9.060194

print(df[['X', 'Z']])

df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)

# axis = 1 especificar que se quiere borrar la columna
print(df.drop('TOTAL', axis=1))
print(df)

df.drop('TOTAL', axis=1, inplace=True)
print(df)


#Borrar fila
df.drop('D', axis=0, inplace=True)
print(df)

#Selecionar filas
print(df.loc['C'])

#Seleccionar subset
print(df.loc['C', 'Z'])

print(df.loc[['A', 'B'], ['W', 'Y']])

print(df>0)
#        W      X      Y      Z
# A  False   True   True   True
# B   True   True  False  False
# C   True  False   True   True

print(df[df>0])
#           W         X         Y         Z
# A  0.024620  4.438784  0.263304       NaN
# B  9.780511  3.054995  6.432869  3.437758
# C       NaN       NaN  0.011998       NaN

print(df[df['X']>0])
#           W         X         Y         Z
# A -4.839405  7.815586 -9.686872 -2.105450
# C -0.360109  4.509590 -4.532884 -2.336743]

print(df[df['X']>0][['Y','Z']])
#           Y         Z
# A -6.478033  8.198089

print(df[(df['X']>0) | (df['Z']>0)])
#           W         X         Y        Z
# A -5.546236 -3.966111 -3.414348  9.02496