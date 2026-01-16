#### Variables ####
# Enteros (int)
edad=25
cantidad=25

#Flotantes (Float)
precio= 9.99
altura=1.75

#Cadenas de texto (Strings)

nombre = "Juan"
mensaje = 'Hola , Mundo'

#Booleanos (Bool)

es_mayor_de_edad = True
tiene_descuento = False

#### Operadores ####

#Aritmeticos 
a=10
b=3

suma = a+b # 13
resta = a-b # 7
multiplicacion = a*b #30
division = a/b #3.3333
division_entera = a//b #3
modulo = a%b #1
potencia = a**b #1000

#Comparacion
a=10
b=3

igual = (a == b) #False
diferente = (a != b) #True
mayor_que = (a > b) #True
menor_que = (a < b) #False
mayor_o_igual = (a >= b) #True
menor_o_igual = (a <= b) #False

#Logicos
a=10
b=3
resuktado_and = (a > 5 and b < 5) #True
resultado_or = (a > 5 or b > 5) #True
resultado_not = not(a > 5) #False

#### Estructuras condicionales ####
# If
edad = 20
if edad >= 18:
    print("Eres mayor de edad")

# If-Else
edad = 15
if edad >= 18:
    print("Eres mayor de edad") 
else:
    print("Eres menor de edad")

# If-Elif-Else
calificacion=85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Notable")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesita mejorar")

####  Bucles ####
# For
frutas = ["manzana", "banana", "naranja"]
for frutas in frutas:
    print(frutas)

# While
contador = 0 
while contador <5:
    print (contador)
    contador +=1 # Suma 1 al contador en cada iteracion

#Control de Bucles
# Break se utiliza para salir de un bucle independentemente de si la condicion del bucle es verdadera
contador = 0
while True:
    print(contador)
    contador +=1
    if contador ==5:
        break

# Continue se utiliza para saltar a la siguiente iteracion del bucle
for i in range(10):
    if i % 2 ==0:
        continue
    print(i)  # Imprime solo numeros impares

#Pass Operacion nula que no hace nada, se utiliza como un marcador de posicion
for i in range(5):
    pass  # No hace nada

#### Estructuras de datos ####
# Listas # 
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # manzana
print(frutas[1])  # banana
print(frutas[2])  # naranja

print(frutas[-1])  # naranja
print(frutas[-2])  # banana
print(frutas[-3])  # manzana

 #-- - Agregar, eliminar y modificar elementos en una lista - --

frutas.append("pera")  # Agrega "pera" al final de la lista
frutas.remove("banana")  # Elimina "banana" de la lista
frutas.insert(1, "kiwi")  # Inserta "kiwi" en la posicion 1
frutas.pop()  # Elimina y devuelve el ultimo elemento de la lista
frutas.sort()  # Ordena la lista en orden alfabetico
frutas.reverse()  # Invierte el orden de la lista
print(len(frutas))  # Imprime la longitud de la lista

    # Lista de compresion forma concisa de crear listas basadas en secuencias existentes

numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]  # [1, 4, 9, 16, 25]
print(cuadrados) # Imprime 4, 16 

# Tuplas # 

#Creacion y Acceso

punto = (3,4)
print(punto[0]) #Imprime el 3
print(punto[1])# Imprime el 4

# Método de tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)
print(mi_tupla.index(2))        # Salida: 1 ya que busca el primer numero 2 que encuentre en la tupla
print(mi_tupla.index(2, 2))     # Salida: 3 Busca el numero 2 empezando por la posicion 2
print(mi_tupla.index(2, 2, 4))  # Salida: 3 Busca el numero empezando por el indice 2 y terminando antes del indice 4
print(mi_tupla.count(2))        # Salida: 3 Cuantas veces aparece el mismo numero 2
print(len(mi_tupla))            # Salida: 6 Cuantos elementos tiene la tupla

    # Diccionarios #
# Creacion y Acceso

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

#Metodos de diccionarios

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

    #Conjuntos (set)
#Creacion y operaciones basicas
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

# Metodo de conjuntos
frutas = {"manzana", "banana", "naranja"}
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}
frutas.clear()
print(frutas)  # Imprime set()

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