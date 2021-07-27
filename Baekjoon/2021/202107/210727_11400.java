import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge> {
    int start;
    int end;

    public Edge(int start, int end) {
        if (start > end) {
            this.start = end;
            this.end = start;
        } else {
            this.start = start;
            this.end = end;
        }
    }

    @Override
    public int compareTo(Edge e) {
        if (this.start == e.start) {
            return this.end - e.end;
        }
        return this.start - e.start;
    }
}

public class Main {
    static int N, E;
    static int order = 1;
    static ArrayList[] graph;
    static int[] visit;
    static ArrayList<Edge> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        visit = new int[N + 1];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        answer = new ArrayList<>();
        for (int i = 1; i < N + 1; i++) {
            if (visit[i] == 0) {
                dfs(1, 0);
            }
        }

        StringBuilder sb = new StringBuilder();
        int cnt = 0;

        Collections.sort(answer);
        System.out.println(answer.size());
        for (Edge edge : answer) {
            System.out.println(edge.start + " " + edge.end);
        }
    }

    static int dfs(int id, int parent) {
        visit[id] = order++;
        int retVal = visit[id];

        // 모든 자식 그래프 탐색
        for (int i = 0; i < graph[id].size(); i++) {
            int next = (int) graph[id].get(i);

            // 이 전의 node 방문 x
            if (next == parent) {
                continue;
            }
            // 처음 왔으면
            if (visit[next] == 0) {
                // root일때 자식 수 계산
                // dfs 진행
                int low = dfs(next, id);
                // 순환하지 않으면 -> 단절점
                if (low > visit[id]) {
                    answer.add(new Edge(id, next));
                }
                // 단절점이 아니어도 이전에 방문한 위치를 return 해야함
                retVal = Math.min(retVal, low);
            } else {
                // 이미 방문했다면 방문 위치 중 최소값 넘겨준다.
                retVal = Math.min(retVal, visit[next]);
            }
        }
        return retVal;
    }
}
