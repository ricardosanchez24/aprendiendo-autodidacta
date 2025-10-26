import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
public class holaMundo{
    
    public static int sumar(int numero1, int numero2){
        int suma = numero1 + numero2;
        return suma;
    }

    public static void main(String[] args) {
        
        System.out.println("hola mundo");

        String name = "ricardo";
        name = "caro";
        System.out.println(name);

        int numero = 5;
        numero = 5*5;
        System.out.println(numero);
        double numero2 = 19.99;
        System.out.println(numero2);

        if (numero == 10){
            System.out.println("el numero es 10");
        }else if (numero == 25){
            System.out.println("el numero es 25");
        }else{
            System.out.println("el numero es diferente de 10");
        }

        ArrayList<String> cars = new ArrayList<>();
        cars.add("volvo");
        cars.add("ferrari");
        cars.add("ford");
        cars.add("nissan");
        System.out.println(cars.get(1));
        System.out.println(cars);
        cars.set(3,"chevrolet");
        System.out.println(cars);
        cars.remove(0);
        System.out.println(cars);

        // Map example fixed (antes: Map diccionario = new HasMap();)
        //Map<String, String> diccionario = new HashMap<>();

        for (int i = 0; i < cars.size(); i++){
            System.out.println(cars.get(i));
        }
        //llamada de la funcion "sumar"
        int resultado = sumar(10,10);
        System.out.println(resultado);
    }
    
}