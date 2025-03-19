import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "Titanic-Dataset.csv"
df = pd.read_csv(file_path)

muestra = df["Fare"].values

n = len(muestra)
x_bar = np.mean(muestra)
S_x2 = np.var(muestra, ddof=1)
S_x = np.sqrt(S_x2)
X2 = 0.5063

plt.figure(figsize=(7, 4))
plt.hist(muestra, bins=10, color="blue", alpha=0.8, edgecolor="black")
plt.xlabel("Valores de Fare - muestra")
plt.ylabel("Frecuencia")
plt.title("Histograma de la columna 'Fare'")
plt.show()

print(f"Varianza muestral: {S_x2:.4f}")
print(f"Desviación típica muestral: {S_x:.4f}")
print(f"Distribución: {X2:.4f}")