import java.time.LocalDate;

public class Reserva {

    // Atributos
    private int id;
    private Cliente cliente;
    private Habitacion habitacion;
    private LocalDate fechaReserva;
    private LocalDate fechaEntrada;
    private LocalDate fechaSalida;
    private int dias;
    private double precioTotal;
    
    // Constructor
    public Reserva(int id, Cliente cliente, Habitacion habitacion, LocalDate fechaReserva, LocalDate fechaEntrada, LocalDate fechaSalida, int dias, double precioTotal) {
        this.id = id;
        this.cliente = cliente;
        this.habitacion = habitacion;
        this.fechaReserva = fechaReserva;
        this.fechaEntrada = fechaEntrada;
        this.fechaSalida = fechaSalida;
        this.dias = dias;
        this.precioTotal = precioTotal;
    }

    // Métodos
    @Override
    public String toString() {
    return "Información de la Reserva:\n" +
           "ID: " + id + "\n" +
           "Cliente: " + cliente.getNombre() + " " + cliente.getApellido() + "\n" +
           "Habitación: " + habitacion.getNumero() + "\n" +
           "Fecha de Reserva: " + fechaReserva + "\n" +
           "Fecha de Entrada: " + fechaEntrada + "\n" +
           "Fecha de Salida: " + fechaSalida + "\n" +
           "Días: " + dias + "\n" +
           "Precio Total: $" + precioTotal;
}
    /*public void mostrarInformacion() {
        System.out.println("Información de la Reserva:");
        System.out.println("ID: " + id);
        System.out.println("Cliente: " + cliente.getNombre() + " " + cliente.getApellido());
        System.out.println("Habitación: " + habitacion.getNumero());    
        System.out.println("Fecha de Reserva: " + fechaReserva);
        System.out.println("Fecha de Entrada: " + fechaEntrada);
        System.out.println("Fecha de Salida: " + fechaSalida);
        System.out.println("Días: " + dias);
        System.out.println("Precio Total: $" + precioTotal);
    } */

    // Getters y Setters
    public int getId() {
        return id;
    }     
    public void setId(int id) {
        this.id = id;
    }
    public Cliente getCliente() {
        return cliente;
    }
    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public Habitacion getHabitacion() {
        return habitacion;
    }
    public void setHabitacion(Habitacion habitacion) {
        this.habitacion = habitacion;
    }
    public LocalDate getFechaReserva() {
        return fechaReserva;
    }
    public void setFechaReserva(LocalDate fechaReserva) {
        this.fechaReserva = fechaReserva;
    }
    public LocalDate getFechaEntrada() {
        return fechaEntrada;
    }
    public void setFechaEntrada(LocalDate fechaEntrada) {
        this.fechaEntrada = fechaEntrada;
    }
    public LocalDate getFechaSalida() {
        return fechaSalida;
    }
    public void setFechaSalida(LocalDate fechaSalida) {
        this.fechaSalida = fechaSalida;
    }
    public int getDias() {
        return dias;
    }
    public void setDias(int dias) {
        this.dias = dias;
    }
    public double getPrecioTotal() {
        return precioTotal;
    }
    public void setPrecioTotal(double precioTotal) {
        this.precioTotal = precioTotal;
    }    

}
