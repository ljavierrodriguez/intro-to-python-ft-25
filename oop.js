class Persona {
    constructor(nombre, apellido, edad){
        //console.log("Clase Persona")
        this.nombre = nombre
        this.apellido = apellido
        this.edad = edad
    }

    nombre = "";
    apellido = "";
    edad = ""

    saludar(){
        return `Hola Soy, ${this.nombre} ${this.apellido}`
    }
}


let persona = new Persona("John", "Doe", "Unknown")
console.log(persona)
console.log(persona.nombre)
console.log(persona.saludar())


class Estudiante extends Persona {
    constructor(nombre, apellido, edad, universidad){
        super(nombre, apellido, edad)
        this.universidad = universidad
    }

    saludar(){
        return `Hola Soy el estudiante, ${this.nombre} ${this.apellido}`
    }
}

let est = new Estudiante("David", "Smith", "30", "Universidad de Chile")
console.log(est)
console.log(est.saludar())