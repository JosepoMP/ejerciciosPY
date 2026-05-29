# Proceso: ejemplo_CM
# Imprime los números del 1 a N y su suma

N = int(input("Ingrese número entero N: "))

vc = 1
suma = 0

while vc <= N:
    print("Cuenta:", vc)
    suma = suma + vc
    vc = vc + 1

print("La suma de 1 hasta", N, "es:", suma)