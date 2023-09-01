import time
import os

num1=10
num2=5

while True:
    print(f"Humano, que operacion eliges para {num1} y {num2}?")
    print("Presiona m para Multiplicar")
    print("Presiona d para Dividir")
    print("Presiona s para Sumar")
    print("Presiona r para Restar")
    print("Presiona e para Salir (Exit)")
    op = str(input("OPCION: ")).lower()
    
    if op == "m":
        print(f"La multiplicacion de {num1} x {num2} es igual a {num1*num2}")
    elif op == "d":
        print(f"La division de {num1} / {num2} es igual a {num1/num2}")
    elif op == "s":
        print(f"La suma de {num1} + {num2} es igual a {num1+num2}")
    elif op == "r":
        print(f"La resta de {num1} - {num2} es igual a {num1-num2}")
    elif op == "e":
        print(f"ADIOS HUMANO!")
        break
    else:
        print("Humano idiota, introdujiste una letra invalida!")
    
    time.sleep(3)
    os.system("clear")

print("\n\nFIN DEL PROGAMA!")