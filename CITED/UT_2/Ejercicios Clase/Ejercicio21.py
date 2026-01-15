# Pida un numero y calcula su factorial

print("Introduzca un numero para calcular su factorial: ")
numero = int(input())
factorial = 1
for i in range(1, numero + 1):
    factorial = factorial * i
print("El factorial de", numero, "es", factorial)
