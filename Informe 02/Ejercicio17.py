# Pídale al usuario por pantalla la temperatura. 
# Si la temperatura es mayor a 27 imprima el mensaje “Comprar helado”. 
# De lo contrario, si la temperatura es menor a 15 grados imprima “Comprar chocolate”. 
# De lo contrario, imprima “Comprar jugo de naranja”.
# Al final siempre imprima “Fin programa”.

# --- Entrada ---
temperatura = float(input("Ingrese la temperatura: "))

# --- Proceso y Salida ---
if (temperatura > 27):
    print("Comprar helado")
elif (temperatura < 15):
    print("Comprar chocolate")
else:
    print("Comprar jugo de naranja")

print("Fin programa")