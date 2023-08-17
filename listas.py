'''
    Las listas nos permiten almacenar cualquier tipo de valor:
    enteros, flotantes, cadenas y hasta otras funciones
'''

lista=["Hola",
       "humano",
       "como",
       "estas",
       "?", 
       1, 
       2, 
       3.333, 
       [4, 5, 6, ["a", "b", "c", [3.1416]]]
       ]
# Mostramos toda la lista
print(lista)

#Mostramos el primer elemento
print("Primer elemento de la lista: \n\t",lista[0])

#Mostramos el ultimo elemento
print("Ultimo elemento de la lista: \n\t",lista[-1])

#Mostramos el penultimo elemento
print("Penultimo elemento de la lista: \n\t",lista[-2])

#Mostramos el rango del primero al tercero
#print("Primer elemento al tercero de la lista: ",lista[0:3])
print("Primer elemento al tercero de la lista: \n\t",lista[:3])

#Mostramos el rango del tercero al ultimo
print("Del segundo elemento de la lista hasta el ultimo:\n\t",lista[2:])