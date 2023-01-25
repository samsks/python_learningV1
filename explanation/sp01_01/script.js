// Comentário

/*
    Funções
*/

function greetings() {
  return "olá M5";
}

// console.log(typeof greetings)
// console.log(greetings())

/*
    Tipos Primitivos
*/

// Inteiro
// CamelCase
const myInteger = 10;
// console.log(typeof myInteger)
// console.log(myInteger)

// // Float
// let myFloat = 5.2
// console.log(typeof myFloat)
// console.log(myFloat)

// // String
// const myString = "uma string"
// console.log(myString)
// console.log(typeof myString)

// // Boleano
// const myBooleanTrue = true
// const myBooleanFalse = false
// console.log(myBooleanTrue)
// console.log(typeof myBooleanTrue)

// Tipagem fraca
console.log(1 + "1");

/*
    Estruturas Condicionais
*/

// let x = 5

// if (x > 5){
//     console.log("x é maior que 5")
// } else if (x == 5){
//     console.log("x é igual a 5")
// } else {
//     console.log("x é menor que 5")
// }

// // let y = 10

// if (x == 5 && y == 10){
//     console.log('x = 5 E y = 10')
// }

// if (x == 5 || y == 10){
//     console.log('x = 5 OU x = 10')
// }

// if (!(x == 20)){
//     console.log('x não é 20')
// }

// let myString = 'x-salada'
// if (myString.includes('x')){
//     console.log('x encontrado')
// }

// if (!myString.includes('z')){
//     console.log('z não encontrado')
// }

// /*
//     Estruturas de Repetição
// */

let myString = "olá M5!";

for (let i = 0; i < myString.length; i++) {
  console.log(myString[i]);
}

// for (let x of myString){
//     console.log(x)
// }

// for (let i = 0; i < myString.length; i++){
//     console.log(i, myString[i])
// }

for (let i = 0; i < 10; i++) {
  console.log(i);
}

// for (let i = 2; i < 10; i+=2){
//     console.log(i)
// }

// for (let i = 0; i < 10; i++){
//     console.log(i)
//     if (i == 3){
//         break
//     }
// }

// let z = 0

while (z < 3) {
  console.log("loop while", z);
  z++;
}
