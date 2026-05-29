cantidadFlores = int(input("Ingrese la cantidad de flores: "))

if cantidadFlores >= 10:
    precioTotal = cantidadFlores * 8
    print("Total a pagar: ", precioTotal)
elif cantidadFlores >= 5:
    precioTotal = cantidadFlores * 10
    print("Total a pagar: ", precioTotal)
elif cantidadFlores == 3:
    print("No debes pagar nada, las flores son gratis")
else:
    precioTotal = cantidadFlores * 15
    print("Total a pagar:", precioTotal)

print("Fin programa")