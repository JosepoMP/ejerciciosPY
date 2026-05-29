# Sistema de acceso simple con bucle

# --- Usuario y contraseña por defecto ---
usuario = "admin"
contrasena = "12345"

while True:

    # --- Menú ---
    print("\n=== SISTEMA DE ACCESO ===")
    print("1. Cambiar nombre de usuario")
    print("2. Acceder")
    print("3. Agregar usuario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # --- Opción 1: Cambiar nombre de usuario ---
    if opcion == "1":
        nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ")
        usuario = nuevo_usuario
        print("✅ Nombre de usuario cambiado a:", usuario)

    # --- Opción 2: Acceder ---
    elif opcion == "2":
        usuario_ingresado = input("Ingrese su usuario: ")
        clave_ingresada = input("Ingrese su contraseña: ")

        if usuario_ingresado == usuario and clave_ingresada == contrasena:
            print("✅ Bienvenido,", usuario)
        else:
            print("❌ Usuario o contraseña incorrectos, intente de nuevo")

    # --- Opción 3: Agregar usuario ---
    elif opcion == "3":
        nuevo_usuario = input("Ingrese el nuevo usuario: ")
        nueva_clave = input("Ingrese la nueva contraseña: ")
        usuario = nuevo_usuario
        contrasena = nueva_clave
        print("✅ Usuario agregado:", usuario)

    # --- Opción 4: Salir ---
    elif opcion == "4":
        print("👋 Hasta luego!")
        break

    # --- Opción inválida ---
    else:
        print("❌ Opción no válida, intente de nuevo")