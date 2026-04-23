
public class Habitacion {

    // Atibutos:
    private int numero;
    private boolean ocupado = false;
    private double precio;
    private String tipoCama; 
    private boolean vistaAlMar;

    // Constructor Vacío:
    public Habitacion() {
    }

   
    public Habitacion(int numero, double precio, String tipoCama, boolean vistaAlMar) {
        this.numero = numero;
        this.precio = precio;
        this.tipoCama = tipoCama;
        this.vistaAlMar = vistaAlMar;
    }

    //Métodos:
    public void reservar() {
        this.ocupado = true;
    }

    public void cancelarReserva() {
        this.ocupado = false;
    }
    public void mostrarDetalles() {
        System.out.println("Detalles de la Habitación:");
        System.out.println("Número: " + numero);
        System.out.println("Ocupado: " + (ocupado ? "Sí" : "No"));
        System.out.println("Precio: $" + precio);
        System.out.println("Tipo de Cama: " + tipoCama);
        System.out.println("Vista al Mar: " + (vistaAlMar ? "Sí" : "No"));

    }


    // Getters y Setters:
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
    public boolean isOcupado() {
        return ocupado;
    }

    public void setOcupado(boolean ocupado) {
        this.ocupado = ocupado;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
    public String getTipoCama() {
        return tipoCama;
    }

    public void setTipoCama(String tipoCama) {
        this.tipoCama = tipoCama;
    }
    public boolean isVistaAlMar() {
        return vistaAlMar;
    }

    public void setVistaAlMar(boolean vistaAlMar) {
        this.vistaAlMar = vistaAlMar;
    }



}
