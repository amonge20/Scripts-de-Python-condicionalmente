# Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
# Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
# de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
# ¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
# introduce en mayúsculas? ¿Y si sin querer pone in punto en mitad de su nombre (p.e. nao.mi)?¿Y
# si se le cuela una almohadilla (p.e se#rgio)?

# Variable para al usuario
Nombre_Usuario = input("Escribe tu nombre de usuario: ")

# Validacion del usuario
if Nombre_Usuario == "alejandro":
    print("Bienvenido",Nombre_Usuario.title())
elif Nombre_Usuario == "naomi":
    print("Bienvenido",Nombre_Usuario.title())
elif Nombre_Usuario == "sergio":
    print("Bienvenido",Nombre_Usuario.title())
elif Nombre_Usuario == "invitado":
    print("Bienvenido",Nombre_Usuario.title())
else:
    print("Bienvenido",Nombre_Usuario.title())