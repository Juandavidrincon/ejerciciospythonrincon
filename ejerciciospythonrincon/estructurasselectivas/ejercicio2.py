CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas en Unidades, compradas: "))
ValorUnitario= int(input("ingrese el total a pagar por las zapatillas: "))

subTotal = (CantidadDeZapatillas) * (ValorUnitario)
print(f"El precio a pagar sin el descuento es del:  {subTotal}")
# Ingresamos la variable de la cantidad de las zapatillas compradas y el valor unitario

if CantidadDeZapatillas>=3:
    totalaPagar= subTotal-(subTotal*0.20)  
    formatearNumero = str(totalaPagar).split('.')[0]
    print(f"El total a pagar con el descuento del 20% es: {formatearNumero} " )
elif CantidadDeZapatillas<3:
   totalaPagar2 = subTotal-(subTotal*0.10)
   formatearNumero = str(totalaPagar2).split('.')[0]
   print(f"EL Total a pagar con el descuento del 10% es: {formatearNumero} ")
   
  #Si la cantidad es mayor a 3 agregamos el descuento del 20% si es menor a 3 entonces le cambiamos el descuento al 10% 