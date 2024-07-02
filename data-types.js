// Data Types
/* 

String = "", '', ``
Number = -10, 10, -10.5, 10.5
Boolean = true / false
Undefined = undefined

Object:
    Array = []
    Literal Object = {}
    Null = null



*/

let nombre = "Luis"
let apellido = 'Rodriguez'
let nombreCompleto = `${nombre} ${apellido}`

let parrafo = `Lorem Ipsum es simplemente el texto de 
relleno de las imprentas y archivos de texto. Lorem Ipsum 
ha sido el texto de relleno estándar de las industrias 
desde el año 1500, cuando un impresor (N. del T. persona 
que se dedica a la imprenta) desconocido usó una galería 
de textos y los mezcló de tal manera que logró hacer un 
libro de textos especimen. ${nombre} No sólo sobrevivió 500 años, 
sino que tambien ingresó como texto de relleno en documentos 
electrónicos, quedando esencialmente igual al original. 
Fue popularizado en los 60s con la creación de las hojas 
"Letraset", las cuales contenian pasajes de Lorem Ipsum, y 
más recientemente con software de autoedición, como por 
ejemplo Aldus PageMaker, el cual incluye versiones de
Lorem Ipsum.`

let temp = 10
temp = 10.5
temp = -10
temp = -14.5

console.log(typeof(temp))

let open = true
let active = false

let x; // undefined
let y = null // object

let numbers = [1, 2, 3, 4, 5, 6] // object
numbers.push(7)
numbers.push(8)
numbers.pop()

let person = {
    name: 'John',
    lastname: 'Doe',
    age: 'Unknown'
}

console.log(person.name)
console.log(person['name'])