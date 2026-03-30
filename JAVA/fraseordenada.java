import java.util.Arrays;

public class fraseordenada {
    public static void main(String[] args) {
        String frase = "¡Hola, Mundo... Adrianb dice que es el caracter coma, NO una COMA..!";
        char[] letras = frase.toCharArray();
        Arrays.sort(letras);
        String fraseOrdenada = new String(letras);
        System.out.println(fraseOrdenada);
    }
}
