#Este codigo analiza los descuentos segun el día de la semana, los valores de los productos
#su descuento aplicado y el costo final
#Hecho por Pedro salamanca Y Jose Patiño Hincapie 


dia=input("Ingrese el dia: ").lower()
producto=input("Ingrese el producto fruver, carnes, vino: ").lower()
precio=float(input("Ingrese el valor del producto "))

descuento=0

if dia=="lunes" and producto=="fruver":
  descuento=precio*0.3
elif dia=="martes" and producto=="carnes":
  descuento=precio*0.3
elif dia=="jueves" and producto=="vino":
  descuento=precio*0.3

elif dia=="miercoles":
  if producto=="carnes":
    descuento=precio*0.15
  elif producto=="fruver":
    descuento=precio*0.1
  elif producto=="vino":
    descuento=precio*0.05

elif dia=="viernes":
  if producto=="vino":
    descuento=precio*0.15
  elif producto=="fruver":
    descuento=precio*0.1
  elif producto=="carnes":
    descuento=precio*0.05

#Calculo final
valor_descuento=descuento
total=precio-valor_descuento

print("Descuento aplicado: ", valor_descuento)
print("Total a pagar: ", total)