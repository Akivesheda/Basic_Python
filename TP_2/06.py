# Ingresar el porcentaje de batería de un celular:

carga = int(input())

if carga == 100:
    print("Carga completa")
elif carga <= 99 and carga >= 20:
    print("Carga adecueda")
else:
    print("Carga baja")