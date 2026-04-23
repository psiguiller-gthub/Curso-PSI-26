public class Vehiculo {
    // Atributos
    private String matricula;
    private String color;  

    // Constructor por defecto Vacío    SIEMPRE HACER UN CONSTRUCTOR VACÍO PARA PODER CREAR OBJETOS DE LA CLASE
    public Vehiculo() {  
    }

    // Constructor con parámetros
    public Vehiculo(String matricula) {
        this.matricula = matricula;
    }
    
    public Vehiculo(String matricula, String color) {
        this.matricula = matricula;
        this.color = color;
    }

// Métodos


// Getters y Setters
    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}