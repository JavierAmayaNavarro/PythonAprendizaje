
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
