let numero1 : number = 0
let numero2 : number = 1
let rta : number = 0
let contador : number = 0

while (contador <= 10) {
    let resultado = numero1 + numero2
    numero1 = numero2
    numero2 = resultado

    console.log(resultado);
    contador += 1
}