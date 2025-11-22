print("Ejercicios diccionarios - martes \n")
print("\nEjercicio 1\n")
#Escribe tus datos
usuario = {
    "nombre": "Yamileth",
    "edad" : 18,
    "ciudad" : "Monterrey"
}
print("Diccionario completo:")
print(usuario)
print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Ciudad:", usuario["ciudad"])


print("\nEjercicio 2\n")
videojuego = {
    "título": "Minecraft", 
    "plataforma": "PC"
}

print("Diccionario original:")
print(videojuego)
# Agregar nuevos datos
videojuego["año"] = 2011
videojuego["genero"]= "Sandbox"
videojuego["es_multijugador"] = True

print("\nDiccionario después de agregar datos:")
print(videojuego)
print("\nNuevos datos agregados:")
print("Año:", videojuego["año"])
print("Genénero", videojuego["genéro"])
print("¿Es multiplicador?:", videojuego["es_multiplicador"])

print("\nEjercicio 3\n")
#Agregar tus datos
perfil = {
    "usuario": "Tu nombre",
    "seguidores": 500,
    "publicaciones": 25,
    "ciudad": "Tu ciudad"
}

print("Perfil original:")
print(perfil)
print("Seguidores antes:", perfil["seguidores"])

#Modificar valores (gana más seguidores)
perfil["seguidores"] = 1250
perfil["publicaciones"] = 45

print("\nPerfil actualizado:")
print(perfil)
print("seguidores ahora::", perfil["seguidores"])
print("Publicaciones ahora:", perfil["publicaciones"])


print("\nEjercicio 4 - eliminar un par clave-valor\n")
#Escribe tus datos
cuenta = {
    "usuario": "pon tu usuario",
    "email": "agrega emial",
    "teléfono": "escribe tu numero",
    "ciudad": "pon tu cd"
}

print("Cuneta original (con teléfono):")
print(cuenta)
# Eliminae el número de teléfono por privacidad
del cuenta["teléfono"]

print("\nCuenta depués de eliminar teléfono:")
print(cuenta)
print("\nVerificarción - ¿existe 'telefono'?:", "teléfono" in cuenta)


print("\nEjercicio 5 - len\n")
# Agregae vuestra propia peli
película = {
    "título": "Avatar",
    "director": "James Cameron",
    "año": 2009,
    "genero": "Ciencia Ficción",
    "duración_minutos": 162,
    "calificación": 8.0
}

print("Película:")
print(película)
cantidad = len(película)
print("\n¿Cuántos datos tiene el diccionario?:", cantidad)
print("El diccionario tiene", cantidad, "pares clave-valor")


print("\nEjercicio 6 - obtener las keys\n")
# Agregae vuestra cancion fav
canción = {
    "titulo": "deja vu",
    "artista": "olivia rodrigo",
    "album": "GUTS",
    "año": 2023,
    "género": "Pop Rock",
    "duración_segundos": 300
}

print("Diccionario de canción:")
print(canción)
print("\nTodas las claves del diccionario:")
claves = canción.keys()
print(claves)

print("\nMostrando claves una por una:")
for clave in claves:
    print("-", clave)


print("\nEjercicio 7: ontener los values")
calificaciones = {
    "Economia" 8.5,
    "Derecho de aduanas": 9.0,
    "Admin de negocios": 8.0
    "Logistica y cadena de suministros": 7.5,
    "Mercadotecnia Internacional": 9.5
}

print("Diccionario de calificaciones:")
print(calificaciones)
print("?nTodos los valores del diccionario:")
valores = calificaciones.values()
print(valores)

print("\nMostrando valores uno por uno:")
for valor in valores:
    print("-", valor)
print("\nPromedio de calificaciones:",sum(valores) / len(valores))