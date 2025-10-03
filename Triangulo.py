# En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
# piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
# este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
# con esas piezas.
# (Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
# todas las posibles combinaciones)

# Pedimos al usuario las longitudes de los lados del triangulos
Triangulo_lado1 = int(input("Introduce el primer lado del triangulo: "))
Triangulo_lado2 = int(input("Introduce el segundo lado del triangulo: "))
Triangulo_lado3 = int(input("Introduce el tercer lado del triangulo: "))

# Condicion de que si los 2 lados suman y es mayor que el tercer lado, entonces se puede hacer un triangulo
if (Triangulo_lado1 + Triangulo_lado2 > Triangulo_lado3) and (Triangulo_lado1 + Triangulo_lado3 > Triangulo_lado2) and (Triangulo_lado2 + Triangulo_lado3 > Triangulo_lado1):
    print("Se puede construir un triangulo con las piezas que tenemos")
else:
    print("No se puede construir un triangulo con las piezas que tenemos")