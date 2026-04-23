import java.time.LocalDate;

public class Main {

    // función para calcular los días entre dos fechas
    public static int calcularDiasEntreFechas(LocalDate fechaEntrada, LocalDate fechaSalida) {
        return fechaEntrada.until(fechaSalida).getDays();
    }

    public static void main(String[] args) {

    // Objetos Habitaciones
    Sencilla habitacionSencilla = new Sencilla(101, 75.0, "Sencilla", false, false, true);
    Doble habitacionDoble = new Doble(201, 250, "Doble", false, true, true);
    Suite habitacionSuite = new Suite(301, 450, "Suite", false, true, true, true);

    // Objetos Clientes
    Cliente cliente1 = new Cliente("ANICETO", "Pérez", "12345678", "aniceto.perez@example.com");
    Cliente cliente2 = new Cliente("ANACLETA", "Gómez", "87654321", "anacleta.gomez@example.com");
    Cliente cliente3 = new Cliente("ANASTASIA", "López", "13579246", "anastasia.lopez@example.com");

    // Objetos del Front
    Front front = new Front("Recepción");

    // Objetos de Reservas
   // Ejemplo de creación de una reserva

   // Datos reserva 1
    LocalDate fechaEntrada = LocalDate.of(2026, 4, 1);
    LocalDate fechaSalida = LocalDate.of(2026, 4, 10);
    int dias = calcularDiasEntreFechas(fechaEntrada, fechaSalida);
    Reserva reserva1 = new Reserva(1, cliente1, habitacionSencilla, LocalDate.now(), fechaEntrada, fechaSalida, dias, habitacionSencilla.getPrecio() * dias);

    // Datos reserva 2
    LocalDate fechaEntrada2 = LocalDate.of(2025, 7, 5);
    LocalDate fechaSalida2 = LocalDate.of(2025, 7, 15);
    int dias2 = calcularDiasEntreFechas(fechaEntrada2, fechaSalida2);
    Reserva reserva2 = new Reserva(2, cliente2, habitacionDoble, LocalDate.now(), fechaEntrada2, fechaSalida2, dias2, habitacionDoble.getPrecio() * dias2);

    // Datos reserva 3
    LocalDate fechaEntrada3 = LocalDate.of(2024, 8, 20);
    LocalDate fechaSalida3 = LocalDate.of(2024, 8, 30);
    int dias3 = calcularDiasEntreFechas(fechaEntrada3, fechaSalida3);
    Reserva reserva3 = new Reserva(3, cliente3, habitacionSuite, LocalDate.now(), fechaEntrada3, fechaSalida3, dias3, habitacionSuite.getPrecio() * dias3);

    // Mostrar información de las reservas    
    System.out.println(reserva1.toString());    
    System.out.println(reserva2.toString());
    System.out.println(reserva3.toString());

    // Mostrar información de las habitaciones
    System.out.println(habitacionSencilla.toString());
    System.out.println(habitacionDoble.toString());
    System.out.println(habitacionSuite.toString());

    // Mostrar información de los clientes
    System.out.println(cliente1.toString());
    System.out.println(cliente2.toString());
    System.out.println(cliente3.toString());

    // Mostrar información del Front    
    System.out.println(front.toString());

    //reserva.mostrarInformacion();
    }

}