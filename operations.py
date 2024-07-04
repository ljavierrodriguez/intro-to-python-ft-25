import datetime
class Persona:
    def __init__(self, nombre, apellido, anio_nacimiento, gender):
        self.nombre = nombre
        self.apellido = apellido
        self.anio_nacimiento = anio_nacimiento
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

    # Metodo de Instancia
    def saludar(self):
        return f"Hola soy, {self.nombre} {self.apellido}"
    
    # Metodo de Estatico
    @staticmethod
    def get_edad(anio):
        return datetime.datetime.now().year - anio
    
    # Metodo de Clase
    @classmethod
    def sumar(self, a, b):
        return a + b
    



persona = Persona("John", "Doe", 1981, "male")

# Llamada al metodo de instancia
print(persona.saludar())

# Llamada al metodo estatico
print(Persona.get_edad(1981))

# Llamada al metodo de clase
print(persona.sumar(10, 10))

# Acceso a un atributo privado
print(persona.get_gender())

persona.set_gender("Female")
print(persona.get_gender())

