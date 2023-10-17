'''
    Declarar multiples variables
    Pedir al usuario que ingrese el valor de 2 variables
    Realizar varias operaciones aritmeticas
    pmostrar resultados en consola
'''

n01 = float(input("\nIngresa el primer numero: "))
n02 = float(input("Ingresa el segundo numero: "))

sum = n01 + n02
res = n01 - n02
mul = n01 * n02
div = n01 / n02
divEnt = n01 // n02
mod = n01 % n02

print("\nSUMA: ", n01, " + ", n02, " = ", sum)
print(f"RESTA: {n01} - {n02} = {res}")
print(f"MULTIPLICACION: {n01} * {n02} = {mul}")
print(f"DIVISION: {n01} / {n02} = {div}")
print(f"DIVISION ENTERA: {n01} // {n02} = {divEnt}")
print(f"MODULO: {n01} % {n02} = {mod}\n")

