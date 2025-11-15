
# Ejercicios 1-6

# Escribe tu función aquí 
def mostrar_perfil():
    print(" Usuario: @taylorswift")
    print(" Seguidores: 1.2b")
    print (" Bio: Cantante")

# Pruébala (llámala 2 veces)
mostrar_perfil()
print() # Línea en blanco para separar 
mostrar_perfil()


# Ejercicio 2

# Escribe tu función aquí 
def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales

# Pruébala con diferentes valores
horas = calcular_horas_tiktok(30) # 30 minutos por dia
print(f"Ves {horas} horas de TikTok a la semana")

horas2 = calcular_horas_tiktok(60) # 60 minutos por día
print(f"Ves {horas2} horas de TikTok a la semana")


# Ejercicio 3 
# Escribe tu función aquí
def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
        return "Sí puedes comprarlo"
    else:
        return "No te alcanza"

# Pruebala con diferentes casos
resultado1 = puedo_comprar(500, 300) #Tengo $500, cuesta $300
print(f"Tenis nuevos: {resultado1}")

resultado2 = puedo_comprar(150, 800) # Tengo $150, cuesta $800
print(f"Celular nuevo: {resultado2}")

resultado3 = puedo_comprar (100, 100) # Tengo $100, cuesta $100
print (f"Audífonos: {resultado3}")


# Ejercicio 4 
print("\nEjercicios 1")

def calcular_likes_totales(likes_foto1, likes_foto2, likes_foto3):
    total = likes_foto1 + likes_foto2 + likes_foto3 
    return total

total = calcular_likes_totales(150, 230, 89)
print (f"Tienes {total} likes en total ")

total2 = calcular_likes_totales(800, 420, 300)
print(f"Tienes {total2} lokes en total")


# Ejercicio 5

print("\nEjercicio 2\n")

def aplicar_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * porcentaje_descuento / 100
    precio_final = precio_original - descuento
    return precio_final

precio_final = aplicar_descuento(1000, 20) #1000 con 20% de descuento
print (f"Precio final: ${precio_final}")

precio_final2 = aplicar_descuento(500, 10) #$500 con 10% de descuento
print(f"Precio final: ${precio_final}")


# Ejercicio 6
print ("\nEjercicio 3\n")

def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio

promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio}")

promedio2 = calcular_promedio(100, 95, 88)
print (f"Tu promedio es: {promedio2}")