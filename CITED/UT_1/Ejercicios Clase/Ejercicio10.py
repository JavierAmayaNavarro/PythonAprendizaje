# Pedimos los segundos al usuario
segundos = float(input("Introduce el tiempo en segundos: "))

# Convertimos los segundos a horas y minutos
horas = segundos / 3600
minutos = segundos / 60

# Mostramos el resultado
print(f"{segundos} segundos son {horas} horas o {minutos} minutos o {segundos} segundos")
