#Definimos el precio de las frutas

precio_manzana = 1.5
precio_pera = 2.0 

#Pedimos la cantidad de frutas por semestre

manzanas_semestre1= int(input("Introduce los kilos de manzanas que vendistes en el primer semestre:"))
manzanas_semestre2= int(input("Introduce los kilos de manzanas que vendistes en el segundo semestre:"))
peras_semestre1= int(input("Introduce los kilos de peras que vendistes en el primer semestre:"))
peras_semestre2= int(input("Introduce los kilos de peras que vendistes en el segundo semestre:"))

#Calculamos las ganancias de cada cosa

venta_manzanas = (manzanas_semestre1 + manzanas_semestre2) * precio_manzana
venta_peras = (peras_semestre1 + peras_semestre2) * precio_pera

#Mostramos la ganacia total 

print("La ganancia total del año es de" , venta_manzanas + venta_peras , "€")