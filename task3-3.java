import java.util.Scanner;

public class LCMCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите количество чисел: ");
        int n = scanner.nextInt();
        int[] numbers = new int[n];

        System.out.println("Введите " + n + " целых числа:");
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }

        int lcm = findLCM(numbers);
        System.out.println("Наименьшая общая кратная (НОК) для введённых чисел: " + lcm);
    }

    public static int findLCM(int[] numbers) {
        int lcm = numbers[0];
        for (int i = 1; i < numbers.length; i++) {
            lcm = lcm(lcm, numbers[i]);
        }
        return lcm;
    }

    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
