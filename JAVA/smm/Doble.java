public class Doble extends Habitacion {

    // Atributos:
    private boolean tieneSofaCama;
    private boolean tieneCamasSeparadas;


    // Constructor:
    public Doble(int numero, double precio, String tipoCama, boolean vistasAlMar, boolean tieneSofaCama, boolean tieneCamasSeparadas) {
        super(numero, precio, tipoCama, vistasAlMar);
        this.tieneSofaCama = tieneSofaCama;
        this.tieneCamasSeparadas = tieneCamasSeparadas;
    }


    //Métodos:
    @Override
    public void mostrarDetalles() {
        System.out.println("Habitación Doble:");
        System.out.println("Número: " + getNumero());
        System.out.println("Precio: $" + getPrecio());  
        System.out.println("Tipo de Cama: " + getTipoCama());
        System.out.println("Vista al Mar: " + (isVistaAlMar() ? "Sí" : "No"));
        System.out.println("Sofá Cama: " + (tieneSofaCama ? "Sí" : "No"));
        System.out.println("Camas Separadas: " + (tieneCamasSeparadas ? "Sí" : "No"));
    }


    // Getters y Setters:
    public boolean isTieneSofaCama() {
        return tieneSofaCama;
    }

    public void setTieneSofaCama(boolean tieneSofaCama) {
        this.tieneSofaCama = tieneSofaCama;
    }

    public boolean isTieneCamasSeparadas() {
        return tieneCamasSeparadas;
    }   

    public void setTieneCamasSeparadas(boolean tieneCamasSeparadas) {
        this.tieneCamasSeparadas = tieneCamasSeparadas;
    }




}


