# Total_Kilometros
# Programa que calcula consumo de gasolina y velocidad media de un viaje

KmRecorrido = float(input("Ingrese el total de kilmetros recorridos: "))
precio = float(input("Ingrese el precio de la gasolina (por litro): "))
dinero = float(input("Ingrese el dinero gastado en el viaje: "))
horas = float(input("Ingrese el tiempo de horas del viaje: "))
minutos = float(input("Ingrese el tiempo adicional de minutos: "))

# --- Calculos --- 
consumoGasoTotal = dinero / precio                        # Total en litros
consumoGasoKm = consumoGasoTotal / KmRecorrido            # Litros por kilómetro
consumoGaso100Km = consumoGasoKm * 100                    # Litros por 100 km

precioGasoKm = consumoGasoKm * precio                     # Gasto en euros por km
precioGaso100Km = precioGasoKm * 100                      # Gasto en euros por 100 km

velKmHora = KmRecorrido / (horas + (minutos / 60))        # Velocidad en km/h
velMetrSeg = (KmRecorrido * 1000) / ((horas * 3600) + (minutos * 60))  # Velocidad en m/s

# --- Salidas ---
print("El consumo de gasolina en litros por 100 kilómetros es:", consumoGaso100Km)
print("El consumo de gasolina en euros por 100 kilómetros es:", precioGaso100Km)
print("El consumo de gasolina en litros por kilómetro es:", consumoGasoKm)
print("El consumo de gasolina en euros por kilómetro es:", precioGasoKm)
print("La velocidad media en Km/Hora es:", velKmHora)
print("La velocidad media en metros/seg es:", velMetrSeg)