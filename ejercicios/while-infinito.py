from os import system

contador = 1

system('clear')

while contador <100:
    try:
        numero = int(input("Introduce un entero: "))
        if numero == 111:
            print("Correcto! Y Adios!")
            break
        
        print("Has introducido ", numero)
    except Exception as e:
        print("Dije un número pendejo!")
        