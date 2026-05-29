# Proceso: ejemplo_CP
# Calcula la tabla de multiplicar de un número N

N = int(input("Ingrese número entero N: "))

resultado = 0

for vc in range(1, 11):
    resultado = vc * N
    print("N x", vc, "=", resultado)