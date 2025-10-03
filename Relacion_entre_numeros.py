# Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
# de los otros dos

# Pedimos al usuario 3 numeros
print("--- Introduce 3 numeros ---")

# Introducimos los 3 numeros
a = int(input("Introduce el numero A: "))
b = int(input("Introduce el numero B: "))
c = int(input("Introduce el numero C: "))

# Verificamos si alguno es la suma de los otros 2
if a == b + c:
    print(f"El primer número ({a}) es la suma de los otros 2 ({b} + {c})")
elif b == a + c:
    print(f"El primer número ({b}) es la suma de los otros 2 ({a} + {c})")
elif c == a + b:
    print(f"El primer número ({c}) es la suma de los otros 2 ({a} + {b})")
else:
    print("Ninguno de los numeros es la suma de los otros 2")