# Algoritmo: Promedio
# Calcula el promedio de 4 materias y evalúa acceso a beca

# --- Entradas ---
matematicas = float(input("Ingrese la nota de matematicas: "))
castellano  = float(input("Ingrese la nota de castellano: "))
ingles      = float(input("Ingrese la nota de ingles: "))
sociales    = float(input("Ingrese la nota de sociales: "))

# --- Proceso ---
promedio = (matematicas + castellano + ingles + sociales) / 4

# --- Salida ---
print("El promedio es:", promedio)

if promedio > 4.5:
    print("Puedes acceder a la beca")
else:
    print("Aún no puedes acceder a la beca, intenta el otro semestre")