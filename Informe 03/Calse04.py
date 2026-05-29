# Programa que imprime las primeras N potencias de 2 y su promedio

N = int(input("¿Cuántas potencias de 2 desea calcular? "))

suma = 0
contador = 1

while contador <= N:
    potencia = 2 ** contador
    print("2 elevado a", contador, "=", potencia)
    suma = suma + potencia
    contador = contador + 1

promedio = suma / N
print("La suma total es:", suma)
print("El promedio de las", N, "potencias es:", promedio)