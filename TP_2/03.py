# Ingresar el valor del índice de calidad del aire (ICA) y clasificar


""" Menor a 50: Bueno
    Entre 50 y 100: Moderado
    Mayor a 100: Peligroso """

ICA = int(input("Ingresar el Índice de Calidad del Aire (ICA): "))

if ICA < 50:
    print("Bueno")
elif (ICA >= 50) and (ICA <= 100):
    print("Moderado")
else:
    print("Peligroso")