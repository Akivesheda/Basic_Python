# Ingresar la temperatura corporal (en °C) y clasificarla

""" Menor a 36°C: Hipotermia
    Entre 36°C y 37.5°C: Normal
    Mayor a 37.5°C: Fiebre """

grados_c = float(input("Temperatura en °C: "))

if grados_c < 36:
    print("Hipotermia")
elif grados_c >= 36 and grados_c <= 37.5:
    print("Normal")
else:
    print("Fiebre")