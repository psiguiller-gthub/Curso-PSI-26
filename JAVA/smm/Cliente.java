public class Cliente {
    
    // Atributos:
    public String nombre;
    public String apellido;
    public String numeroTelefono;
    public String email;

    // Constructor:
    public Cliente(String nombre, String apellido, String numeroTelefono, String email) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numeroTelefono = numeroTelefono;
        this.email = email;
    }

    // Métodos:
    public void mostrarInformacion() {
        System.out.println("Información del Cliente:");
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
        System.out.println("Número de Teléfono: " + numeroTelefono);
        System.out.println("Email: " + email);
    }
    

    // Getters y Setters:
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
