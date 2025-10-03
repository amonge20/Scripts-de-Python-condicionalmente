# Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
# financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
# producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
# entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
# estrictamente por encima de 150 el bot deberá imprimir la orden de vender

# El usuario pedira datos al Bot trading, como por ejemplo el precio
precio = int(input("Introduce cantidad de dinero: "))

# Condicion de que si el usuario introduce una cantidad menor de 100 dolares. El bot trading imprimira por pantalla "la orden de comprar"
if precio < 100:
    print("Orden de comprar")
# Pero si esta entre 100 y 150 dolares (ambos incluidos), el bot imprimira la orden de hold
elif 100 <= precio <= 150:
    print("Orden de hold")
# Pero si el precio esta por encima de 150 dolares, el bot imprimira la orden de vender
elif precio > 150:
    print("Orden de vender")