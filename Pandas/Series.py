import numpy as np
import pandas as pd

#Listas - Arrays - Dict
etiquetas = ['A', 'B', 'C', 'D']

lista = [25, 50, 75, 100]
print(lista)

print(pd.Series(data=lista))
# 0     25
# 1     50
# 2     75
# 3    100

print(pd.Series(data=lista, index=etiquetas))
# A     25
# B     50
# C     75
# D    100


array = np.random.randint(50, size=4)
print(pd.Series(array, etiquetas))
# A    20
# B    18
# C     8
# D     9

print(pd.Series({'A':25, 'B':50, 'C':75, 'D':100}))
# A     25
# B     50
# C     75
# D    100


ingresos = pd.Series([100,300,200], index=['Enero', 'Febrero', 'Marzo'])
print(ingresos)
# Enero      100
# Febrero    300
# Marzo      200

print(ingresos[0]) # 100

#Metodos

gastos = pd.Series([100,150,250], index=['Enero', 'Febrero', 'Marzo'])
print(gastos)

total = ingresos.subtract(gastos)
print(total)
# Enero        0
# Febrero    150
# Marzo      -50