# Generar un pograma que valide si a un partido politico pasó el umbral para asignarle curules.
# El programa pedirá al usuario por pantalla la cantidad de votos válidos (int).
# El programa pedirá al usuario por pantalla la cantidad de votos de su partido (int).
#  El programa validará que la cantidad de votos de su partido es mayor al 3% de los votos válidos.
# Si se cumple lo anterior el programa imprimirá “Tu partido tendrá curules”.
# En caso contrario, imprimirá “Se quemaron”.

# --- Entradas ---
votosValidos = int(input("Ingrese votos válidos: "))
votosPartido = int(input("Ingrese votos por su partido:"))

umbral = votosValidos * 0.03

# --- Proceso y Salida ---

if (votosPartido > umbral):
    print("Tu partido tendrá curules")
else:
    print("Se quemaron")