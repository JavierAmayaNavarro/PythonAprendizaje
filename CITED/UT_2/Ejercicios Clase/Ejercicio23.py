# Muestra los primeros 20 numeros de la sucesión de Fibonacci.

a, b = 0, 1   # Inicializamos los dos primeros números de Fibonacci
c = 0         # Variable auxiliar para la suma

for i in range(20):   # Queremos los primeros 20 números
    print(a)          # Imprimimos el número actual
    c = a + b         # Calculamos el siguiente número de la sucesión
    a = b             # Actualizamos 'a' al siguiente número
    b = c             # Actualizamos 'b' al siguiente número
