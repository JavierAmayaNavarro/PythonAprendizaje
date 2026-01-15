# -El alumnado deberá programar un sistema que simule el manejo de una cuenta bancaria sencilla mediante un menú interactivo.
# El programa permitirá:
# # -	Consultar el saldo: Mostrará el dinero que posee el usuario
# -	Ingresar dinero: Se añadirá al saldo
# -	Retirar dinero: Se quitará del saldo
# -	Ver el historial resumido de operaciones: Esta opción deberá ser capaz de mostrar estos mensajes.
# “Has hecho X ingresos por un total de X €”
# “Has hecho X retiradas por un total de X €”
# -	Ver historial de operaciones: Las tres últimas operaciones (sin usar listas)
# -	Salir del programa: Con opción de confirmar salida antes de salir


saldo = 0
totalingresos = 0
totalretiradas = 0
cantidadingresos = 0
cantidadretiradas = 0
ultimasoperaciones = ["", "", ""]

salir = False

while not salir:
    print("\nMenú de opciones:")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial resumido de operaciones")
    print("5. Ver historial de operaciones")
    print("6. Salir del programa")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion == "1":
        print(f"Saldo actual: {saldo} €")
    
    elif opcion == "2":
        ingreso = float(input("Ingrese la cantidad a depositar: "))
        saldo += ingreso
        totalingresos += ingreso
        cantidadingresos += 1
        ultimasoperaciones.pop(0)
        ultimasoperaciones.append(f"Ingreso: {ingreso} €")
        print(f"Has ingresado {ingreso} €. Nuevo saldo: {saldo} €")
    
    elif opcion == "3":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            totalretiradas += retiro
            cantidadretiradas += 1
            ultimasoperaciones.pop(0)
            ultimasoperaciones.append(f"Retiro: {retiro} €")
            print(f"Has retirado {retiro} €. Nuevo saldo: {saldo} €")
    
    elif opcion == "4":
        print(f"Has hecho {cantidadingresos} ingresos por un total de {totalingresos} €")
        print(f"Has hecho {cantidadretiradas} retiradas por un total de {totalretiradas} €")
    
    elif opcion == "5":
        print("Últimas tres operaciones:")
        for operacion in ultimasoperaciones:
            if operacion:
                print(operacion)
    
    elif opcion == "6":
        confirmar = input("¿Está seguro que desea salir? (s/n): ")
        if confirmar.lower() == 's':
            salir = True
            print("Saliendo del programa...")
        else:
            print("Continuando en el programa...")
    
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
