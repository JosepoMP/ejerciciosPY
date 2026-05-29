# Ejercicio1. Solicitar dos numeros e imprimir si el segundo es mayor que el primero.
# Si se cumple lo anterior, imprimir si el segundo es mayor que dos veces el primero.

a = int(input("digite el valor de a: "))
b = int(input("digite el valor de b: "))

if (b>a):
    print("El segundo valor ingresado es mayor que el primero.")
    if (b>=a*2):
        print("El segundo valor contiene al primero dos o mas veces")
        