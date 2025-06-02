# Mostrar al usuario un menú con 4 opciones

print("1 = Hamburguesa")
print("2 = Pizza")
print("3 = Ensalada")
print("4 = Salir")
menu = int(input("Ingrese número (1-4): "))

if (menu == 1):
    print("Hamburguesa")

elif(menu == 2):
    print("Pizza")

elif(menu == 3):
    print("Ensalada")

elif(menu == 4):
    print("Salir")

else:
    print("Error")