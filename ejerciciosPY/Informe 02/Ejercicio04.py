# Ejercicio04. Solicitar el nombre y la edad de una persona. imprimir en
# Consola un mensaje personalizado que diga si la persona puede votar en las proximas
# Elecciones (con la fecha de las votaciones)

fecha_elecciones = "26 de octubre de 2025"

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("✅ Hola", nombre + ", puedes votar en las próximas elecciones del", fecha_elecciones)
else:
    falta = 18 - edad
    print("❌ Hola", nombre + ", aún no puedes votar.")
    print("   Te faltan", falta, "años para poder hacerlo.")