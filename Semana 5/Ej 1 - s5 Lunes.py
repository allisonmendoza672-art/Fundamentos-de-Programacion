# Paso 1: Creae las dos matrices
matriz_a = [
    [1, 2]
    [3, 4]
]
matriz_b = [
    [5, 6]
    [7, 8]
]
# Paso 2: Crear matriz vacía para el resultado
resultado = []
# Paso 3: Recorrer las matrices y sumar 
for i in range(2): # 2 filas
    fila = [] # Creae fila vacía

    for j in range(2): # 2 columnas
        suma= matriz_a[i][j] + matriz_b[i][j] # Suma elementos
        suma = matriz_a[i][j] + matriz_b[i][j]# Sumar elementos
        fila.append(suma) # Agregar a la fila

    resultado.append(fila) # Agregar fila al resultado

# Pao 4: Mostrar resultado 
print("Matriz A:")
for fila in matriz_a:jjhiui
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\nMatriz B:")
for fila in matriz_b
    for elemento in fila:
        print(elemento, end=" ")

print("\nResultado A + B:")
for fila in resultado:
    for elemento in fila:
        print(elementpm end=" ")
    print()