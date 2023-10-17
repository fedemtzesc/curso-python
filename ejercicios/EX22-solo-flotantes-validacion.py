# ESTE PROGRAMA VALIDA QUE SOLO SE CAPTUREN POR CONSOLA VALORES NUMERICOS

num = input("Captura un numero de coma floante: ")
lista = num.split(sep=".") #El metodo split devuelve una lista

if len(lista)==1:
    if lista[0].isdigit():
        print("El numero es entero!")
    else:
        print("El valor no es un numero!")
elif len(lista)==2:
    if "." in num and len(lista)==2 and lista[0].isdigit() and lista[1].isdigit():
        print(f"El numero {num} es de coma flotante!")
    else:
        print(f"El valor {num} NO es un numero de coma flotante!")
else:
    print(f"El valor {num} NO es de coma flotante!")