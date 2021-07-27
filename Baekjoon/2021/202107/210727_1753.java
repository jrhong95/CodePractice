import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node> {

    int cost;
    int id;

    public Node(int cost, int id) {
        this.cost = cost;
        this.id = id;
    }

    @Override
    public int compareTo(Node n) {
        return this.cost - n.cost;
    }
}

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static int V, E;
    static int[] dist;
    static ArrayList[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        dist = new int[V + 1];
        graph = new ArrayList[V + 1];
        for (int i = 0; i < V + 1; i++) {
            dist[i] = INF;
            graph[i] = new ArrayList<Node>();
        }

        int start = Integer.parseInt(br.readLine());
        dist[start] = 0;

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(w, b));
        }
        dijkstra(new Node(0, start));

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < V + 1; i++) {
            if (dist[i] == INF) {
                sb.append("INF").append("\n");
            } else {
                sb.append(dist[i]).append("\n");
            }
        }
        System.out.print(sb.toString());
    }

    static void dijkstra(Node start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(start);

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (cur.cost > dist[cur.id]) {
                continue;
            }

            for (int i = 0; i < graph[cur.id].size(); i++) {
                Node next = (Node) graph[cur.id].get(i);

                if (dist[next.id] > cur.cost + next.cost) {
                    dist[next.id] = cur.cost + next.cost;
                    pq.add(new Node(dist[next.id], next.id));
                }
            }
        }
    }
}
