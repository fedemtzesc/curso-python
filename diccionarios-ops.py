# Indentar diccionarios
alumnos = {
    1:["Federico","Martinez"],
    2:["Alicia", "Martinez"],
    3:["Agapito","Velez"]
    }
'''
print(alumnos[1])
print(alumnos[2])
print(alumnos[3])
print(alumnos[4])
'''

for alumno in range(1,5,1):
    if alumno in alumnos:
        print(alumnos[alumno])
    else:
        print("El alumno ",alumno," no existe")
print()

# Funcion get
for alumno in range(1,5,1):
    print(alumnos.get(alumno,f"El alumno {alumno} no existe"))

# Funcion keys
print(alumnos.keys())

# Funcion values
print(alumnos.values())

# Funcion items
print(alumnos.items())

# Funcion clear
alumnos.clear()
print("Alumnos clareados: ",alumnos)