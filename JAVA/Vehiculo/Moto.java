public class Moto extends Vehiculo {
    private String asiento;
    private String manillar;

    public Moto() {
    }

    public Moto(String matricula) {
        super(matricula);
    }

    public Moto(String matricula, String color) {
        super(matricula, color);
    }

    public Moto(String matricula, String color, String asiento, String manillar) {
        super(matricula, color);
        this.asiento = asiento;
        this.manillar = manillar;
    }

    public String getAsiento() {
        return asiento;
    }

    public void setAsiento(String asiento) {
        this.asiento = asiento;
    }

    public String getManillar() {
        return manillar;
    }

    public void setManillar(String manillar) {
        this.manillar = manillar;
    }
}