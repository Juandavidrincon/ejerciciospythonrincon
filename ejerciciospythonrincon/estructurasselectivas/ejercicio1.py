nombEstudiante= input("Ingrese el Nombre del Estudiante: ")


califi_1 = int(input("Ingrese la Primera Nota (0-100): "))


califi_2 = int(input("Ingrese la Segunda Nota (0-100): "))


califi_3 = int(input("Ingrese la Tercera Nota(0-100): ")) # Ingresamos las variables que son el nombre de los estudiantes y sus notas

if  califi_1 >= 101 or califi_2 >= 101 or califi_3 >= 101:
    print(f"En Alguna de las Notas Ingresadas un Numero es Mayor a 100 no se admite como una nota valida")

#Si la nota digitada es mayor a 100 no será valida
else:
    caliCasi = (califi_1) + (califi_2) + (califi_3)

    califiFinal = caliCasi/3

    formatearNumero = str(califiFinal).split('.')[0]

    if califiFinal >= 70:
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Aprobó 🎉")
    
    else:
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Reprobó 😓")


#Si la nota final es mayor de 70 el estudiante será aprobado si es menor será reprobado