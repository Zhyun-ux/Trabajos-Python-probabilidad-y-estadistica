import pandas as pd

def bondad_ajuste():
    num_categorias = int(input("Ingrese el número de categorías: "))
   
    categorias = []
    frecuencias_observadas = []
   
    for i in range(num_categorias):
        categoria = input(f"Ingrese el nombre de la categoría {i}: ")
        frecuencia = int(input(f"Ingrese la frecuencia observada de {categoria}: "))
       
        categorias.append(categoria)
        frecuencias_observadas.append(frecuencia)
   
    opcion = input("¿Desea ingresar las frecuencias esperadas? (s/n): ").strip().lower()
   
    if opcion == 's':
        frecuencias_esperadas = []
        for i in range(num_categorias):
            frecuencia = float(input(f"Ingrese la frecuencia esperada de {categorias[i]}: "))
            frecuencias_esperadas.append(frecuencia)
    else:
        total_observado = sum(frecuencias_observadas)
        frecuencias_esperadas = [total_observado / num_categorias] * num_categorias

    chi_cuadrado = sum(((fo - fe) ** 2) / fe for fo, fe in zip(frecuencias_observadas, frecuencias_esperadas))

    tabla = pd.DataFrame({
        "Categoría": categorias,
        "Frecuencia Observada": frecuencias_observadas,
        "Frecuencia Esperada": frecuencias_esperadas,
        "(FO - FE)^2 / FE": [((fo - fe) ** 2) / fe for fo, fe in zip(frecuencias_observadas, frecuencias_esperadas)]
    })

    print("\nTabla de Bondad de Ajuste:\n")
    print(tabla.to_string(index=False))
    print(f"\nValor Calculado: {chi_cuadrado:.4f}")

bondad_ajuste()