import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ahorros = [52, 104, 32, 65, 15, 76]
# plt.plot(ahorros)
# plt.show()

tiempo = np.random.randint(-100, 100, size=[3,3])
# plt.plot(tiempo)
# plt.show()

for t in range(1,11)[::-1]:
    plt.fill_between(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}"          # Leyenda para cada serie
    )
plt.title("Tablas")
plt.xlabel("Numero")
plt.ylabel("Resultado")
plt.legend()
plt.show()