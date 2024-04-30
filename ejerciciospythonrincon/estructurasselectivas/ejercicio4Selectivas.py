

from random import *
valorCompra=int(input("Ingrese el Valor de la Compra: "))
balotas=choice(["Verde","Roja","Color diferente"])
# Asignamos las variables  donde indicamos el valor de la compra y los colores de las balotas
if balotas =="Rojo":
    print(f"Te toco el descuento del 15%")
    descuento=valorCompra*0.15
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
# Si la balota es igual a rojo asignamos el debido descuento que se le hace al valor de la compra digitada 
elif balotas=="Verde":
    print(f"Te toco el descuento del 20%")
    descuento=valorCompra*0.2
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
# Si la balota es igual a verde asignamos el debido descuento que se le hace al valor de la compra digitada 
elif balotas=="Color diferente":
    print(f"No tiene descuento")
    valorPagar=valorCompra
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
# Al salir un color diferente al rojo y verde no se les asigna descuento al valor de la compra digitada
    