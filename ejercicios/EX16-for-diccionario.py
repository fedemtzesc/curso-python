'''
En este ejercicio vamos a acceder a una lista de alumnos que 
tengan:
- nombre
- edad
- calificación

Además un diccionario que tenga alumnos y maestros donde:

Los alumnos tendrán:
- nombre
- edad
- calificación

Y los maestros tendrán:
- nombre
- grado
'''
alumnos = [
    {"nombre":"Federico", "edad":50, "calificacion":10},
    {"nombre":"Alicia", "edad":49, "calificacion":9},
    {"nombre":"Pedro", "edad":35, "calificacion":8},
    {"nombre":"Carlos", "edad":20, "calificacion":8},
]

'''
for alumno in alumnos:
    print(f"Nombre:{alumno['nombre']} Edad:{alumno['edad']} Calificacion:{alumno['calificacion']}")
'''
 
escuela = {
    "alumnos":alumnos,
    "maestros":[
        {"nombre":"Javier", "grado":"Licenciatura"},
        {"nombre":"Martha", "grado":"Maestria"},
        {"nombre":"Pedro", "grado":"Doctorado"},        
    ]
}

print("ALUMNOS\n---------------------")
for alumno in escuela['alumnos']:
    print(f"Nombre:{alumno['nombre']} Edad:{alumno['edad']} Calificacion:{alumno['calificacion']}")
print()
print("MAESTROS\n---------------------")
for maestro in escuela['maestros']:
    print(f"Nombre:{maestro['nombre']} Grado:{maestro['grado']}")

print(escuela)