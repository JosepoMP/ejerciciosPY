# Realice el codigo del siguiente enunciado.
# Pídale al usuario por pantalla su género de música favorito.
# Si el género es “Electronica” o “Pop”:
# Pídale por pantalla por el año en que nació. Si el año es mayor a 2000 y el género es “Pop” imprima “Tengo la camisa negra”. De lo contrario, imprima “Por siempre Daft punk”.
# De lo contrario, imprima por pantalla “Los únicos géneros buenos son Electronica y Pop”.
# Al final siempre imprima “Fin programa”.

# --- Entrada ---
genero = input("Ingrese genero: ")

if (genero == "Electronica" or genero == "Pop"):
    año = int(input("Ingrese su año de nacimiento: "))
    if (año > 2000 and genero == "Pop"):
        print("Tengo la camisa negra")
    else:
        print("Por siempre Daft punk")
else: 
    print("Los unicos generos buenos son Electeonica y Pop")

print("Fin programa")