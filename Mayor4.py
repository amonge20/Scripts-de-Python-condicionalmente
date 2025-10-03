# Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
# pantalla.

# Preguntamos al usuario mediante un bucle, 4 numeros y despues calcularemos el más mayor
numeros_pedidos = []

for i in range(4):
    numero = int(input("Introduce un numero: "))
    numeros_pedidos.append(numero)

numeroMayor = max(numeros_pedidos)
print("El numero mayor es:", numeroMayor)