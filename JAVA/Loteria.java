import java.util.Random;
import java.
import.

public static int generaNumInt(){
    return
}

public class Loteria {
    public static void main(String[] args) {
        Random random = new Random();
        int[] numeros = new int[7];

        for (int i = 0; i < 6; i++) {
            numeros[i] = random.nextInt(49) + 1; // Números del 1 al 49
        }
        System.out.println("Números de la lotería: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
    }
}