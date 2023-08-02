num1 = 10
num2 = 20
num3 = 30

res = num1 < num2
print(num1, " < ", num2, " : ", res)

res = num1 > num2
print(num1, " > ", num2, " : ", res)

res = num1 == num2
print(num1, " == ", num2, " : ", res)

res = num1 <= num2
print(num1, " <= ", num2, " : ", res)

res = num1 >= num2
print(num1, " >= ", num2, " : ", res)

res = num1 != num2
print(num1, " != ", num2, " : ", res)

# Las operaciones aritmeticas tienen prioridad antes que las relacionales
res = num1-num2 == -(num2-num1) 
print(num1-num2, " == ", -(num2-num1), " : ", res)