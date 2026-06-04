class Vehiculo {

    #velocidad;   // Propiedad privada. No se puede acceder directamente desde fuera de la clase.

    constructor(marca, modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.encendido = false;
        this.#velocidad = 0;       // Propiedad privada. Getters y setters para acceder.
        this.intermitente = false;
    }

    arrancar() {
        this.encendido = true;
        console.log(`${this.marca} ${this.modelo} arrancado.`);
    }

    apagar() {

        if(this.velocidad > 0) {
            console.log("No se puede apagar en movimiento.");
            return;
        }
        this.encendido = false;
        console.log(`${this.marca} ${this.modelo} apagado.`);
    }

    acelerar() {

        if(!this.encendido) {
            console.log("El vehículo está apagado.");
            return;
        }

        this.velocidad += 10;

        console.log(`Velocidad: ${this.velocidad} km/h`);
    }

    frenar() {

        if(this.velocidad > 0) {
            this.velocidad -= 10;
        }

        console.log(`Velocidad: ${this.velocidad} km/h`);
    }

    ponerIntermitente() {
        this.intermitente = true;
        console.log("Intermitente activado.");
    }

    quitarIntermitente() {
        this.intermitente = false;
        console.log("Intermitente desactivado.");
    }
}

class Coche extends Vehiculo {

    abrirMaletero() {
        console.log("Maletero abierto.");
    }
}

class Moto extends Vehiculo {

    hacerCaballito() {

        if(this.velocidad > 20) {
            console.log("La moto hace un caballito.");
        }
        else {
            console.log("Necesitas más velocidad.");
        }
    }
}


/* VARIABLES */
let coche1 = new Coche("Toyota", "Corolla");
let moto1 = new Moto("Yamaha", "R1");


/* CONSTANTES */
const LIMITE_VELOCIDAD = 120;


/* FUNCIONES */
function mostrarLimite() {
    console.log(`Límite: ${LIMITE_VELOCIDAD} km/h`);
}


/* PRUEBAS */
coche1.arrancar();
coche1.acelerar();
coche1.ponerIntermitente();
coche1.frenar();
coche1.apagar();

console.log("----------------");

moto1.arrancar();
moto1.acelerar();
moto1.acelerar();
moto1.acelerar();
moto1.hacerCaballito();

mostrarLimite();