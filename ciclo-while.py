import time

contador = 1

while contador <= 100:
    print(f"Vamos en : {contador:03d}")
    time.sleep(100/1000)
    contador+=1
    
print("\n***  Fin del Ciclo!  ***\n\n")