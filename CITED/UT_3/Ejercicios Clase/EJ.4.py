#Función para verificar si un número es par.

def es_par(n: int) -> bool:
    return n % 2 == 0

n1 = int(input("Introduce el número: "))

print(es_par(n1))