public class Cliente {
    // Atributos
    private String nombre;
    private String apellido;
    private String numeroTelefono;
    private String email;

    // Constructores
    public Cliente() {
    }
    public Cliente(String nombre, String apellido, String numeroTelefono, String email) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numeroTelefono = numeroTelefono;
        this.email = email;
    }
    
    // Métodos
    public String toString() {
        return "Información del Cliente:\n" +
               "Nombre: " + nombre + "\n" +
               "Apellido: " + apellido + "\n" +
               "Número de Teléfono: " + numeroTelefono + "\n" +
               "Email: " + email;
    }
    
    // Setters y Getters
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getApellido() {
        return apellido;
    }
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    public String getNumeroTelefono() {
        return numeroTelefono;
    }
    public void setNumeroTelefono(String numeroTelefono) {
        this.numeroTelefono = numeroTelefono;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

}