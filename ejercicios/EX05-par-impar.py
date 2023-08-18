print("Humano, ingresa dos numeros pares:")
num1 = int(input("Captura el primer numero par: "))
num2 = int(input("Captura el siguiente numero par: "))

numPar1 = (num1%2==0)
numPar2 = (num2%2==0)

if not numPar1:
    print("Humano imbecil! El numero ", num1, " no es par!")
else:
    print("Muy bien humano! El numero", num1, " es par!")

if not numPar2:
    print("Humano imbecil! El numero ", num2, " no es par!")
else:
    print("Muy bien humano! El numero", num2, " es par!")