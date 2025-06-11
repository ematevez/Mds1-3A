function dividir(a, b) {
    if(b==0){
    print("No su puede dividir por cero);
    }else{    
    return a / b; // ERROR: no valida división por cero
    }
    }
console.log(dividir(4, 0)); // Debería manejar el error
