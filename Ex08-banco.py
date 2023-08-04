saldo = 1000.0

print("!!Bienvenido pequeño mortal al banco¡¡\n\
      Elige una opcion de las siguientes:\n\
      1. Ingresar Dinero\n\
      2. Retirar Dinero\n\
      3. Salir\n\n\
      Opcion:")

opcion = int(input())

if opcion==1:
    desposito = float(input("Cuanto dinero va a ingresar?:"))
    saldo+=desposito
    print(f"Tu nuevo saldo es {saldo}")
elif opcion==2:
    retiro = float(input("Cuanto dinero va a retirar?:"))
    if retiro>saldo:
        print("Pinche humano! Te estas sobregirando! Tu saldo es de $", saldo)
        quit()
    else:
        saldo-=retiro
        print(f"Tu nuevo saldo es {saldo}")
else:
    print("ADIOS!")
    quit()


#TIP: En python no existe el switch()
