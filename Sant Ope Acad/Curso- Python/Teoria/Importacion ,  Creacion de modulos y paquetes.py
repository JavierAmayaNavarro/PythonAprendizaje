#### Importacion y Creacion de Modulos ####

#Importar modulo completo
import math

resultado = math.sqrt(25)
print(resultado) #Imrpime 5.0

#Importar una parte del modulo

from math import sqrt

resultado = sqrt(25)
print (resultado)

# Funciones y clases de modulos estandar
# Math - Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.
# Random - Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.
# Datetime - Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

## Crear y utilizar modulos personalizados
#mi_modulo.py  -- Este es un archivo aparte 
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b

#Importamos mi modulo al documento main por ejemplo

import mi_modulo


mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

## - Organizacion del codigo en modulos - ##
# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")

import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

#Crear y utilizar paquetes - Para ello , tenemos que crear un directorio y agregar un archivo llamado __init.py dentro del directorio para que se inicialice el paquete
#Suponiendo la siguiente estructura , 
#- mi_paquete/
#    __init__.py
#    modulo1.py
#    modulo2.py
#Luego en el archvo main lo que tenemos que hacer es importar los modulos de la siguiente manera
from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()