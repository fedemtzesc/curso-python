
val = 1
bol = True


while bol:
    # Estas instrucciones se ejecutan al menos una vez
    print("Valor:", val)
    val+=1
    
    # Y esta seria la validacion en la parte de abajo del do-while
    if(val==5):
        bol=False   # Tanto esto...
        break       # como esto nos saca del while
        
        