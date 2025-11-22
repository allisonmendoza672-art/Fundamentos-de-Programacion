print("Ejercicio 1\n")

canciones_dia = ("Blindings Lights", "Heat Waves", "Anti-Hero")
canciones_noche = ("Levitating", "As it was")

playlist_completa = canciones_dia + canciones_noche
print(canciones_dia)
print(canciones_noche)
print(playlist_completa)

print("\nEjercicio 2\n")
ubicaciones_norte = ((19.5, -99.2), (19.6, -99.3))
ubicaciones_sur = ((19.4, -99.1), (19.3, -99.4))

todas_ubicaciones = ubicaciones_norte + ubicaciones_sur
print(ubicaciones_norte)
print(ubicaciones_sur)
print(todas_ubicaciones, "\n")

print("\nEjercicio 3 - Repetición\n")

emojis = ("💚", "🦋")
cartel = emojis * 5
print(emojis)
print(cartel, "\n")

print("\Ejercicio 4 - Longitud\n")

seguidores_tiktok = 1500
seguidores_insta = 2300
seguidores_fb = 950
seguidores_total = seguidores_tiktok + seguidores_insta + seguidores_fb
seguidores = (seguidores_tiktok, seguidores_insta, seguidores_fb)
cantidad_redes = len(seguidores)

print("seguidores en TikTok:", seguidores_tiktok)
print("seguidorrs en instagram:", seguidores_insta)
print("seguidores en Facebook:", seguidores_fb)
print("Total seguidores:", seguidores_total)
print("Cantidad de redes sociales:", cantidad_redes)

print("\nEjercicio 5 - vount\n")

resultados_partidas = ("gané", "perdí", "gané", "gané", "perdí", "gané", "empate")
veces_gane = resultados_partidas.count("gané")
print("He ganado:", veces_gane)

print("\nEjercicio 6 - index")

ranking = ("Marcelo", "Mariana", "Vane", "Abi", "Fer", "Marcelo", "orlando")
mi_posicion = ranking.index("Mariana")
print("Estoy en la posición: ", mi_posicion, "\n")

print("\nEjercicio 7 - slicing\n")

juegos = ("Minecraft", "Fortnite", "Roblox", "Among us", "Valorant", "GIA V", "ACNH", "Call of duty")
ultimos_tres = juegos[2:5]
print(ultimos_tres)

print("\nEjercicio 8 - recorrer tupla\n")

canciones = ("EYES CLOSED", "The Fate Of Ophelia", "When did you get hot", "Golden")

for cancion in canciones:
    print(cancion)
    
print("\nEjercio 9 - verificae si un elemento existe\n")

grupo_proyecto = ("Meli", "Alex", "Mia", "Andrea")

print("integrantes del equipo", grupo_proyecto)
print("\n¿Mia está en el grupo?")
print("Mia" in grupo_proyecto)

print("\n¿Orlando está en el grupo?")
print("Orlando" in grupo_proyecto)

print("\nEjercicio 10 - Ordenar la tupla\n")

puntuaciones = (580, 250, 1040, 390, 750, 2480, 870, 138, 938)
puntuaciones_ordenadas = tuple(sorted(puntuaciones))
print(puntuaciones_ordenadas)


