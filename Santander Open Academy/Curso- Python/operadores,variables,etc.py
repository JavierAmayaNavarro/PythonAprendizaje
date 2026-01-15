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

#Estructuras condicionales
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

#Bucles
# For
frutas = ["manzana", "banana", "naranja"]
for frutas in frutas:
    print(frutas)

# While
contador = 0 
while contador <5:
    print (contador)
    contador +=1 # Suma 1 al contador en cada iteracion