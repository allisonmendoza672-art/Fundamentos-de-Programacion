#Ejemplo 1 con print

print("Ejemplo 1\n")

# Instrucción 1
nombre = "Abi"

# Instrucción 2
edad = 17

# Instrucción 3
print("Hola, soy", nombre)

#Instrucción 4 
print("Tengo", edad, "años")


#Ejemplo 2 con print 
#2. Nueva Línea (\n)
print("\nEjemplo 2\n")

# Sin \n (todo en una línea)
print("Hola Mundo")
# Salida: Hola Mundo

# Con \n (salto de línea)
print("Hola\nMundo")

# Múltiples \n
print("Línea 1\nLínea 2\nLínea 3")


#Ejemplo 3 con tabulacion
print("\nEjemplo 3\n")

print("Nombre:\tEstefi")
print("Edad:\t16")
print("Ciudad:\tMonterrey")


#Ejemplo 4 con tabulacion
print("\nEjemplo 4\n")

#Crear una conversación de chat 
print("Ana:\tHola, ¿cómo estás?")
print("Luis:\tBien, ¿y tú?")
print("Ana:\t¡Genial!\n")
print("===== Chat guardado en =====")
print("C:\\Users\\L01448464\\Documents\\chat.txt")


#Ejemplo 5 
print("\nEjemplo 5\n") 

# Dos argumentos
print("Hola", "Mundo")
#Salida: Hola Mundo
#            ↑
#          espacio automático

# Tres argumentos
print("Me", "gusta", "dibujar")

#Mezclando tipos de datos 
print("Tengo", 2, "mascotas en mi casa")

# Con variables
nombre = "Fer"
cantidad_hermanos = 2
print("Me dicen", nombre, "y tengo", cantidad_hermanos, "hermanos")


#Ejemplo 6. OPERADORES ARITMÉTICOS
print("Ejercicio 6. OPERADORES ARITMÉTICOS")
#SUMA (+): vamos a sumar dos números
numero1 = 42 
numero2 = 22
suma = numero1 + numero2
print("Operador suma:", suma)

#RESTA (-): ahora vamos a restar
resta = numero1 + numero2
print ("Operador restas:", resta)

#MULTIPLICACIÓN (*): multiplicación dos números
multiplicación = numero1 * numero2
print("Operador multiplicacion:", multiplicación)

#DIVISIÓN (/): dividimos y obtenemos resultado con decimales 
division = numero1 / numero2
print("Operador division:",division)

#DIVISIÓN ENTERA (//): dividimso pero solo quremos la parte entera
division_entera  = 10 // 3
print ("Operador division entera:", division_entera)

# (%): obtiene el residuo (lo que sobra ) de una división
residuo = 10 % 3
print("Operador residuo:", residuo)

#POTENCIA (**): elevar un número a una potencia 
potencia = 2 ** 3
print("Operador potencia:", potencia)


# Ejercicio 7 Operadores de comparación 
print("Ejercicio 7. Operadores de comparación")

print("¿He aprobado o no la materia")
# MAYOR O IGUAL (>): La calificación mínima para pasar es 70
calificacion = 70
resultado5 = calificacion >= 70
print("Aprobé?:", resultado5)

#MAYOR (>): La calificación mínima para pasar es 70
resultado6 = calificacion > 70
print("Aprobé?:", resultado6)

# Vamos a comprar estos dos números 
mi_edad = 17
edad_minima = 18

#IGUAL A (==): Pregunta ¿Los números son iguales?
resultado1 = mi_edad == 15
print("\n¿Soy mayor de edad? (==):", resultado1)

#DIFERETE DE (!=): Pregunta: ¿Los números son diferentes)
resultdo2 = mi_edad != 20
print("¿Tengo 18 años? (!=):", resultdo2)

#MENOR QUE (<): Pregunta: ¿El primer número es menor?
resultado3 = mi_edad < 18
print ("Mi edad es menor que 18 (>):", resultado3)

#MENOR O IGUAL (<=): Pregunta : ¿ES menor o igual?
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):", resultado4)


#Ejercicio 8. Operadores lógicos
print("Ejercicio 8. Operadores lógicos")
# Imaginemos que queremos entrar a un juego online
tengo_internet = True # Sí tengo internet
tengo_cuenta = True # Sí tengo cuenta

# AND (y): Las DOS condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar (ambas True):", puedo_jugar)

#Probemos cuando falta algo 
tengo_internet2 = True 
tengo_cuenta2 = False 
peuedo_jugar2 = tengo_internet2 and tengo_cuenta2
print8("¿Puedo jugar? (una es False):", peuedo_jugar2)

#OR (o): Al menos UNA condición debe ser verdadera
tengo_celular = True 
tengo_tablet = False 
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menos una True):", tengo_dispositivo)

#NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)


#Ejercicio 9. Operadores de asignación 
print("Ejercicio 9. Operadores de asignación\n")

#ASIGNACIÓN SIMPLE (=): Guardamos un valor en una variable 
puntos = 0
print("Puntos iniciales:", puntos)

#SUMA Y ASIGNA (+=): Es lo mismo que escribir: puntos = puntos + 10 
puntos += 10
print("GANASTE 10 PUNTOS (+=):", puntos)

#RESTA Y ASIGNA (-=): Es lo mismo que escribir: puntos = puntos - 5
puntos -= 5
print("Perdiste 5 puntos (-=):", puntos)

#MULTIPLICA Y ASIGNA (*=): Es lo mismo que escribir: puntos = puntos * 2
puntos *= 2
print("¡Puntos x2! (*=):", puntos)

#DIVIDE Y ASIGNA (/=): Es lo mismo que escribir. puntos = puntos / 2
puntos /=2
print("Dividir puntos (/=):", puntos)


#Ejercicio 10. Operadores de identidad
print("Ejercicio 10. Operador de identidad\n")

#Programa que compra objetos
print("=== ¿SON LA MISMA COSA? ===")
#Creamos dos listas que se ven iguales
lista1 = ["manzana", "pera"]
lista2 = ["manzana", "pera"]
lista3 = lista1 # lista3 es la MISMA que lista 1

#IS (es): Pregunta ¿Son el mismo objeto en la memoria?
print("lista1 es lista2? (is):", lista1 is lista2) #False (diferentes objetos)
print("listaq es lista3? (is):", lista1 is lista3) #Trues (mismo objeto)

# IS NOT (no es): Pregunta ¿ NO son el mismo objeto?
print("¿lista1 NO es lista2? (is not):", lista1 is not lista2) #True 