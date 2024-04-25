preciodelacompra=int(input("Digite el valor de la compra : "))
descuento=int(input("Digite el descuento : "))
#Primero asigné las variables y puse el comando int para indicarle al input que son numeros enteros y le pido al usuario con el input que me brinde la informacion'''
sacarDescuento=descuento / 100 
#segundo, hacemos la operacion y dividimos el descuento sobre 100 que es 100% del valor del descuento
multiplicar=sacarDescuento * preciodelacompra
#tercero, multiplique el descuento por el valor de la compra para saber cuanto se le tiene que restar al precio final
precioFinal=preciodelacompra - multiplicar
#cuarto, aca se coge el valor de la compra y se le resta el valor del descuento
print("La compra fue",preciodelacompra,"con un descuento de",descuento ,"%","el valor final a pagar es",precioFinal)
#quinto, con el comando print se imprime el valor de la compra, el descuento, precio final y con la "," concateno las variables y listo