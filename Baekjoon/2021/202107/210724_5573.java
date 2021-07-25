import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R, C, N;
    static int[][] map, dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        dp = new int[R + 1][C + 1];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][0] = N - 1;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {

                dp[i + 1][j] += dp[i][j] / 2;
                dp[i][j + 1] += dp[i][j] / 2;

                if (dp[i][j] % 2 == 1) { // 현재 위치가 홀수인 경우
                    if (map[i][j] == 1) { // 오른쪽 부터 갈 경우
                        dp[i][j + 1] += 1;
                    } else { // 아래쪽 부터 갈 경우
                        dp[i + 1][j] += 1;
                    }

                    map[i][j] = (map[i][j] + 1) % 2;
                }
            }
        }
        move();
    }

    static void move() {
        int r = 0, c = 0;
        while (r < R && c < C) {
            if (map[r][c] == 0) { // 아래로
                map[r][c] = 1;
                r++;
            } else {
                map[r][c] = 0;
                c++;
            }
        }
        System.out.println((r + 1) + " " + (c + 1));
    }
}
