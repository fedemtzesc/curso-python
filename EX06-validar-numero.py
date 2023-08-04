x = float(input("Humano captura el valor de X: "))
y = float(input("Humano captura el valor de Y: "))

if x<0 or abs(y)==1:
    print("X no puede ser menor que 0 o |Y| no puede ser igual a 1!")
else:
    f_x_y = (x**(1/2)) / (y**2 - 1)
    print(f"El resultado de f({x},{y}) = {f_x_y}")
