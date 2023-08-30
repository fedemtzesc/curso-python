'''
En este ejercicio vamos a pedir al humano que ingrese el 
número correcto para poder dividir correctamente ese número
de lo contrario colocaremos al humano en (como el tío novato
le llama) la rueda del hamster.

1.-Pedir al humano un número divisor.
2.-Pedir al humano un número dividendo superior a 0.
3.-Si el humano ingresa un dividendo superior a 0 realizar 
la división.
4.-De lo contrario reprenderlo y regresar al inicio hasta 
que cumpla la orden.
'''

divisor=float(input("Humano ingresa el divisor: "))
dividendo=float(input("Humano ingresa un dividendo mayor a cero: "))


while dividendo == 0:
    print("*** Humano imbecil! El dividendo tiene que ser diferente a cero!")
    dividendo=float(input("***  Ingresa dividendo mayor a cero: "))

resultado = divisor / dividendo

print(f"Resultado de {divisor}/{dividendo} = {resultado}")