n=0
f=1

while True:
    num = input("Humano captura un numero mayor a 1: ")
    
    if num.isdigit():
        n = int(num)   
        if n>1:
            break
        else:
            print("Humano imbecil! Te pedi un numero mayor a uno")
    else:
        print("Humano imbecil! Te pedi un numero no una letra!")
            
for n in range(n,0,-1):
    if n==1:
        print(n, end=" = ")
    else:
        print(n, end=" x ")
    f*=n
    
print("", f)

