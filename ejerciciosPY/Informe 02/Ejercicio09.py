# Algoritmo: Cambio de Moneda
# Convierte soles a dólares o euros según el tipo de cambio

# --- Entrada --- 
nombre = input("Ingrese el nombre del cliente: ")
monto = float(input("Ingrese el monto en soles: "))
print("Seleccione moneda de cambio")
print("[1] Dolares  [2] Euros")
moneda = int(input())

# --- Proceso --- 
if moneda == 1:
    cambio = monto/ 2.35
    simbolo = "$"
else:
    cambio = monto / 3.58
    simbolo = "€"

# --- Salida ---
print(" Se cambio en:", simbolo, cambio)