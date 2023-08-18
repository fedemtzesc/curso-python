'''
El diccionario de la Real Academia Española define una cola como “hilera de personas que esperan
turno para alguna cosa”.
Los elementos se atienden en el orden en que llegaron; es decir, el primer elemento en entrar 
(primero de la cola) es el primero en ser atendido (salir). 
La cola es una estructura FIFO (First In First Out).

La particularidad de una estructura de datos de cola es el hecho de que sólo podemos acceder al 
primer y al último elemento de la estructura. Las operaciones usuales de las colas son insertar 
y quitar. Así mismo, los elementos sólo se pueden eliminar por el principio y sólo se pueden 
añadir por el back de la cola.
'''
cola = []

cola.append("Juan")
print("llego ", cola[-1])
print(cola)

cola.append("Alejandra")
print("llego ", cola[-1])
print(cola)

cola.append("Pancho")
print("llego ", cola[-1])
print(cola)

cola.append("Maria")
print("llego ", cola[-1])
print(cola)

cola.append("Federico")
print("llego ", cola[-1])
print(cola)

for i in range(0,len(cola)):
    p = cola.pop(0)
    print("Se fue",p)
    print(cola)
