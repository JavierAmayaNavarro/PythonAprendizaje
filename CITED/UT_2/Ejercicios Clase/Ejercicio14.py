print("Introduzca una nota entre 0 y 10:")
nota = float(input())

match nota: # Esto es un swtch
    case nota if 0 <= nota < 5:
        print("Insuficiente")
    case nota if 5 <= nota < 6:
        print("Suficiente")
    case nota if 6 <= nota < 7:
        print("Bien")
    case nota if 7 <= nota < 9:
        print("Notable")
    case nota if 9 <= nota <= 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida. Debe estar entre 0 y 10.")

