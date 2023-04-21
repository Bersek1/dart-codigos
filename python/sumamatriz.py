import numpy as np

# Pedir al usuario el número de filas y columnas
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Crear la primera matriz
matriz_1 = np.zeros((filas, columnas))
print("ingrese los elementos de la matriz 1 \n")
for i in range(filas):
    for j in range(columnas):
        matriz_1[i][j] = float(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))

# Crear la segunda matriz
matriz_2 = np.zeros((filas, columnas))
print("ingrese los elementos de la matriz 2 \n")
for i in range(filas):
    for j in range(columnas):
        matriz_2[i][j] = float(input(f"Ingrese el valor para la fila {i+1}, columna {j+1}: "))

# Función para sumar las matrices
def sumar_matrices(matriz1, matriz2):
    return np.add(matriz1, matriz2)

# Función para restar las matrices
def restar_matrices(matriz1, matriz2):
    return np.subtract(matriz1, matriz2)

# Sumar las matrices 
matriz_suma = sumar_matrices(matriz_1, matriz_2)
print("la suma de las matrices es:")
print(matriz_suma)

# Restar las matrices
matriz_resta = restar_matrices(matriz_1, matriz_2)
print("la resta de las matrices es:")
print(matriz_resta)
