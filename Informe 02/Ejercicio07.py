# Algoritmo: Entrada Circo
# Calcula el precio final de la entrada según la edad del cliente

# --- Entradas --- 
p = float(input("Ingrese el precio de de la entrada: "))
edad = float(input("Ingrese la edad del cliente: "))

# --- Cálculo ---
if edad < 10: 
    p = p - (p * 0.25)

# --- Salidas ---
print("El monto final a pagar es:",p)