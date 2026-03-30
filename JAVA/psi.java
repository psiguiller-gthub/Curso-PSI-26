public class psi { // Entidad Principal
    public static int numero;
    public static void main(String[] args) { // MAIN Punto de Comienzo
        String holaMundo = "¡Hola, Mundo!";
        System.out.println(holaMundo);
        numero = 10;
        System.out.println("El número es: " + numero);
        System.out.println("¿Es mayor de edad (20)? " + isMayorDeEdad(20));
        System.out.println("La suma de 5 y 3 es: " + suma(5, 3));
        float resultado = multiplicar(6.3f, 5);
        System.out.println("El resultado de la multiplicación es: " + resultado);
        
    } // FIN MAIN

    public static boolean isMayorDeEdad(int num) { // Metodo 1
        return num > 18;
    } // Metodo 1

    public static int suma(int num01, int num02) { // Metodo 2
        return num01 + num02;
    } // Metodo 2

    public static float multiplicar(float num01, int num02) { // Metodo 3
        return num01 * num02;
    } // Metodo 3

} // Entidad Principal