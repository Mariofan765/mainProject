package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {


  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println(reverseString(scanner.nextLine().split(" ")));
  }

  public static String reverseString(String[] input) {
    String[] reversed = new String[input.length];
    for (int i = 0; i < input.length; i++) {
      reversed[i] = input[input.length - i - 1];
    }
    return Arrays.toString(reversed);
  }
}