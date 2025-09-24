# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
# divisor es cero el programa debe mostrar un error.

# Preguntamos al usuario sobre que 2 numeros quiere que se divida
Numero_1 = int(input("Introduce el primer numero: "))
Numero_2 = int(input("Introduce el segundo numero: "))

# Con la operacion de la division, si el numero que se divide da 0, el programa nos saltara error
if Numero_2 != 0:
    Operacion_Division = Numero_1 / Numero_2
    print(Operacion_Division)
else:
    print("Error de calculo")