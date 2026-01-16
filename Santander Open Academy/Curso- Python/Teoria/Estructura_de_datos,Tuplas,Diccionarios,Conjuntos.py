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
