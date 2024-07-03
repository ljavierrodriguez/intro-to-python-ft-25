// Functions
/* 

Declarativas:

function functionName(params...){
    sentences
}

Expresiones de Funciona

const functionName = function(params...){
    sentences
}

Funciones de Flecha

const functionName = (params...) => {
    sentences    
}


*/

function sumar(a, b){
    return a+ b
}

let result = sumar(10, 10)
console.log(result)

const restar = (a, b = 5) => a - b

console.log(restar(10))


function totalizar(...rest){
    console.log(rest) // [1, 2, 3, 4, 5, 6]
}

totalizar(1, 2, 3, 4, 5, 6)