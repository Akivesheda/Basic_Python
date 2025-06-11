# Ingresar el tipo de cliente (`A`, `B`, `C`) y aplicar un descuento

cliente = str(input())

if cliente == ("a") or cliente == ("A"):
    print("20% de descuento")
elif cliente == ("b") or cliente == ("B"):
    print("10% de descuento")
elif cliente == ("c") or cliente == ("C"):
    print("Sin descuento")
else:
    print("Error")