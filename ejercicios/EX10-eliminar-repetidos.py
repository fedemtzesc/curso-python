lista = [9,8,5,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4]
print(lista)
lista = list(set(lista))
lista.sort(reverse=True)
print(lista)
lista.sort(reverse=False)
print(lista)