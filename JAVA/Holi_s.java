import java.util.ArrayList;
import java.util.List;

public class Holi {

    public static int generaNumInt(){
        return (int) (Math.random()* 49 + 1);
    }

    public static int numComplementario (){
        int numerajo = (int) (Math.random()*9);
        return numerajo;
    }


    public static void main(String[] args) {

        int complementario = numComplementario();
        List<Integer> numeros = new ArrayList<>();

        for(int i = 0; i < 6; i++){
            int num = generaNumInt();
            while (numeros.contains(num)) {
                num = generaNumInt();
            }

            numeros.add(num);
        }
        System.out.println("Ganadora: " +numeros);
        System.out.println("Complementario: "+ complementario);
    }
}
