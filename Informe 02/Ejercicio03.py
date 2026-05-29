
# Ejercicio03. Solicitar un numero al usuario e imprimir segun el caso:
# "En numero ingresado es par"
# si el numero es par, revisar e imprimir:
# "El numero tambien es mulriplo de 3"
# "El numero es par pero no es multiplo de 3"

Num = int(input("Por favor ingresa un numero: "))

if(Num%2 == 0):
    print("Es par")
    if(Num%3 == 0):
        print("Es multiplo de 3")
