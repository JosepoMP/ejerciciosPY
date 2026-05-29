# Cree un programa que dependiendo del año en que naciste te diga a que generación perteneces:
# El programa pedirá al usuario por pantalla el año en que naciste (int).
# Si el año está entre 1994 y 2010 imprimirá “Eres Generación Z”.
# Si no, si el año está entre 1981 y 1993 imprimirá “Eres Milennial”.
# De lo contrario, imprimirá “Eres de otra generación”.

# --- Entrada ---
año = int(input("Ingrese año de nacimiento: "))

# --- Proceso y Salida ---
if (año >= 1994 and año <= 2010):
    print("Eres Generacion z")
elif ( año >= 1981 and año <= 1993):
    print("Eres Milennial")
else: 
    print("Eres de otra generacion")

