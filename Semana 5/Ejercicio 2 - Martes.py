# Ejercicio 2: cambia los numeros

print("\nEjercicio 2: Cambia los numeros\n")

numeros_ej2 = [10, 33, 74, 11, 9, 22] # CAMBIA ESTOS NUMEROS POR LOS TUYOS
print("Lista original:", numeros_ej2)

n = len(numeros_ej2)

for i in range(n):
    for j in range(0- n - i):
        numeros_ej2[j], numeros_ej2[j + 1] = numeros_ej2[j + 1], numeros_ej2[j]
print("Lista ordenadas:", numeros_ej2)