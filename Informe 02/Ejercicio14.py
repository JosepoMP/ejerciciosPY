# Algoritmo: NT_ARENA
# Calcula la cantidad de arena necesaria para una pared

# --- Valores fijos ---
metros = 0.5

# --- Entradas ---
largo = float(input("Teclea el largo de la pared: "))
ancho = float(input("Teclea el ancho de la pared: "))

# --- Proceso ---
arena = largo * ancho * metros

# --- Salida ---
print("La cantidad de arena es:", arena)