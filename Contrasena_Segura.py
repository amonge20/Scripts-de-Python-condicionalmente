# Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
# especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
# comprueba si es una contraseña segura e indícalo por pantalla.

# Variable para las vocales minuscula en un array
vocales = ['a','e','i','o','u']
Caracteres_Especiales = ['*','#']

# El usuario introducira la contraseña
Usuario_Contrasena = input("Introduce tu contraseña: ")

# Bucle para contar si hay vocales o no
tiene_vocal = False
simbolos_encontrados = set()

for caracter in Usuario_Contrasena:
    if caracter in vocales:
        tiene_vocal = True
    if caracter in Caracteres_Especiales:
        simbolos_encontrados.add(caracter)

# Si la contraseña que introduce el usuario, tiene lo que se le pide. Se sabra si es una contraseña segura o insegura
if tiene_vocal and len(simbolos_encontrados) >= 2:
    print("Es una contraseña segura")
else:
    print("Es una contraseña insegura")