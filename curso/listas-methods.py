lista = [1,2,3]

print("longitud: ", len(lista), " Contenido: ",  lista)
lista.append(4)
print("longitud: ", len(lista), " Contenido: ", lista)
lista.insert(0,0) #En la posicion 0 pone el valor de 0
print("longitud: ", len(lista), " Contenido: ", lista)
lista.insert(4,77) #En la posicion 0 pone el valor de 0
print("longitud: ", len(lista), " Contenido: ", lista)
#lista.insert(5,88) #En la posicion 0 pone el valor de 0
print("longitud: ", len(lista), " Contenido: ", lista)
lista.extend([5, 6, 7]) #Se le puede agregar otra lista dentro
print("longitud: ", len(lista), " Contenido: ", lista)
lista+=[8,9,10, 8] #Hacemos lo mismo con el operador suma
print("longitud: ", len(lista), " Contenido: ", lista)
# A continuacion viene un ejemplo para validar si un numero esta contenido en la lista:
num = 77
if num in lista:
    print(f"El numero {num} SI esta en la lista")
else:
    print(f"El numero {num} NO esta en la lista")

# Ejemplo para mostrar la posicion en la que se encuentra el elemento
print("Posicion del valor 77: ", lista.index(77))
# Ejemplo que me dice cuantas veces se repite el elemento
num = 8
print("El numero", num ,"se repite", lista.count(num), "veces")
# El metodo pop elimina el ultimo elemento de la lista
lista.pop()
print("Eliminamos el ultimo elemento con pop() y nos queda: ", lista)
# o tambien el elemento para el cual indiquemos el indice
# para este ejemplo eliminamos el 77
lista.pop(4)
print("Ahora eliminamos el 77 con pop(4) y nos queda ahora: ", lista)
# El metodo remove quita elemento utilizando su valor
lista.remove(10)
print("La lista ahora queda de esta forma: ", lista)
# Finalmente usamos el metodo reverse para mostrar la lista al reves
# reverse reacomoda la lista al reves (OJO: no los ordena)
lista.reverse()
print("Ahora la lista esta reversada asi:  ", lista)
# Y a diferencia de reverse() el metodo sort los ordena modificando la lista
lista.sort(reverse=False)
print("Elementos ordenados: ", lista)
# El metodo sorted no modifica la lista pero si la regresa ordenada
lista2 = sorted(lista, reverse=True)
print("Lista2: ", lista2)
# Finamente podemos limpiar la lista con 
lista.clear()
print("Lista clareada: ", lista)