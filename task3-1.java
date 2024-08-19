//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  public Main() {
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println(removeDuplicates(scanner.nextLine().split("")));
  }

  public static List<Integer> removeDuplicates(String[] input) {
    int[] uniqueArray = Arrays.stream(input).mapToInt(Integer::parseInt).distinct().toArray();
    return Arrays.stream(uniqueArray).boxed().toList();
  }
}
