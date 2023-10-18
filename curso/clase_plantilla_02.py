#Segunda forma de creacion de una clase (se le crean los campos y se inicializan a la vez)
class NombreClase:
    nombre = "Sin Nombre"
    apellidos = "Sin Apellidos"
    edad = 0
    
mi_clase = NombreClase() # Asi creamos una instancia de la clase

mi_clase.nombre="Federico" # Asi le creamos un campo y le asignamos un valor
mi_clase.apellidos="Martinez Escamilla"
mi_clase.edad=50

print(mi_clase)
print(mi_clase.nombre, mi_clase.apellidos, "=>edad:", mi_clase.edad) # Y asi accedemos al campo de la clase

        
    
    