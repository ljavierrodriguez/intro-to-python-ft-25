class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._gender = None # Protegido
        self.__address = None # Privado

    def saludar(self):
        return f"Hola Soy, {self.nombre} {self.apellido}"
    
    def __repr__(self) -> str:
        return f"<Persona nombre={self.nombre} apellido={self.apellido}>"



persona = Persona("Jane", "Doe", "Unknown")
print(persona)
print(persona.saludar())

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, universidad):
        super().__init__(nombre, apellido, edad)
        self.universidad = universidad 

    def saludar(self):
        return f"Hola soy el estudiante, {self.nombre} {self.apellido}"


est = Estudiante("Jane", "Doe", "Unknown", "Universidad de Chile")
print(est)
print(est.saludar())


est1 = Persona("John", "Doe", 10)
est2 = Persona("Jane", "Doe", 15)
est3 = Persona("Jonny", "Doe", 6)
est4 = Persona("Sam", "Doe", 3)

print(est1, est2, est3)