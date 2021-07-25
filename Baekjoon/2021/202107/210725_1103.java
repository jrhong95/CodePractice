import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean flag = false;
    static int R, C, answer = 0;
    static int[][] map, dp;
    static boolean[][] visited;
    static int[] mr = { 1, -1, 0, 0 };
    static int[] mc = { 0, 0, -1, 1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new int[R][C];
        dp = new int[R][C];
        visited = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            String s = br.readLine();
            for (int j = 0; j < C; j++) {
                String n = String.valueOf(s.charAt(j));
                if (n.equals("H")) {
                    n = "0";
                }
                map[i][j] = Integer.parseInt(n);
            }
        }
        int ans = dfs(0, 0);
        if (flag) {
            System.out.println(-1);
        } else {
            System.out.println(ans + 1);
        }
    }

    static int dfs(int r, int c) {
        if (visited[r][c]) {
            flag = true;
            return 0;
        }

        visited[r][c] = true;

        for (int i = 0; i < 4; i++) {
            int cr = r + mr[i] * map[r][c];
            int cc = c + mc[i] * map[r][c];

            if (cr < 0 || R <= cr || cc < 0 || C <= cc || map[cr][cc] == 0) {
                continue;
            }

            dp[r][c] = Integer.max(dp[r][c], dfs(cr, cc) + 1);
        }
        visited[r][c] = false;
        return dp[r][c];
    }
}
