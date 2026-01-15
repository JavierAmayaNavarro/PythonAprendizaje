dia = str(input("Introduce un dia de la semana:"))

match dia: # Esto es un switch
    case "Lunes":
        print("Hoy es Lunes ")
    case "Martes":
        print("Hoy es Martes ")
    case "Miercoles":
        print("Hoy es Miercoles ")
    case "Jueves":
        print("Hoy es Jueves ")
    case "Viernes":
        print("Hoy es Viernes ")
    case "Sabado":
        print("Hoy es Sabado ")
    case "Domingo":
        print("Hoy es Domingo ")
    case _:
        print("Dia no valido")
        
