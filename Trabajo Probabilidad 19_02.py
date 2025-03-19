import numpy as np
import matplotlib.pyplot as plt
import random 

# 1. Crear una población ficticia
np.random.seed(42)
poblacion = np.random.randint(1, 101, 500)  # 500 valores entre 1 y 100
print("Primeros 10 valores de la población:", poblacion[:10])

# Muestreo aleatorio simple con reemplazo
muestra_con_reemplazo = np.random.choice(poblacion, size=30, replace=True)
media_con_reemplazo = np.mean(muestra_con_reemplazo)

# Muestreo aleatorio simple sin reemplazo
muestra_sin_reemplazo = np.random.choice(poblacion, size=30, replace=False)
media_sin_reemplazo = np.mean(muestra_sin_reemplazo)

# Imprimir resultados
print("Muestra con reemplazo:", muestra_con_reemplazo)
print("Media muestral con reemplazo:", media_con_reemplazo)
print("Muestra sin reemplazo:", muestra_sin_reemplazo)
print("Media muestral sin reemplazo:", media_sin_reemplazo)

random.seed(15)

total_population = 30
sample_size= 6
first_element= random.randint(1,total_population)
print(f"primer elemento seleccionado: {first_element}")

increment= total_population // sample_size
print(f"Incremento sistematico : {increment}")

systematic_sample = [(first_element + i * increment) % total_population for i in range (sample_size)]
print(f"Muestra sistematica:{systematic_sample}")

num_grupos = 10
tamano_grupo = 50
conglomerados = [poblacion[i * tamano_grupo:(i + 1) * tamano_grupo] for i in range(num_grupos)]
conglomerados_seleccionados = random.sample(conglomerados, 3)
print("Muestreo por conglomerados (grupos completos seleccionados):")
for i, grupo in enumerate(conglomerados_seleccionados, 1):
    print(f"Grupo {i}: {grupo}")

print("\nMuestreo polietápico (valores seleccionados dentro de cada grupo):")
grupos_polietapicos = random.sample(conglomerados, 3)
for i, grupo in enumerate(grupos_polietapicos, 1):
    valores_seleccionados = random.sample(grupo, 5)
    print(f"Grupo {i}: {valores_seleccionados}")