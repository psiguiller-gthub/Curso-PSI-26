import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class CalculadoraFechas {

    public static long calcularDiferenciaDias(LocalDate fechaSalida, LocalDate fechaEntrada) {
        // Validamos si la salida es después de la entrada
        if (fechaEntrada.isAfter(fechaSalida)) {
            throw new IllegalArgumentException("Error: La fecha de salida (" + fechaSalida + ") no puede ser anterior a la de entrada (" + fechaEntrada + ").");
        }
        // Devuelve los días que hay entre ambas fechas
        return ChronoUnit.DAYS.between(fechaEntrada, fechaSalida);  // Siempre va a devolver un long positivo o cero, nunca negativo
    }

    public static void main(String[] args) {
         try {
            // Ejemplo con error: Salida el día 15 y entrada el día 10
            LocalDate entrada = LocalDate.of(2026, 04, 15);
            LocalDate salida = LocalDate.of(2026, 04, 10);

            long dias = calcularDiferenciaDias(salida, entrada);
            System.out.println("Días: " + dias);
            
        } catch (IllegalArgumentException e) {
            // Aquí capturamos el error y mostramos el mensaje personalizado
            System.err.println(e.getMessage());
        }
                
        LocalDate entrada = LocalDate.of(2026, 3, 4);
        LocalDate salida = LocalDate.of(2026, 4, 21);
        //Sencilla miSencilla01 = new Sencilla();
        //Sencilla miSencilla02 = new Sencilla()

        long dias = calcularDiferenciaDias(salida, entrada);        
        System.out.println("Días de diferencia: " + dias);
    }
}
