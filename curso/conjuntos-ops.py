a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {1,2,3,4,5,6}
d = {11,12,13,14,15,16}
e = frozenset({73,74,75}) # Asi se hace un conjunto inmutable

print("Conjunto a =>",a)
print("Conjunto b =>",b)
print("Conjunto d =>",d)
print("Conjunto e =>",e)

print("a es igual a b?: ", a == b)
u = a | b #union de a y b
print("Union (suma) entre a y b =>",u)

i = a & b #interseccion de a y b (es lo unico que tienen en comun a y b)
print("Interseccion entre a y b =>",i)

dab = a - b #diferencia entre a y b (se le quita a a todo lo que tenga en comun con b)
print("Diferencia entre a y b =>", dab)

dba = b - a #diferencia entre b y a (se le quita a b todo lo que tenga en comun con a)
print("Diferencia entre b y a =>", dba)

ds = a ^ b #diferencia SIMETRICA entre a y b (es la union de todo lo que no tienen en comun a y b)
print("Diferencia simetrica entre a y b (inversa de la interseccion)=>", ds)

# determinar cual conjunto es subconjunto de c
print("a es subconjunto de c: ",a.issubset(c))
print("b es subconjunto de c: ",b.issubset(c))
# Ahora determinamos si c es superconjunto padre de a y b
print("c es superconjunto de a: ",c.issuperset(a))
print("c es superconjunto de b: ",c.issuperset(b))
# Ahora conjuntos que estna desconectados uno de otro 
print("a esta desconectado de d?: ", a.isdisjoint(d))