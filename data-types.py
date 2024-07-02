# Data Types
''' 

String
Integer
Float
Boolean

Array:
    List = []
    Tuple = ()
    Set = {}

Dict
    
None

'''

nombre = "Luis"
apellido = 'Rodriguez'
nombre_completo = f"{nombre} {apellido}"

parrafo = f"""Lorem Ipsum es simplemente el texto de 
relleno de las imprentas y archivos de texto. Lorem Ipsum 
ha sido el texto de relleno estándar de las industrias 
desde el año 1500, cuando un impresor (N. del T. persona 
que se dedica a la imprenta) desconocido usó una galería 
de textos y los mezcló de tal manera que logró hacer un 
libro de textos especime {nombre}n. No sólo sobrevivió 500 años, 
sino que tambien ingresó como texto de relleno en documentos 
electrónicos, quedando esencialmente igual al original. 
Fue popularizado en los 60s con la creación de las hojas 
"Letraset", las cuales contenian pasajes de Lorem Ipsum, y 
más recientemente con software de autoedición, como por 
ejemplo Aldus PageMaker, el cual incluye versiones de
Lorem Ipsum."""

temp = 10 # int
temp = 10.5 # float

print(dir(temp))

open = True
active = False

x = None
y = None

numbers = [1, 2, 3, 4, 5, 6] # list
numbers.append(7)
numbers.append(8)
numbers.pop()

status = ('Active', 'Inactive', 'Canceled', 'Suspended', 'Complete') # tuple

frutas = {"Pera", "Manzana", "Melon", "Banana"}
print(frutas) # set


persona = {
    "name": "John",
    "lastname": "Doe",
    "age": "Unknown"
}

print(persona["name"])