'''
Hacer un programa que:
    - Programa que pida un número entero n.
    - Validar que el número n sea mayor a 1.
    - Bucle que genere una serie fibonacci de 1 hasta n.
    - 1 1 2 3 5 8 13 21 34...n
'''
x=0
y=1
z=0

while True:
    n = int(input("Humano por favor ingresa un numero mayor a 1: "))
    
    if n < 1:
        break

    print("1",end=" ")
    for i in range(0,n):
        z=x+y
        print(f"{z}",end=" ")
        x=y
        y=z
    
    x=0
    y=1
    z=0

    print()
    


