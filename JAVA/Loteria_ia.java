import java.util.Random;

public class Loteria {
    public static void main(String[] args) {
        Random random = new Random();
        int[] numeros = new int[7];

        for (int i = 0; i < 6; i++) {
            int nuevoNumero;
            boolean esRepetido;

            do {
                nuevoNumero = random.nextInt(49) + 1;
                esRepetido = false;

                // Comprobar si el número ya está en el array
                for (int j = 0; j < i; j++) {
                    if (numeros[j] == nuevoNumero) {
                        esRepetido = true;
                        break;
                    }
                }
            } while (esRepetido); // Si es repetido, repite el proceso

            numeros[i] = nuevoNumero;
        }

        System.out.println("Números de la lotería (sin repetir): ");
        for (int num : numeros) {
            System.out.printf("%02d ", num); // Formateado con 2 dígitos
        }
    }
}