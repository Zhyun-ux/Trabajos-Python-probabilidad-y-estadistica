import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "worldcup.csv"
df = pd.read_csv(file_path)

muestra = df["Time"].values

n = len(muestra)
x_bar = np.mean(muestra)
S_x2 = np.var(muestra, ddof=1)
S_x = np.sqrt(S_x2)
X2 = 0.5077

plt.figure(figsize=(8, 5))
plt.hist(muestra, bins=20, color="green", alpha=0.8, edgecolor="black")
plt.xlabel("Valores de Time - muestra")
plt.ylabel("Frecuencia")
plt.title("Histograma de la columna 'Time'")
plt.show()

print(f"Varianza muestral: {S_x2:.4f}")
print(f"Desviación típica muestral: {S_x:.4f}")
print(f"Distribución: {X2:.4f}")