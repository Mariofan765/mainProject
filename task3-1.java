import java.util.Scanner;
import java.util.ArrayList;

public class PrimeFactorization {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите число для разложения на простые множители: ");
        int number = scanner.nextInt();

        ArrayList<Integer> factors = primeFactors(number);
        System.out.println("Простые множители числа " + number + ": " + factors);
    }

    public static ArrayList<Integer> primeFactors(int n) {
        ArrayList<Integer> factors = new ArrayList<>();
        while (n % 2 == 0) {
            factors.add(2);
            n /= 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if (n > 2) {
            factors.add(n);
        }
        return factors;
    }
}
