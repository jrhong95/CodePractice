import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static ArrayList[] tree;
    static int[][] parent;
    static int[] depth;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        K = 0; // 공간 복잡도를 위한 K계산.
        for (int i = 1; i <= N; i *= 2) { // K를 넉넉히 잡아도 문제 없다. ex) K=17
            K++;
        }

        tree = new ArrayList[N + 1];
        depth = new int[N + 1];
        parent = new int[K][N + 1];

        for (int i = 0; i < N + 1; i++) {
            tree[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            tree[a].add(b);
            tree[b].add(a);
        }

        dfs(1, 1);
        fillParent();
        int tc = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < tc; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            sb.append(lca(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()))).append("\n");
        }
        System.out.println(sb.toString());
    }

    static void fillParent() {
        for (int i = 1; i < K; i++) {
            for (int j = 1; j < N + 1; j++) {
                parent[i][j] = parent[i - 1][parent[i - 1][j]];
            }
        }
    }

    static int lca(int a, int b) {
        if (depth[a] < depth[b]) { // a가 더 깊게 만들어 준다.
            int tmp = a;
            a = b;
            b = tmp;
        }

        // 더 깊은 a를 2^K만큼 올려서 depth 맞추기
        for (int i = K - 1; i >= 0; i--) {
            if (Math.pow(2, i) <= depth[a] - depth[b]) {
                a = parent[i][a];
            }
        }

        // depth를 맞췄는데 같은 노드일 경우
        if (a == b) {
            return a;
        }
        // 공통 조상이 바로 아래까지 depth 올린다.
        // 최악의 경우 N이 편향되어있기 때문에 2^K-1부터 탐색한다
        for (int i = K - 1; i >= 0; i--) {
            if (parent[i][a] != parent[i][b]) {
                a = parent[i][a];
                b = parent[i][b];
            }
        }
        return parent[0][a];
    }

    static void dfs(int n, int dep) {
        depth[n] = dep;

        for (int i = 0; i < tree[n].size(); i++) {
            int next = (int) tree[n].get(i);

            if (depth[next] == 0) {
                dfs(next, dep + 1);
                parent[0][next] = n;
            }
        }
    }
}
