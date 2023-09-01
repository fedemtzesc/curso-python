# Las tuplas son como listas pero son inmutables, no se pueden modificar
'''
    No les puedes ordenar, no les puedes hacer Pop, etc...
    Solo puedes:
    Mostrar un elemento
    Mostrar un rango
    in
    index
    
'''
tupla = (1,1,2,3,"Hola","humano") #A diferencia de las listas que usaban [] ahora usan ()

print("tupla: ",tupla, "<== LA TUPLA TIENE PARENTESIS A DIFERENCIA DE UNA LISTA")
print("tupla[1] = ", tupla[1])
print("tupla[0:3] = ", tupla[0:3])
print("El 3 esta en la tupla = ",3 in tupla)
print("tupla.index('Hola') = ", tupla.index("Hola"))
print("tupla.count(1) = ", tupla.count(1)) #cuantas veces se repite?
print("len(tupla) = ", len(tupla))

# Tambien puedo convertir una tupla en una lista nueva
lista = list(tupla)
print("lista: ", lista, "<== AHORA CON CORCHETES PORQUE ES UNA LISTA")
# Y ya le puedo aplicar las operaciones de una lista normal
lista.append('idiota')
lista.insert(3,"Fedex")
print(lista)
# Y tambien puedo convertir una lista en una nueva tupla
tupla2 = tuple(lista)
print("La tupla2: ", tupla2)