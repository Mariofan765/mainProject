package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {


  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Введите первый параметр: ");
    int m = scanner.nextInt();
    System.out.println("Введите второй параметр: ");
    int n = scanner.nextInt();
    System.out.println(countUniquePaths(m, n));
  }

  public static int countUniquePaths(int m, int n) {
    int[][] dp = new int[m][n];

    for (int i = 0; i < m; i++) {
      dp[i][0] = 1;
    }
    for (int j = 0; j < n; j++) {
      dp[0][j] = 1;
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
      }
    }

    return dp[m - 1][n - 1];
  }
}