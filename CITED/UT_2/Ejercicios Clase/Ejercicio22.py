# Pide numeros hasta que el usuario introduzca un 0 y muestra la suma de todos los numeros introducidos

suma = 0 
while True:
    numero = int(input("Introduzca un numero (0 para terminar): "))
    if numero == 0 :
        break
    suma +=numero
print("La suma de los numeros introducidos es:", suma)

