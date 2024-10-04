package com.xzchto;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите значения через пробел:");
        String input = scanner.nextLine();
        String[] stringNumbers = input.trim().split("\\s+");

        int[] numbers = Arrays.stream(stringNumbers)
                .mapToInt(Integer::parseInt).toArray();
        int result = 0;
        for(int number : numbers) {
            result += number * number;
        }
        System.out.println(result);
    }
}
