package P_11051;

import java.util.Scanner;

public class Main {
    static int[][] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        dp = new int[N + 1][N + 1];
        System.out.println(combination(N, K));
    }

    static int combination(int n, int r) {
        if (dp[n][r] == 0) {
            if (n == r || r == 0) {
                dp[n][r] = 1;
            } else {
                dp[n][r] = (combination(n - 1, r - 1) + combination(n - 1, r)) % 10007;
            }
        }
        return dp[n][r];
    }
}
