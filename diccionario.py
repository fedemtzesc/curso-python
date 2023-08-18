diccionario={} # declaracion de un diccionario
diccionario={"python":1, "java":2, "javascript":3}

print(diccionario)
print("Elementos en el diccionario: ",len(diccionario))

# Obetener el valor de cada llave en el diccionario:
print(diccionario["python"])
print(diccionario["java"])
print(diccionario["javascript"])

# Agregar un elemento nuevo
diccionario["c++"] = 4
print(diccionario)

# Modificar un elemento de la lista
diccionario["c++"] = 5
print(diccionario)

# Borramos un elemento
del(diccionario["c++"])
print(diccionario)

# Metemos dos elementos a la vez
diccionario["c/c++"]=[4,5]
diccionario["c/c++"]=(4,5)
diccionario["otros"] = {100, 101, 102}
print(diccionario)
