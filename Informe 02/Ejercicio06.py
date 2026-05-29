# Algoritmo: Bonificacion
# Calcula la bonificación y sueldo final de un trabajador según número de hijos

# --- Entradas ---
nombre = input("Ingrese el nombre del trabajador: ")
basico = float(input("Ingrese el sueldo basico: "))
hijos = int(input("Ingrese el numero de hijos: "))

# --- Cálculo ---
bonificacion = 0

if hijos > 0:
    bonificacion = basico * 0.07

final = basico + bonificacion

# --- Salidas ---
print("La bonificacion es:", bonificacion)
print("El sueldo final es:", final)