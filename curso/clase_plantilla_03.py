#Tercera forma de creacion de una clase (Al crear los campos en el constructor, ya no se definen en la clase)
class NombreClase:
    #nombre = "Sin Nombre"
    #apellidos = "Sin Apellidos"
    #edad = 0
    
    # Asi se define un constructor de clase en python con la palabra reservada __init__
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre #self es el equivalente al this de JAVA
        self.apellidos = apellidos
        self.edad = edad
    
# AHORA, SI INSTANCIAMOS LA CLASE USANDO SU CONSTRUCTOR ...
mi_clase = NombreClase('Federico', 'Martinez Escamilla', 50) # Asi creamos una instancia de la clase

# ... YA NO SERA NECESARIO ESTO:
#mi_clase.nombre="Federico" # Asi le creamos un campo y le asignamos un valor
#mi_clase.apellidos="Martinez Escamilla"
#mi_clase.edad=50

# Esto nos muestra la direccion de memoria donde se aloja la nueva instancia
print(mi_clase)
# Y aqui vemos los valores de los campos de la clase
print(mi_clase.nombre, mi_clase.apellidos, "=>edad:", mi_clase.edad) # Y asi accedemos al campo de la clase

        
    
    