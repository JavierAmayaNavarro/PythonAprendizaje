# Pide un numero y muestra su tabla de multiplicar del 1 al 10

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1,11):
    resultado = numero * i
    print (numero, " x " , i , " = " , resultado)