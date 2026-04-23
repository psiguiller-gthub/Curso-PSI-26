public class Doble extends Habitacion {

    // Atributos
    private boolean sofaCama;
    private boolean camasSeparadas;

    // Constructor
    public Doble(int numero, double precio, String tipoCama, boolean vistaAlMar, boolean sofaCama, boolean camasSeparadas) {
        super(numero, precio, tipoCama, vistaAlMar);
        this.sofaCama = sofaCama;
        this.camasSeparadas = camasSeparadas;
    }

    // Métodos
    @Override
    public String toString() {
        return "Habitación Doble:\n" +
               "Número: " + getNumero() + "\n" +
               "Precio: $" + getPrecio() + "\n" +
               "Tipo de Cama: " + getTipoCama() + "\n" +
               "Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No") + "\n" +
               "Sofá Cama: " + (sofaCama ? "Sí" : "No") + "\n" +
               "Camas Separadas: " + (camasSeparadas ? "Sí" : "No");
    }

    // Getters y Setters
    public boolean isSofaCama() {
        return sofaCama;
    }

    public void setSofaCama(boolean sofaCama) {
        this.sofaCama = sofaCama;
    }

    public boolean isCamasSeparadas() {
        return camasSeparadas;
    }

    public void setCamasSeparadas(boolean camasSeparadas) {
        this.camasSeparadas = camasSeparadas;
    }

}
