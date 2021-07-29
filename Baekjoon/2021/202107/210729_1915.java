import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        dp = new int[N + 1][M + 1];

        for (int i = 1; i < N + 1; i++) {
            String s = br.readLine();
            for (int j = 1; j < M + 1; j++) {
                dp[i][j] = Integer.parseInt(String.valueOf(s.charAt(j - 1)));
            }
        }
        int ans = 0;
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < M + 1; j++) {
                if (dp[i][j] != 0) {
                    int tmp = dp[i - 1][j - 1];
                    tmp = Math.min(tmp, dp[i][j - 1]);
                    tmp = Math.min(tmp, dp[i - 1][j]);
                    dp[i][j] = tmp + 1;
                    ans = Math.max(ans, dp[i][j]);
                }
            }
        }
        System.out.println(ans * ans);
    }
}
