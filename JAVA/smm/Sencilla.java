public class Sencilla extends Habitacion {

    // Atributos:
    private boolean exterior;
    private boolean tieneBanoPrivado;

    // Constructor:
    public Sencilla(int numero, double precio, String tipoCama, boolean vistaAlMar, boolean exterior, boolean tieneBanoPrivado) {
        super(numero, precio, tipoCama, vistaAlMar);
        this.exterior = exterior;
        this.tieneBanoPrivado = tieneBanoPrivado;
    }
    
    // Métodos:
    @Override
    public void mostrarDetalles() {
        System.out.println("Habitación Sencilla:");
        System.out.println("Número: " + getNumero());
        System.out.println("Precio: $" + getPrecio());
        System.out.println("Tipo de Cama: " + getTipoCama());
        System.out.println("Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No"));
        System.out.println("Exterior: " + (exterior ? "Sí" : "No"));
        System.out.println("Baño Privado: " + (tieneBanoPrivado ? "Sí" : "No"));
    }


    // Getters y Setters:
    public boolean isExterior() {
        return exterior;
    }

    public void setExterior(boolean exterior) {
        this.exterior = exterior;
    }

    public boolean isTieneBanoPrivado() {
        return tieneBanoPrivado;
    }

    public void setTieneBanoPrivado(boolean tieneBanoPrivado) {
        this.tieneBanoPrivado = tieneBanoPrivado;
    }

}


