public class Main {
    public static void main(String[] args) {
        // Crear un objeto de la clase Vehiculo
        Vehiculo miVehiculo = new Vehiculo("1234ABC", "Rojo");
        System.out.println("Matricula: " + miVehiculo.getMatricula());
        System.out.println("Color: " + miVehiculo.getColor());

        // Crear un objeto de la clase Coche
        Coche miCoche01 = new Coche();
        Coche miCoche02 = new Coche("4587GHI");
        Coche miCoche03 = new Coche("7896JKL", "Blanco");
        Coche miCoche04 = new Coche("6543MNO", "Gris", "2", "Izquierdo");
        System.out.println("Matricula: " + miCoche02.getMatricula());
        System.out.println("Color: " + miCoche03.getColor());
        System.out.println("Puertas: " + miCoche04.getPuertas());
        System.out.println("Volante: " + miCoche04.getVolante());

        // Crear un objeto de la clase Moto
        Moto miMoto01 = new Moto();
        Moto miMoto02 = new Moto("5678DEF");
        Moto miMoto03 = new Moto("9012GHI", "Verde");
        Moto miMoto04 = new Moto("1234JKL", "Azul", "Deportivo", "Recto");
        System.out.println("Matricula: " + miMoto02.getMatricula());
        System.out.println("Color: " + miMoto03.getColor());
        System.out.println("Asiento: " + miMoto04.getAsiento());
        System.out.println("Manillar: " + miMoto04.getManillar());
    }

}