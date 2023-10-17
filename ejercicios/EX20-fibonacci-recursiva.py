'''
Hacer un programa que:
    - Programa que pida un número entero n.
    - Validar que el número n sea mayor a 1.
    - Bucle que genere una serie fibonacci de 1 hasta n.
    - 1 1 2 3 5 8 13 21 34...n
'''

def calculaFibonacci(n):
    if n < 2:
        return n;
    return calculaFibonacci(n-1) + calculaFibonacci(n-2)

x=0

while True:
    n = int(input("Humano por favor ingresa un numero mayor a 1: "))
    
    if n < 1:
        break

    for i in range(0,n+1):
        x = calculaFibonacci(i)
        print(f"{x}",end=" ")
    print()
    



