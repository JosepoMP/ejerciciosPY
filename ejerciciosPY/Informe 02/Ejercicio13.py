# Algoritmo: Ganancia por Inversión
# Calcula la ganancia mensual de un capital invertido con un interés del 2%

# --- Entradas ---
capital = int(input("Ingrese el monto a invertir: "))
dias    = int(input("Ingrese el número total de días del mes a considerar: "))

# --- Proceso ---
interes  = 0.02
ganancia = (capital * dias) * interes

# --- Salida ---
print("La ganancia por cobrar después del mes es de:", ganancia)