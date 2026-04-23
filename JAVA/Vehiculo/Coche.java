public class Coche extends Vehiculo {
    // Atributos
    private String puertas;
    private String volante;

    // Constructores
    public Coche() {
    }

    public Coche(String matricula) {
        super(matricula);
    }

    public Coche(String matricula, String color) {
        super(matricula, color);
    }

    public Coche(String matricula, String color, String puertas, String volante) {
        super(matricula, color);
        this.puertas = puertas;
        this.volante = volante;
    }
    // Setters y Getters
    public String getPuertas() {
        return puertas;
    }

    public void setPuertas(String puertas) {
        this.puertas = puertas;
    }

    public String getVolante() {
        return volante;
    }

    public void setVolante(String volante) {
        this.volante = volante;
    }
}