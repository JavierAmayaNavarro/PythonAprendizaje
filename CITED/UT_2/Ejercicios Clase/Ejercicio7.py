lluvia = bool(input("¿Está lloviendo? (True/False): "))
tareas = bool(input("¿Has terminado tus tareas? (True/False): "))
biblioteca = bool(input("¿Vas a la biblioteca? (True/False): "))

if (not lluvia and tareas) or biblioteca:  #Si no llueve y has terminado tus tareas, o si vas a la biblioteca   #Se puede simplificar a: if (not lluvia and tareas) or biblioteca
    print("Puedes salir a la calle.")
else:
    print("No puedes salir a la calle.") #Si está lloviendo y no has terminado tus tareas, y no vas a la biblioteca