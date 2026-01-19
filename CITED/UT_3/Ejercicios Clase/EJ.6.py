#6 Suma de números primos
#a. Crear un método que verifique si un número es primo.
# b. Otro método que sume todos los números primos entre 1 y N.

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def suma_primos_hasta(n: int) -> int:
    return sum(x for x in range(2, n + 1) if es_primo(x))

numero = int(input("Introduce un numero: "))

print(suma_primos_hasta(numero))