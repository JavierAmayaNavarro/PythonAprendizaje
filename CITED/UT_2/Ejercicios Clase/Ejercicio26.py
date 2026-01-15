# Ejercicio de bucle perfecto

# Pedir al usuario que introduzca un número
numero = int(input("Introduce un numero: "))

sumadivisores = 0

# Calcular la suma de los divisores propios
for i in range(1, numero):
    if numero % i == 0:
        sumadivisores += i

# Comprobar si el número es perfecto
if numero == sumadivisores:
    print(f"{numero} es un numero perfecto")
else:
    print("El numero no es perfecto")
