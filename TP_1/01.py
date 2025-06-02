# Ingresar la edad de una persona y mostrar en qué categoría está

edad = int(input("ingrese la edad: "))

if (edad < 18):
    print("Menor de edad")

elif (edad >= 18) and (edad <= 64):
    print("Adulto")

else:
    print("Adulto mayor")