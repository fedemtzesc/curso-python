'''
    Los conjuntos son una coleccion no ordenada y sin elementos
    repetidos, algunos de los metodos usados en los conjuntos son:
    * add #Agregar un valor
    * discard #Elimina un valor
    * in
    * clear #Borra todos los elementos
    Ayuda a hacer la escritura mas rapido en disco duro por no estar
    ordenada como una lista.
'''
conjunto = set()
conjunto = {1,2,3, "hola", "humano", 1,2,3} # no tomara en cuenta los ultimos 1,2,3
print(conjunto)
conjunto.add(100)
print(conjunto)
encontrado = "humano" in conjunto
print("Encotnraste al humano?:", encontrado)
conjunto.discard(100)
print("conjunto sin el 100: ", conjunto)
conjunto.clear()
print("Conjunto clareado: ", conjunto)