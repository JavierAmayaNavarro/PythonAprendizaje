# Función para sumar dos números y procedimiento para mostrar el resultado.

# Función para sumar dos números
def sumar(a: float, b: float) -> float:
    return a + b

# Procedimiento para mostrar el resultado
def mostrar_resultado_suma(n1: float, n2: float) -> None:
    print("Resultado:", sumar(n1, n2))

# Entrada de datos
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

# Llamada al procedimiento
mostrar_resultado_suma(n1, n2)

