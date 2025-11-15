# Suma d matrices de 3x3
matriz_a = [
    [1, 2, 3],
    [4, 5, 5]
    [7, 8, 9]
]
matriz_b = [
    [9, 8, 7]
    [6, 5, 4]
    [3, 2, 1]
]
# Crear matriz resultado
resultado = []
# Sumar elemento por elemento
for i in range(3): # 3 filas
    fila = []
    for j in range(3): # 3 coumnas
        suma = matriz_a[i][j] + matriz_b[i][j]
        fila.append(suma)

    resultado.append(fila)
# Mostrar resultado
for fila in resultado:
    for elemento in fila:
        pront(elemeneto, end=" ")
    print()

    
