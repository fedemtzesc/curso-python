'''
    bin()
    hex()
    abs()
    round()
    eval()
'''

valor = bin(73)
print("bin(73): ", valor)

valor = int("0b1001001", 2)
print("0b1001001 : ", valor)

valor = hex(73)
print("hex(73) :  ", valor)

valor = int("0x49", 16)
print("0x49 : ", valor)

valor = abs(-16)
print("abs(-16) : ", valor)

valor = round(6.6)
print("round(6.6) : ", valor)

valor = round(6.5)
print("round(6.5) : ", valor)

valor = eval('5+6')
print("eval('5+6') : ", valor)
