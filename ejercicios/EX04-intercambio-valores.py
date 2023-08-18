print("Humano, ingresa los pinch... valores que se te piden a continuacon...")
a = int(input("a: "))
b = int(input("b: "))

print(f"Tus valores capturados son a: {a}, y b:  {b}")

aux = a
a = b
b = aux

print(f"Los valores intercambiados ahora son a: {a}, y b:  {b}")