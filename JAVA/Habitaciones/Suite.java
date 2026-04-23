public class Suite extends Habitacion {

    // Atributos
    private boolean jacuzzi;
    private boolean salaDeEstar;
    private boolean piscina;

    // Constructor
    public Suite(int numero, double precio, String tipoCama, boolean vistaAlMar, boolean jacuzzi, boolean salaDeEstar, boolean piscina) {
        super(numero, precio, tipoCama, vistaAlMar);
        this.jacuzzi = jacuzzi;
        this.salaDeEstar = salaDeEstar;
        this.piscina = piscina;
    }

    // Métodos
    @Override
    public String toString() {
        return "Habitación Suite:\n" +
               "Número: " + getNumero() + "\n" +
               "Precio: $" + getPrecio() + "\n" +
               "Tipo de Cama: " + getTipoCama() + "\n" +
               "Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No") + "\n" +
               "Jacuzzi: " + (jacuzzi ? "Sí" : "No") + "\n" +
               "Sala de Estar: " + (salaDeEstar ? "Sí" : "No") + "\n" +
               "Piscina: " + (piscina ? "Sí" : "No");
    }

    // Getters y Setters
    public boolean isJacuzzi() {
        return jacuzzi;
    }

    public void setJacuzzi(boolean jacuzzi) {
        this.jacuzzi = jacuzzi;
    }

    public boolean isSalaDeEstar() {
        return salaDeEstar;
    }

    public void setSalaDeEstar(boolean salaDeEstar) {
        this.salaDeEstar = salaDeEstar;
    }

    public boolean isPiscina() {
        return piscina;
    }

    public void setPiscina(boolean piscina) {
        this.piscina = piscina;
    }

}
