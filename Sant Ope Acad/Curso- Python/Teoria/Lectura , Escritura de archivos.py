#### Lectura y escritura de archivos ####

#Lectura de archivos - Sirve para leer el contenido de un archivo 
archivo = open("datos.txt", "r") # Suponiendo que tenemos este archivo previamente creado  La R significa Read(Modo Lectura)
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura de archivos - Escribir datos en un archivo, lo abrimos en modo escritura ("w")
archivo = open("datos.txt" , "w")
archivo.write("Hola Mundo")
archivo.close()

# Puedes escribir en los archivos con la apertura y cierre de archivos de manera automatica de los siguientes comandos 

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

