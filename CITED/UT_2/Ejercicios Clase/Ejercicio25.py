suma = 0
num_trabajadores = 0
mayores = 0

print("Introduce las edades de los trabajadores (número negativo para terminar):")

while True:
    edad = int(input(f"Edad del trabajador {num_trabajadores + 1}: "))
    
    if edad < 0:
        break  # Sale si se introduce un número negativo
    
    suma += edad
    num_trabajadores += 1
    
    if edad >= 60:
        mayores += 1

if num_trabajadores > 0:
    media = suma / num_trabajadores
    print("\n--- RESULTADOS ---")
    print("Suma de las edades:", suma)
    print("Media de las edades:", media)
    print("Número de trabajadores:", num_trabajadores)
    print("Mayores de 60 años:", mayores)
else:
    print("No se introdujeron edades válidas.")