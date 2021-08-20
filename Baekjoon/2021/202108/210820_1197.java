import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
    int start, end, cost;

    public Edge(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge e) {
        return this.cost - e.cost;
    }
}

public class Main {
    static int V, E;
    static int[] set;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        set = new int[V + 1];
        for (int i = 1; i <= V; i++) {
            set[i] = i;
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            pq.add(new Edge(a, b, c));
        }

        long cost = 0;
        int count = 0;
        while (!pq.isEmpty()) {
            if (count == V - 1) {
                break;
            }
            Edge cur = pq.poll();

            if (find(cur.start) != find(cur.end) && cur.start != cur.end) {
                union(cur.start, cur.end);
                cost += cur.cost;
            }
        }
        System.out.println(cost);
    }

    static int find(int a) {
        if (set[a] == a) {
            return a;
        }
        return set[a] = find(set[a]);
    }

    static void union(int a, int b) {
        set[find(b)] = find(a);
    }
}
