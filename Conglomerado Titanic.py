import pandas as pd
import numpy as np
import random

dataset_path = 'Titanic-Dataset.csv'
data = pd.read_csv(dataset_path)

print("Primeras filas del conjunto de datos:")
print(data.head())

data = data.dropna(subset=['Cabin'])

conglomerados = data.groupby('Cabin')

grupos_seleccionados = random.sample(list(conglomerados.groups.keys()), 2)

muestra_conglomerado = pd.concat([conglomerados.get_group(grupo) for grupo in grupos_seleccionados])

print("\nMuestreo Conglomerado (2 grupos seleccionados):")
print(muestra_conglomerado)

cabin_selection = random.sample(data['Cabin'].unique().tolist(), 2)

muestra_polietapica = pd.concat([
    data[data['Cabin'] == cabin].sample(n=min(3, len(data[data['Cabin'] == cabin])), random_state=42) 
    for cabin in cabin_selection
])

print("\nMuestreo Polietápico (3 filas de 2 cabinas seleccionadas o menos si hay pocas disponibles):")
print(muestra_polietapica)