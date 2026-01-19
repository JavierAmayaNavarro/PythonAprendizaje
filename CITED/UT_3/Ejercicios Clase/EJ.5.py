#Procedimiento que imprima una tabla de multiplicar.

def tabla_multiplicar(n: int, hasta: int = 10) -> None : 
    for i in range(1, hasta + 1):
        print (f"{n} x {i} = {n * i}")


numero = int(input("Introduce un numero: "))
print(tabla_multiplicar(numero))