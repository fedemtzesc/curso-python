for i in range(1,5):
    print("Numero: ", i)
    
for l in [5,6,7]:
    print("Valor: ", l)
    
for t in [8,9,10]:
    print("ValorT: ", t)
    
diccionario={
    "Python":1,
    "Java":2,
    "Javascript":3
}

'''
for lenguaje in diccionario:
    print(f"{lenguaje} esta en el lugar {diccionario[lenguaje]}")
'''
# Esta es otra forma de hacer el ejemplo anterior
for clave, valor in diccionario.items():
    print(f"{clave} esta en el lugar {valor}")
    

# Tambien podemos iterar las letras de un String
texto = "Federico"
for letra in texto:
    print("Dame una: ", letra)
print("Que dice?: ", texto, "!")