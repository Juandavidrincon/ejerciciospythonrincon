#Le pedimos al usuario que ingrese el número de llantas que desea comprar
total_Comprado = int(input("Ingrese la cantidad de llantas que desea comprar: ")) 
#Aca, definimos que si la cantidad de compra es igual , menor o mayor cobre segun el precio indicado
if total_Comprado < 5:
    precio = 300
    total_A_pagar = total_Comprado * precio
elif total_Comprado<= 10:
    precio = 250
    total_A_pagar = total_Comprado * precio
elif total_Comprado> 10:
    precio = 200
    total_A_pagar = total_Comprado * precio


#Aca, es lo que se muestra segun los primeros datos y con la operacion pasada
print(f"El costo por cada llanta es de ${precio}")
print(f"El total a pagar por {total_Comprado} llantas es de $ {total_A_pagar}")