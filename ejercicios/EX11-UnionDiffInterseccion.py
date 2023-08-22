'''
    Elementos que aparecen en las dos listas (Unión).
    Elementos que aparecen en la primer lista pero no en la segunda (Diferencia).
    Elementos que aparecen en la segunda lista pero no en la primera (Diferencia).
    Elementos que aparecen en Ambas listas (intersección).
'''
L1 = [1,2,2,3,4,5,4,8,54,54,87,99,5]
L2 = [1,2,4,6,2,4,5,2,45,22,55,77,88,99,77]

L1.sort
L2.sort

A = set(L1)
B = set(L2)

U = A | B
print("La union de ambas listas es", U)

DAB = A - B
print("Diff A-B = ", DAB)

DBA = B - A
print("Diff A-B = ", DBA)

INT = A & B
print("A & B = ", INT)