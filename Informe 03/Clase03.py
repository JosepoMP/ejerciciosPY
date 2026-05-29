num = int(input("Ingrese numero entero: "))

while num != 0:
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} NO es par")
    num = int(input("Ingrese número entero: "))