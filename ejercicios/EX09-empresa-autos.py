'''
1.- El diccionario tendrá una lista con 3 empleados con nombre y edad. 
2.- El mismo diccionario tendrá una lista de 3 de autos con marca, modelo y   también cada auto tendrá 2 submodelos
4.- Accederemos a la edad del empleado número 3.
5.- Accederemos al segundo submodelo del auto número 2.
'''

empresa={
    "empleados":[
                 {"nombre":"Maria","edad":20},
                 {"nombre":"Esteban","edad":30},
                 {"nombre":"Pepe","edad":25}
                 ],
    "autos":[
        {"marca":"Ford","modelo":"f20","submodelos":["f20.01","f20.02"]},
        {"marca":"Nissan","modelo":"n20","submodelos":["n20.01","n20.02"]},
        {"marca":"Seat","modelo":"s20","submodelos":["s20.01","s20.02"]}
    ]
}
# Accederemos a la edad del empleado número 3.
print("Accederemos a la edad del empleado número 3 : ",empresa["empleados"][2]["edad"])

# Accederemos al segundo submodelo del auto número 2.
print("Accederemos al segundo submodelo del auto número 2 : ",empresa["autos"][1]["submodelos"][1])

# print("Ver en jsonviewer.com==>",empresa)
