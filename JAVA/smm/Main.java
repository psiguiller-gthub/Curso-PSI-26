import java.time.LocalDate;

public class Main {

    // función para calcular los días entre dos fechas
    public static int calcularDiasEntreFechas(LocalDate fechaEntrada, LocalDate fechaSalida) {
        return fechaEntrada.until(fechaSalida).getDays();
    }

    public static void main(String[] args){

        // Ejemplo de uso de calculo de dias entre fechas

        
        //objetos de habitaciones
        Sencilla habitacionSencilla = new Sencilla(101, 75.0,"Sencilla", false, false, true);
        Doble habitacionDoble = new Doble(201, 120.0,"Doble", true, true, true);
        Suite habitacionSuite = new Suite(301, 250.0,"Suite", true, true, true, true);

        //objeto de cliente
        //    public Cliente(String nombre, String apellido, 
        // String numeroTelefono, String email) {

        Cliente cliente1 = new Cliente("Juan", "Perez", "123456789", "juan.perez@email.com");
        Cliente cliente2 = new Cliente("Maria", "Gomez", "987654321", "maria.gomez@email.com");
        Cliente cliente3 = new Cliente("Carlos", "Lopez", "555555555", "carlos.lopez@email.com");
    
        //    public Reserva(int id, Cliente cliente, Habitacion habitacion, LocalDate fechaReserva, LocalDate fechaEntrada, LocalDate fechaSalida, int dias, double precioTotal) {
         // Ejemplo de creación de una reserva
         // Datos reserva 1
        LocalDate fechaEntrada = LocalDate.of(2024, 6, 1);
        LocalDate fechaSalida = LocalDate.of(2024, 6, 10);
        int dias = calcularDiasEntreFechas(fechaEntrada, fechaSalida);
        Reserva reserva1 = new Reserva(1, cliente1, habitacionSencilla, LocalDate.now(), fechaEntrada, fechaSalida, dias, habitacionSencilla.getPrecio() * dias);

        // Datos reserva 2
        LocalDate fechaEntrada2 = LocalDate.of(2024, 7, 5);
        LocalDate fechaSalida2 = LocalDate.of(2024, 7, 15);
        int dias2 = calcularDiasEntreFechas(fechaEntrada2, fechaSalida2);
        Reserva reserva2 = new Reserva(2, cliente2, habitacionDoble, LocalDate.now(), fechaEntrada2, fechaSalida2, dias2, habitacionDoble.getPrecio() * dias2);

        // Datos reserva 3
        LocalDate fechaEntrada3 = LocalDate.of(2024, 8, 20);
        LocalDate fechaSalida3 = LocalDate.of(2024, 8, 30);
        int dias3 = calcularDiasEntreFechas(fechaEntrada3, fechaSalida3);
        Reserva reserva3 = new Reserva(3, cliente3, habitacionSuite, LocalDate.now(), fechaEntrada3, fechaSalida3, dias3, habitacionSuite.getPrecio() * dias3);

        // Mostrar información de las reservas
        reserva1.mostrarInformacion();
        reserva2.mostrarInformacion();
        reserva3.mostrarInformacion();
        }

}