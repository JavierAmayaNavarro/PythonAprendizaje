#ENUNCIADO 3 – Comprobación de mayoría de edad
#Diseñar una aplicación que determine si una persona es mayor de edad.
#Se considerará mayor de edad cuando la edad sea igual o superior a 18 años.
#El resultado se almacenará en una variable booleana y se mostrará por pantalla.

edad = int(input("Introduce tu edad: "))

es_mayor = edad >= 18

if es_mayor:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
