//import java.time.LocalDate;
//import java.time.LocalTime;
//import java.util.Date;
import java.time.LocalDate;
import java.util.Random;

public class Holi {
    public static void main(String[] args) 
    {
    //  calculadora calculadora = new calculadora();
    //  System.out.println("Saludo!");
    //  int suma = (calculadora.sumaInt(2, 2));
    //  System.out.println(suma);

        Random random = new Random( );
        int num =random.nextInt(1000);
        System.out.println("Saludo!");
        System.out.println(num); 

    //    Date fecha = new Date();
    //    LocalDate fechaHoy = LocalDate.now();
    //    LocalTime horaActual = LocalTime.now();

    //    System.out.println(fecha);
    //    System.out.println(fechaHoy);
    //    System.out.println(horaActual);

    // Crear fecha aleatoria

        Random random2 = new Random();
        int dayoOfYear = random2.nextInt(365) + 1; // Días del 1 al 365
        LocalDate randomDate = LocalDate.ofYearDay(2026, dayoOfYear);
        System.out.println("Fecha aleatoria de 2026 es: " + randomDate);

        int dia = random.nextInt(31) + 1; // Días del 1 al 31 (bound: 32)
        int mes = random.nextInt(12) + 1; // Meses del 1 al 12 (bound: 13)
        int anyo = random.nextInt(2027 - 2020) + 2020; // Años entre 2020 y 2027, rango: [0 al 6]+2020 =2020-2026 (bound: 2027)

        System.out.println("Fecha aleatoria: " + dia + "/" + mes + "/" + anyo);

    }

}