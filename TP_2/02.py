# Ingresar el precio de dos productos y decir cuál conviene más o si cuestan lo mismo

producto_1 = int(input("Ingrese el precio del primer producto: "))
producto_2 = int(input("Ingrese el precio del segundo producto: "))

if producto_1 < producto_2:
    print("El Primer producto cuesta menos")
elif producto_1 > producto_2:
    print("El segundo producto cuesta menos")
else:
    print("Los dos productos cuestan lo mismo")