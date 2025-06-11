# Ingresar un color como texto (por ejemplo: "rojo", "verde", "azul") y decir qué estado representa

estado = str(input("Rojo, Verde o Azul: "))

if estado == "rojo" or "Rojo" or "ROJO":
    print("Ocupado")
elif estado == "verde" or "Verde" or "VERDE":
    print("Disponible")
elif estado == "azul" or "Azul" or "AZUL":
    print("En descanso")
else:
    print("error")