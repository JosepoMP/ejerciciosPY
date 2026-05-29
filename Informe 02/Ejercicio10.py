# Proceso: Postulantes
# Categoriza postulantes según sexo y edad

# --- Entradas ---
sexo = input("Ingrese el sexo del postulante (Femenino/Masculino): ")
edad = int(input("Ingrese la edad del postulante: "))

# --- Proceso ---
if sexo == "Femenino":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
else:
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"

# --- Salida ---
print("La categoria del postulante es:", categoria)