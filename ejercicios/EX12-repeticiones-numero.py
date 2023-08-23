tupla=(1,2,4,2,5,6,7,8,15,2,3)
print(tupla)
numero = int(input("Humano, ingresa un numero de la lista:"))
if numero in tupla:
    print(f"Humano, cuantas veces se repite el numero {numero} en la lista?")
    veces = int(input())
    vecesRep=tupla.count(numero)
    if veces == vecesRep:
        print("Buen chico! ahora dame la patita")
    else:
        print(f"Humano pendeo! El numero {numero}, se repite {vecesRep} veces en la lista.")
else:
    print("Humano estupido! El numero que elegiste no esta en la lista!")
    



