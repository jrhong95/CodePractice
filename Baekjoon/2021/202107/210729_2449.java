import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[][] dp;
    static int[] bulbs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        bulbs = new int[N];
        dp = new int[N][N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            bulbs[i] = Integer.parseInt(st.nextToken());
        }

        divideConquer(0, N - 1);
        System.out.println(dp[0][N - 1]);
    }

    static int divideConquer(int start, int end) {
        // 1. 더 이상 분할정복 할 수 없을 경우
        if (start == end) {
            return 0;
        }
        // 2. 이미 계산 했을 경우
        if (dp[start][end] != 0) {
            return dp[start][end];
        }

        int retVal = Integer.MAX_VALUE;

        int left, right;
        for (int i = start; i < end; i++) {
            // 분할 정복
            left = divideConquer(start, i);
            right = divideConquer(i + 1, end);

            // 양쪽의 색이 같은 경우
            if (bulbs[start] == bulbs[i + 1]) {
                retVal = Math.min(retVal, left + right);
            } else {
                // 같지 않은 경우 변경횟수 +1 해준다.
                retVal = Math.min(retVal, left + right + 1);
            }
        }

        return dp[start][end] = retVal;
    }
}
