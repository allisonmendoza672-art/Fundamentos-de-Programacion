edad = int(input("¿Cuál es tu edad?"))
genero = input("¿Cual es tu género favorito? (acción, comedia, terror). ").lower()

if edad < 13:
    print("Te recomendamos peliculas infatiles")

elif edad >=13 and edad <= 17 and genero == "acción":
    print("Te recomendamos: Spider-Man (PG-13)")

elif edad >=13 and edad <= 17 and genero == "comedia":
    print("Te recomendamos: Sherk (PG-13)")

elif edad >= 13 and edad <= 17 and genero == "terror":
    print("Te recomendamos: Scary Stories (Pg-13)")

elif edad >= 18 and genero == "acción":
    print("Te recomendamos: superbad")

elif edad >= 18  and genero == "comedia":
    print("Te recomendamos: Superbad")

elif edad >= 18 and genero == "terror":
    print("Te recomendamos: El conjuro")
    