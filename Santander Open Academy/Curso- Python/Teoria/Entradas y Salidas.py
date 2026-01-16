#### Entradas // Salidas ####
#Entradas de datos del usuario 
nombre = input("Introduce tu nombre")
edad = input("Introduce tu edad")

print("Hola, " + nombre + "!")
print ("Tienes " + edad + "años.")

# ------------------------------------------------------------------------- #

edad = int(input("Introduce tu edad: "))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Salidas de datos
nombre = "Juan"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")