

function saludar01(nombre) {
    return `Hola ${nombre}`;  // El & se utiliza para insertar la variable dentro de la cadena de texto.
}

const saludar02 = (nombre) => {   
    return "Hola " + nombre;
}

const sumar01 = (a, b) => {
    return a + b;
}

const sumar02 = (a, b) => a + b;  // La flecha indica que es una función, y el resultado de la expresión se devuelve automáticamente.

const duplicar = numero => numero * 2;

const darAlerta = () => "¡Cuidado!";

//-------------------------------------------------------------------

const isZero = numero => numero === 0;  // Función que verifica si un número es cero utilizando el operador de igualdad estricta (===). Devuelve true si el número es cero, y false en caso contrario.

const dividir = (a, b) => a / b;

const isMayorEdad = (edad) => {

    if(edad >= 18) {
        return "Eres mayor de edad";
    }

    return "";
};


const porteroDiscoteca = (edad) => {

    if(isMayorEdad(edad)) {
        return "Puedes entrar";
    }

    return "No puedes entrar";
};

const alCuadrado = numero => numero ** 2;  // Función que eleva un número al cuadrado utilizando el operador de exponenciación (**).


console.log(isZero(0));
console.log(isZero(5));

console.log(isMayorEdad(20));
console.log(isMayorEdad(15));

console.log(porteroDiscoteca(22));
console.log(porteroDiscoteca(16));

console.log(alCuadrado(3));  // 9
console.log(alCuadrado(4));  // 16

//const isZero = numero => numero === 0;  // Operador ternario para evaluar si el número es cero o no. Op.ternario: condición ? valor_si_verdadero : valor_si_falso. trabaja con tres operandos.

//const isMayorEdad = edad => edad >= 18 ? "Eres mayor de edad" : "";  // Operador ternario para evaluar si la edad es mayor o igual a 18.

//const porteroDiscoteca = (edad) => isMayorEdad(edad) ? "Puedes entrar" : "No puedes entrar";  // Función que utiliza la función isMayorEdad para determinar si una persona puede entrar a una discoteca o no.

// CASOS DE USO

//console.log(saludar01("Juan"));
//console.log(saludar02("María"));
//console.log(sumar01(5, 10));
//console.log(sumar02(5, 10));
//console.log(duplicar(5));
//console.log(darAlerta());
