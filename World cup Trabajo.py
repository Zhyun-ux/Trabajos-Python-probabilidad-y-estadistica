import pandas as pd
import numpy as np
import random

dataset_path = 'worldcup.csv'
data = pd.read_csv(dataset_path)

print("Primeras filas del conjunto de datos:")
print(data.head())

data = data.dropna(subset=['Team'])

conglomerados = data.groupby('Team')

grupos_seleccionados = random.sample(list(conglomerados.groups.keys()), 3)

muestra_conglomerado = pd.concat([conglomerados.get_group(grupo) for grupo in grupos_seleccionados])

print("\nMuestreo Conglomerado (3 Equipos seleccionados):")
print(muestra_conglomerado)

team_selection = random.sample(data['Team'].unique().tolist(), 2)

muestra_polietapica = pd.concat([
    data[data['Team'] == team].sample(n=min(2, len(data[data['Team'] == team])), random_state=42) for team in team_selection])

print("\nMuestreo Polietápico (2 Continentes al azar):")
print(muestra_polietapica)

np.random.seed(55)
muestra_con_reposicion= data['Team'].sample(n=10,replace=True,random_state=55)
print("\nMuestreo con reposición de Team:")
print(muestra_con_reposicion)

data_ordenada= data.sort_values(by='Time')
muestra_sistematica= data_ordenada.iloc[::5]

print("\n Muestra sistematica de tiempo")
print(muestra_sistematica)