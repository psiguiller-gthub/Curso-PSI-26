public class Main {

    public static void main(String[] args) {

        String texto[] = { "Uno", "Dos", "Tres", "Cuatro", "Cinco" };
        for (int i = 0; i < 10; i++) {
            try{
                System.out.println("índice " + i + " = " + texto[i]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Fallo en el índice " + i);
            }    
                            
        }

    }
}
