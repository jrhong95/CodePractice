import java.io.*;
import java.util.*;

class Edge {
    int dst, cost;

    public Edge(int dst, int cost) {
        this.dst = dst;
        this.cost = cost;
    }
}

public class Main {
    static int N, K;
    static int[] depth, distance;
    static int[][] parent;
    static ArrayList<ArrayList<Edge>> tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = 0;

        while (Math.pow(2, K) < N)
            K++;

        depth = new int[N + 1];
        distance = new int[N + 1];
        parent = new int[K][N + 1];
        tree = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            tree.get(a).add(new Edge(b, c));
            tree.get(b).add(new Edge(a, c));
        }
        dfs(1, 1, 0);
        fillParent();

        int tc = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < tc; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int root = lca(a, b);
            sb.append(distance[a] + distance[b] - 2 * distance[root]).append("\n");
        }
        System.out.println(sb);
    }

    static void dfs(int start, int cnt, int dist) {
        depth[start] = cnt;
        distance[start] = dist;

        tree.get(start).forEach(edge -> {
            if (depth[edge.dst] == 0) {
                dfs(edge.dst, cnt + 1, dist + edge.cost);
                parent[0][edge.dst] = start;
            }
        });
    }

    static void fillParent() {
        for (int k = 1; k < K; k++) {
            for (int v = 1; v < N + 1; v++) {
                parent[k][v] = parent[k - 1][parent[k - 1][v]];
            }
        }
    }

    static int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int tmp = a;
            a = b;
            b = tmp;
        }

        for (int i = K - 1; i >= 0; i--) {
            if (Math.pow(2, i) <= depth[a] - depth[b]) {
                a = parent[i][a];
            }
        }

        if (a == b) {
            return a;
        }

        for (int i = K - 1; i >= 0; i--) {
            if (parent[i][a] != parent[i][b]) {
                a = parent[i][a];
                b = parent[i][b];
            }
        }
        return parent[0][a];
    }
}
