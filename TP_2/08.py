# Ingresar las calorías de un alimento y mostrar:

""" Menor a 100: Ligero
    Entre 100 y 300: Moderado
    Más de 300: Calórico """

calorias = int(input("Ingrese las calorías: "))

if calorias < 100:
    print("Ligero")
elif calorias >= 100 and calorias <= 300:
    print("Moderado")
else:
    print("Calórico")