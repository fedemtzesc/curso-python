
def Menu():
    listaMenu = [0,1,2,3,4,5,6,7]

    while True:
        print("SELECCIONE UNA OPCION DE MENU:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Division Entera")
        print("6. Residuo")
        print("7. Potenciacion")
        print("0. Salir")
        opcion = int(input("Opcion: "))
        if(opcion not in listaMenu):
            print("Opcion Invalida! Intente de Nuevo...")
        elif(opcion==0):
            print("Adios!")
            return 0
        else:
            print("Has elegido la opcion", opcion)
            return opcion
            break   
            
Menu()
    
    