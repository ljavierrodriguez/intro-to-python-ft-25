# Functions
from random import randint
from math import floor, ceil
""" 

def function_name(params, ...):
    sentences


function_name = lambda expresion : return 

"""

# Parametros Posicionales y por defecto
def sumar(a, b = 10):
    return a + b

result = sumar(10, 10)
print(result)


restar = lambda a, b = 5: a - b


def datos(name, lastname, age, gender):
    return f"Name: {name}"

print(datos("Luis", "Rodriguez", 40, "male"))

print(sumar(10))

# Parametros keywords
def nombre_completo(name, lastname):
    return f"{name} {lastname}"

print(nombre_completo(lastname="Doe", name="John"))


# Empaquetamiento de Argumentos o Parametros

def totalizar(*args):
    print(args) # (1, 2, 3, 4, 5, 6)
    return sum(args)

totalizar(1, 2, 3, 4, 5, 6)


# Empaquetamiento de Argumentos Keywords

def information(**kargs):
    return f"{kargs["name"]} {kargs["lastname"]}" # John Doe

print(information(name="John", lastname="Doe"))

str(1) # "1"
int(10.5) # 10
float(10) # 10.0


names = ["Hugo", "Pago", "Luis"]

results = list(filter(lambda valor: valor.__contains__('L'), names))
print(results) # ["Hugo"]