import java.util.Scanner;


    public class Universidad {

        public static double interesSimple(double capital, double tasa, double tiempo) {
            double interes = capital * tasa * tiempo / 100.0;
            return interes;
        }

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.println("--- Calculadora de Interés Simple ---");

            System.out.print("Por favor, ingresa el capital: ");
            double capital = scanner.nextDouble();

            System.out.print("Ahora, ingresa la tasa de interés (%): ");
            double tasa = scanner.nextDouble();

            System.out.print("Ahora, ingresa el tiempo (en años): ");
            double tiempo = scanner.nextDouble();

            double interes = interesSimple(capital, tasa, tiempo);

            System.out.print("El interés generado es: ");
            System.out.printf("%.2f%n", interes);

            double montoFinal = capital + interes;
            System.out.print("El monto final es: ");
            System.out.printf("%.2f%n", montoFinal);

            scanner.close();
        }
    }

