# Ingresar la temperatura de una bebida y clasificar

""" Menor a 5°C: Fría
    Entre 5°C y 20°C: Templada
    Mayor a 20°C: Caliente """

temperatura = int(input("Ingrese la temperatura en °C: "))

if temperatura < 5:
    print("Bebida fría")
elif temperatura >= 5 and temperatura <= 20:
    print("Bebida tempada")
else:
    print("Bebida caliente")

