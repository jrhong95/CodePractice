import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] indegree, costs, answer;
    static ArrayList[] graph;
    static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        indegree = new int[N + 1];
        costs = new int[N + 1];
        answer = new int[N];
        graph = new ArrayList[N + 1];

        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i = 1; i < N + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            costs[i] = Integer.parseInt(st.nextToken());

            int n = Integer.parseInt(st.nextToken());
            while (n != -1) {
                graph[n].add(i);
                indegree[i]++;
                n = Integer.parseInt(st.nextToken());
            }
        }
        queue = new LinkedList<>();

        for (int i = 1; i < N + 1; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
                answer[i - 1] = costs[i];
            }
        }

        while (!queue.isEmpty()) {
            int now = queue.poll();

            graph[now].forEach(x -> {
                int next = (int) x;
                indegree[next]--;
                answer[next - 1] = Integer.max(answer[next - 1], answer[now - 1] + costs[next]);
                if (indegree[next] == 0) {
                    queue.add(next);
                }
            });
        }

        for (int n : answer) {
            System.out.println(n);
        }
    }
}
