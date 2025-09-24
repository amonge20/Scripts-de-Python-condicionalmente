# Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
# potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)

# Preguntamos al usuario sobre el numero más la potencia que quiere elevar
Numero_pedido = int(input("Introduce un numero: "))
Numero_Elevado = int(input("Introduce el numero elevado: "))

# Calculamos el numero pedido más la potencia que ha pedido el usuario
Operacion_Elevada = Numero_pedido ** Numero_Elevado

# Si el numero elevado al dividirlo termina en 0, 2, 4, 6 y 8 entonces es par
if Operacion_Elevada % 2 == 0:
    print("El numero es par")
# Por el caso contrario seria impar
else:
    print("El numero es impar")