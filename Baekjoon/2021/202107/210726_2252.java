import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static int[] indegree;
    static ArrayList[] graph;
    static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        indegree = new int[N + 1];
        graph = new ArrayList[N + 1];

        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            indegree[b]++;
        }

        queue = new LinkedList<>();
        for (int i = 1; i < N + 1; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }
        StringBuilder sb = new StringBuilder();

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            sb.append(cur).append(" ");

            graph[cur].forEach(x -> {
                int next = (int) x;
                indegree[next]--;
                if (indegree[next] == 0)
                    queue.add(next);
            });
        }

        System.out.println(sb.toString());
    }
}
