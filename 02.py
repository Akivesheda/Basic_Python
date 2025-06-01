# Pedir al usuario que ingrese la velocidad de su vehículo

vel = int(input("ingrese la velocidad en KM/H: "))

if (vel <= 60):
    print("Permitido")

elif (vel >= 61) and (vel <= 80):
    print("Exceso leve")

else:
    print("Exceso grave")