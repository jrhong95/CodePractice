import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static final int MAX = (int) 1e9;
    static int N, M, K;
    static int[][] dp;
    static StringBuilder sb;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();
        dp = new int[N + M + 1][N + M + 1];
        sb = new StringBuilder();

        if (K > combination(N + M, M)) {
            System.out.println(-1);
        } else {
            findWord(N, M, K);
            System.out.println(sb.toString());
        }
    }

    static void findWord(int aCount, int zCount, int rank) {
        int totalCount = aCount + zCount;

        if (totalCount == 0) {
            return;
        } else if (zCount == 0) {
            sb.append("a");
            findWord(aCount - 1, zCount, rank);
        } else if (aCount == 0) {
            sb.append("z");
            findWord(aCount - 1, zCount - 1, rank);
        } else {
            int left = combination(totalCount - 1, zCount);

            if (left < rank) {
                sb.append("z");
                findWord(aCount, zCount - 1, rank - left);
            } else {
                sb.append("a");
                findWord(aCount - 1, zCount, rank);
            }
        }
    }

    static int combination(int n, int r) {
        if (dp[n][r] == 0) {
            if (n == r || r == 0) {
                dp[n][r] = 1;
            } else {
                dp[n][r] = Math.min(MAX, combination(n - 1, r - 1) + combination(n - 1, r));
            }
        }
        return dp[n][r];
    }
}
