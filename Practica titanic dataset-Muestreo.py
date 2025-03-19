import pandas as pd
import numpy as np
import random

dataset_path = 'Titanic-Dataset.csv'
data = pd.read_csv(dataset_path)

print("primeras 10 filas:")
print(data.head(10))

np.random.seed(55)
muestra_con_reposicion= data.sample(n=10,replace=True,random_state=55)
print("\nMuestreo con reposición:")
print(muestra_con_reposicion)

np.random.seed(55)
muestra_sin_reposicion= data.sample(n=10,replace=False,random_state=55)
print("\nMuestreo sin reposición:")
print(muestra_sin_reposicion)

random.seed(15)

total_population = 55
sample_size= 11
first_element= random.randint(1,total_population)
print(f"primer elemento seleccionado: {first_element}")

increment= total_population // sample_size
print(f"Incremento sistematico : {increment}")

systematic_sample = [(first_element + i * increment) % total_population for i in range (sample_size)]
print(f"Muestra sistematica:{systematic_sample}")