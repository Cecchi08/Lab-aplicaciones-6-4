import java.util.Scanner;
import java.util.HashMap;

public class CodigoCesar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el mensaje a encriptar: ");
        String msj = scanner.nextLine();
        String encrypted_msj = "";

        // Diccionario de índices y letras
        HashMap<Integer, Character> diccionarioIndiceNumero = new HashMap<>();
        for (int i = 1; i <= 26; i++) {
            diccionarioIndiceNumero.put(i, (char) (i + 96));  // Letras minúsculas
            diccionarioIndiceNumero.put(i + 26, (char) (i + 64));  // Letras mayúsculas
        }

        // Diccionario de letras y sus índices
        HashMap<Character, Integer> diccionarioNumeroIndice = new HashMap<>();
        for (int i = 1; i <= 26; i++) {
            diccionarioNumeroIndice.put((char) (i + 96), i);  // Letras minúsculas
            diccionarioNumeroIndice.put((char) (i + 64), i + 26);  // Letras mayúsculas
        }

        // Encriptación
        for (int i = 0; i < msj.length(); i++) {
            char c = msj.charAt(i);
            if (c != ' ') {  // Ignorar espacios
                int indiceActual = diccionarioNumeroIndice.get(c);

                // Ajustes de índice según el patrón
                if (indiceActual == 24) indiceActual = 1;
                else if (indiceActual == 25) indiceActual = 2;
                else if (indiceActual == 26) indiceActual = 3;
                else if (indiceActual == 50) indiceActual = 27;
                else if (indiceActual == 51) indiceActual = 28;
                else if (indiceActual == 52) indiceActual = 29;

                // Desplazamiento
                int indiceEncriptado = indiceActual + 3;
                if (indiceEncriptado > 52) {
                    indiceEncriptado -= 52;  // Asegura que no se desborde
                }

                // Obtener la letra encriptada
                encrypted_msj += diccionarioIndiceNumero.get(indiceEncriptado);
            }
        }

        System.out.println("El mensaje encriptado es: " + encrypted_msj);
        scanner.close();
    }
}
