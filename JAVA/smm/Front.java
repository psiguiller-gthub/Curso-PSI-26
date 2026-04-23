public class Front {
    // Atributos:
    private String nombre;

    // Constructor:
    public Front(String nombre) {
        this.nombre = nombre;
    }

    // Métodos:
    public void mostrarInformacion() {
        System.out.println("Información del Front:");
        System.out.println("Nombre: " + nombre);
    }
    


    // Getters y Setters:
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

}
