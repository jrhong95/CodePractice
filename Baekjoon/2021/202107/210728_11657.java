import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static int N, M;
    static ArrayList<Node> graph;
    static long[] dist;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        dist = new long[N + 1];
        graph = new ArrayList<>();

        for (int i = 2; i < N + 1; i++) {
            dist[i] = INF;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.add(new Node(a, b, c));
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                Node now = graph.get(j);

                if (dist[now.start] == INF) {
                    continue;
                }
                dist[now.dest] = Math.min(dist[now.dest], dist[now.start] + now.cost);
            }
        }

        boolean isCycle = false;

        for (int j = 0; j < M; j++) {
            Node now = graph.get(j);
            if (dist[now.start] == INF) {
                continue;
            }

            if (dist[now.dest] > dist[now.start] + now.cost) {
                isCycle = true;
                break;
            }
        }

        if (isCycle) {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 2; i < N + 1; i++) {
                dist[i] = dist[i] == INF ? -1 : dist[i];
                sb.append(dist[i] + "\n");
            }
            System.out.println(sb.toString());
        }
    }
}

class Node {
    int start;
    int dest;
    int cost;

    public Node(int start, int dest, int cost) {
        this.start = start;
        this.dest = dest;
        this.cost = cost;
    }
}
