# Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
# Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
# indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
# contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
# Cambia el script para que no distinga entre mayúsculas y minúsculas.
# (Pista: Necesitarás in If Statement anidado)

# Introducimos usuario y contraseña que tiene que acceder el usuario
Usuario = "Usuario"
Contrasena = "usuario"

# Preguntamos por el usuario y contraseña
Usuario_Introducido = input("Introduce usuario: ")
Contrasena_Introducida = input("Introduce contraseña: ")

# Si el usuario accede de manera correcta a su cuenta, le concedera el acceso
if (Usuario_Introducido == Usuario) and (Contrasena_Introducida == Contrasena):
    print("Acceso concedido. Bienvenido",Usuario)
    
# En caso contrario se le pedira una segunda vez
elif (Usuario_Introducido != Usuario) or (Contrasena_Introducida != Contrasena):
    print("El usuario o la contraseña es incorrecta. Intentelo de nuevo")
    Usuario_Introducido = input("Introduce usuario: ")
    Contrasena_Introducida = input("Introduce contraseña: ")
    
    # Comprobamos por segunda vez las credenciales del usuario
    if (Usuario_Introducido == Usuario) and (Contrasena_Introducida == Contrasena):
        print("Acceso concedido. Bienvenido",Usuario)
    else:
        print("El usuario o la contraseña es incorrecta. Acceso bloqueado")