# Ingresar un valor de saldo y luego pedir que se ingrese un monto a retirar

saldo = int(input("Ingrese su saldo en Pesos: $"))

retiro = int(input("Ingrese monto a retirar: $"))

if saldo > retiro:
    print("Saldo restante:", (saldo - retiro))

else:
    print("Fondos insuficientes")