numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"El número {numero2} es mayor que {numero1}.")
else:
    print("Ambos números son iguales. {numero1} or {numero2}")
