'''
Una pila (stack en inglés) es una lista ordenada o estructura de datos
que permite almacenar y recuperar datos, siendo el modo de acceso a sus
elementos de tipo LIFO (del inglés Last In, First Out, 
«último en entrar, primero en salir»)

Las operaciones de una pila son insertar y quitar.
Insertar (push) añade un elemento a la pila.
Quitar (pop) elimina o saca un elementos de la pila.
Veamos un ejemplo de LIFO: último en entrar, primero en salir
'''
pila=[]
pila.append("T")
pila.append("E")
pila.append("C")
pila.insert(len(pila),"A") #<==ESta instruccion seria el equivalente al PUSH
print(pila)

c = pila.pop()
print(c)
c = pila.pop()
print(c)
c = pila.pop()
print(c)