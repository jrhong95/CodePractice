import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] set;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        set = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            set[i] = i;
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            pq.add((new Edge(a, b, c)));
        }

        int cnt = 0, answer = 0;
        while (!pq.isEmpty()) {
            Edge now = pq.poll();

            if (cnt == N - 1) {
                break;
            }
            if (now.start == now.end || find(now.start) == find(now.end)) {
            } else {
                union(now.start, now.end);
                answer += now.cost;
                cnt++;
            }
        }
        System.out.println(answer);
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

class Edge implements Comparable<Edge> {
    int start;
    int end;
    int cost;

    public Edge(int start, int end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return this.cost - o.cost;
    }
}
