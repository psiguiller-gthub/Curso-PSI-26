public class Sencilla extends Habitacion {

    // Atributos
    private boolean exterior;
    private boolean banyoPrivado;
    
    // Constructores
    public Sencilla() {
    }
    public Sencilla(int numero, double precio, String tipoCama, boolean vistaAlMar, boolean exterior, boolean banyoPrivado) {
        super(numero, precio, tipoCama, vistaAlMar);
        this.exterior = exterior;
        this.banyoPrivado = banyoPrivado;
    }

    // Métodos
    @Override
    public String toString() {
        return "Habitación Sencilla:\n" +
               "Número: " + getNumero() + "\n" +
               "Precio: $" + getPrecio() + "\n" +
               "Tipo de Cama: " + getTipoCama() + "\n" +
               "Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No") + "\n" +
               "Exterior: " + (exterior ? "Sí" : "No") + "\n" +
               "Baño Privado: " + (banyoPrivado ? "Sí" : "No");
    }

    // Getters y Setters
    public boolean isExterior() {
        return exterior;
    }

    public void setExterior(boolean exterior) {
        this.exterior = exterior;
    }

    public boolean isBanyoPrivado() {
        return banyoPrivado;
    }

    public void setBanyoPrivado(boolean banyoPrivado) {
        this.banyoPrivado = banyoPrivado;
    }

}
