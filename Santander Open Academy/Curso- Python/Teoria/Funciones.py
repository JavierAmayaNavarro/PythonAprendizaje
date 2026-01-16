#### Funciones ####

# Definicion y llamada de funciones
def saludo():
    print("Hola Mundo")

saludo() # Aqui imprime Hola Mundo

#Parametros y argumentos
def saludo(nombre):
    print(f"Hola, {nombre}")

saludo("Juan") # Imprime Hola, Juan

# Valores de entorno
def suma(a, b):
    return a+b
resultado = suma(3,4)
print(resultado) #Imprime 7

#Funciones anonimas (lambda)
cuadrado = lambda x: x**2
print(cuadrado(5)) # Imprime 25

#Alcance de las variables (local vd global)
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.

#Funciones definidas por el usuario
import funcion_definidas_usuario # Revisar el siguiente archivo , darle a F12 desde el VSCode

#Documentacion de funciones (docstrings)
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura

# Funcion con numero variable de argumentos
def suma_variable(*numeros): # EL * hace que puedas meter una cualquier cantidad de numeros como si fuera una tupla
    total = 0 
    for numero in numeros:
        total += 0
    return numero
print(suma_variable(1,2,3)) # Imprime 6
print(suma_variable(4,5,6,7)) # Imprime 22