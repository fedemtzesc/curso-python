contador = 1

while contador in range(1,50001,1):
    if contador%2==0:
        print(f"  PAR = {contador}")
    else:
        print(f"IMPAR = {contador}")
    contador += 1
    
print("\nFin del ciclo!")