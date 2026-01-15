# Diseñar un programa que muestre, para cada nº introducido por teclado, si es par, si es positivo y su cuadrado. El proceso de repetira hasta que el usuario introduzca un 0..
numero = int(input("Introduce un número para ver si es par, positivo y su cuadrado (0 para salir): "))

while numero != 0 :
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    if numero > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
        print("El cuadrado del numero es:", numero**2)
    numero = int(input("Introduce otro número (0 para salir): "))
print("Has salido.")
