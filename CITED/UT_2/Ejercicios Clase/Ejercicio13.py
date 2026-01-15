import math

a = int(input("Introduce el coeficiente A:")) #Lo muestras justo al lado de la entrada

print("Introduce el coeficiente B") #Lo muestras abajo de la entrada
b = int(input())

print("Introduce el coeficiente C")
c = int(input())

discriminante = (b * b) - (4 * a * c)
divisor = 2 * a

if discriminante >= 0 and divisor != 0:
    sol1 = (-b + math.sqrt(discriminante)) / divisor
    sol2 = (-b - math.sqrt(discriminante)) / divisor

    print("Las soluciones son:")
    print("Primera solución:", sol1)
    print("Segunda solución:", sol2)
else:
    print("No se puede (no hay soluciones reales o A es 0)")