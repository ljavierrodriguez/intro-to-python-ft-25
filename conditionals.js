// Conditionals
/* 

if (condition) {
    sentences
}

if (condition) {
    sentences
} else {
    sentences
}


if (condition) {
    sentences
} else if (condition) {
    sentences
} else {
    sentences
}


switch(value){
    case value1: sentences;
        break
    case value2: sentences;
        break
    default: sentences;
        break
}


*/

if(true){
    console.log(true)
}else{
    console.log(false)
}

/* && => and || => or ! => not */

let a = 6
let b = 5
let c = 10

if (a > b && a > c){
    console.log("A")
} else if (b > c){
    console.log("B")
} else {
    console.log("C")
}