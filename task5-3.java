import java.util.Scanner;

public class Game {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();

        long tanyaSticks = 0;
        boolean isTanyaTurn = true;

        while (n > 0) {
            if (isTanyaTurn) {
                // Ход Тани
                if (n % 2 == 0) {
                    tanyaSticks += 1;
                    n -= 1;
                } else {
                    tanyaSticks += 1;
                    n -= 1;
                }
            } else {
                if (n % 2 == 0) {
                    n /= 2;
                } else {
                    n -= 1;
                }
            }
            isTanyaTurn = !isTanyaTurn;

        System.out.println(tanyaSticks);
    }
}
