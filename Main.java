
public class Main {
    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {

        // EXERCICIO 2
//        for(int i = 2; i <= 20; i++) {
//
//            if (i % 2 == 0) {
//                System.out.println(i);
//            }
//        }


        // EXERCICIO 3
//        Scanner scanner = new Scanner(System.in);
//        System.out.print("Digite um número: ");
//                int numero = scanner.nextInt();
//        if(numero % 2 == 0){
//            System.out.println("O número é par!");
//        }
//        else {
//            System.out.println("O número é ímpar!");
//        }


        // EXERCICIO 4
//        Scanner scanner = new Scanner(System.in);
//
//        System.out.println("Digite o primeiro número: ");
//        int num1 = scanner.nextInt();
//
//        System.out.println("Digite outro número: ");
//        int num2 = scanner.nextInt();
//
//        if (num1 > num2) {
//            System.out.printf("Maior número: %d", num1);
//        } else {
//            System.out.printf("Maior número: %d", num2);
//        }


        // EXERCICIO 5

//        int regressivo  = 10;

//        while(regressivo > 0){
//          regressivo --;
//          System.out.println(regressivo);       
//        }

        // EXERCICIO 6

        // Scanner scanner = new Scanner(System.in);

        // int soma = 0;

        // for (int i = 0; i < 5; i++) {
        //     System.out.println("Digite um número: ");
        //     int numero = scanner.nextInt();
        //     soma += numero;
        // }

        // EXERCICIO 7
       
        // Scanner scanner = new Scanner(System.in); 
        
        // System.out.print("Digite um número: "); 
        // int num = scanner.nextInt(); 
        
        // for(int i = 1; i <= 10; i++) { 
        //         int resultado = num * i; 
        //         System.out.printf("%d x %d = %d\n", num, i, resultado); 
        // }

        // EXERCICIO 8 

        String palavra = "programacao";
        int contador = 0;

        for(int i = 0; i < palavra.length(); i++) {

                char letra = palavra.charAt(i);

                if(letra == 'a'|| letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u'){
                        contador++;
                }       
        }
        System.out.println("Quantidade de vogais: " + contador);
        


        
    }        
}