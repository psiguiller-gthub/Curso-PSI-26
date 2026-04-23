public class Suite extends Habitacion {

    // Atriubutos:
    private boolean tieneJacuzzi;
    private boolean tieneSalaDeEstar;
    private boolean tienePiscina;

    // Constructor:
    public Suite(int numero, double precio, String tipoCama, boolean vistaAlMar, boolean tieneJacuzzi, boolean tieneSalaDeEstar, boolean tienePiscina) {
        super(numero, precio, tipoCama, vistaAlMar);
        this.tieneJacuzzi = tieneJacuzzi;
        this.tieneSalaDeEstar = tieneSalaDeEstar;
        this.tienePiscina = tienePiscina;
    }
  
    // Métodos:
    @Override
    public void mostrarDetalles() {
        System.out.println("Habitación Suite:");
        System.out.println("Número: " + getNumero());
        System.out.println("Precio: $" + getPrecio());
        System.out.println("Tipo de Cama: " + getTipoCama());
        System.out.println("Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No"));
        System.out.println("Jacuzzi: " + (tieneJacuzzi ? "Sí" : "No"));
        System.out.println("Sala de Estar: " + (tieneSalaDeEstar ? "Sí" : "No"));
        System.out.println("Piscina: " + (tienePiscina ? "Sí" : "No"));
    }
 
    // Getters y Setters:
    public boolean isTieneJacuzzi() {
        return tieneJacuzzi;
    }
    public void setTieneJacuzzi(boolean tieneJacuzzi) {
        this.tieneJacuzzi = tieneJacuzzi;
    }
    public boolean isTieneSalaDeEstar() {
        return tieneSalaDeEstar;
    }
    public void setTieneSalaDeEstar(boolean tieneSalaDeEstar) {
        this.tieneSalaDeEstar = tieneSalaDeEstar;
    }
    public boolean isTienePiscina() {
        return tienePiscina;
    }
    public void setTienePiscina(boolean tienePiscina) {
        this.tienePiscina = tienePiscina;
    }

  
}
