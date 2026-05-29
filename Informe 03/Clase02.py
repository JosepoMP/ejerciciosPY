# Pido un número hasta que sea múltiplo de 11

numero = int(input("Ingrese un número entero: "))

while numero % 11 != 0:
    print("El número no es múltiplo de 11, intente de nuevo")
    numero = int(input("Ingrese un número entero: "))

print("¡El número", numero, "sí es múltiplo de 11!")