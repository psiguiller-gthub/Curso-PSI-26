public class Front {
    // Atributos:
    private String nombre;
    
    // Constructor:
    public Front(String nombre) {
        this.nombre = nombre;
    }

    // Métodos:
    public String toString() {
        return "Información del Front:\n" +
               "Nombre: " + nombre;
    }

    // Getters y Setters:
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

}
