verdadero = True
falso = False
res = False


print('------------------------------------') 
print('Tabla de Verdad Operador AND') 
print('------------------------------------') 
print(verdadero, " AND ", verdadero, " : ", verdadero and verdadero)
print(verdadero, " AND ", falso, " : ", verdadero and falso)
print(falso, " AND ", verdadero, " : ", falso and verdadero)
print(falso, " AND ", falso, " : ", falso and falso)
print('\n------------------------------------') 
print('Tabla de Verdad Operador OR') 
print('------------------------------------') 
print(verdadero, " OR ", verdadero, " : ", verdadero or verdadero)
print(verdadero, " OR ", falso, " : ", verdadero or falso)
print(falso, " OR ", verdadero, " : ", falso or verdadero)
print(falso, " OR ", falso, " : ", falso or falso)
print('\n------------------------------------') 
print('Tabla de Verdad Operador XOR') 
print('------------------------------------') 
print(verdadero, " XOR ", verdadero, " : ", verdadero ^ verdadero)
print(verdadero, " XOR ", falso, " : ", verdadero ^ falso)
print(falso, " XOR ", verdadero, " : ", falso ^ verdadero)
print(falso, " XOR ", falso, " : ", falso ^ falso)
print('\n------------------------------------') 
print('Tabla de Verdad Operador NOT') 
print('------------------------------------') 
print(" NOT ", verdadero, " : ", not verdadero)
print(" NOT ", falso, " : ", not falso)
print('------------------------------------\n') 
