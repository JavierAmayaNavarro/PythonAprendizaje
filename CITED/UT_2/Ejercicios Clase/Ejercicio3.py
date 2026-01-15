numero1= int(input("Ingrese el primer número entero: "))
numero2= int(input("Ingrese el segundo número entero: "))

if numero1 > numero2:
    print("El primer número", numero1, "es mayor que el segundo número", numero2)
elif numero1 < numero2:
    print("El segundo número", numero2, "es mayor que el primer número", numero1)
else:
    print("Ambos números son iguales:", numero1 or numero2)
