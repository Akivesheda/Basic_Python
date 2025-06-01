# Ingresar un número del 1 al 7 representando un día de la semana

print("1 = Lunes")
print("2 = Martes")
print("3 = Miércoles")
print("4 = Jueves")
print("5 = Viernes")
print("6 = Sábado")
print("7 = Domingo")
dia_sem = int(input("ingrese un número (1-7): "))

if dia_sem >= 1  and dia_sem<= 5:
    print("Día laboral")

elif dia_sem == 6 or dia_sem == 7:
    print("Fin de semana")

else:
    print("error")