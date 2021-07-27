import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, E;
    static int order = 1;
    static ArrayList[] graph;
    static int[] visit;
    static boolean[] djj;

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
        djj = new boolean[N + 1];

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i < N + 1; i++) {
            if (visit[i] == 0) {
                dfs(1, true, 0);
            }
        }

        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (int i = 1; i < N + 1; i++) {
            if (djj[i]) {
                cnt++;
                sb.append(i).append(" ");
            }
        }

        System.out.println(cnt + "\n" + sb.toString());
    }

    static int dfs(int n, boolean isRoot, int parent) {
        visit[n] = order++;
        int retVal = visit[n];
        int child = 0;

        for (int i = 0; i < graph[n].size(); i++) {
            int next = (int) graph[n].get(i);

            // 이 전의 node 방문 x
            if (next == parent) {
                continue;
            }
            // 처음 왔으면
            if (visit[next] == 0) {
                // root일때 자식 수 계산
                child++;
                // dfs 진행
                int low = dfs(next, false, n);
                // 순환하지 않으면, low가 visit와 같은 경우 = 마지막 노드일 경우
                if (!isRoot && low >= visit[n]) {
                    djj[n] = true;
                }
                // 단절점이 아니어도 이전에 방문한 위치를 return 해야함
                retVal = Math.min(retVal, low);
            } else {
                // 이미 방문했다면 방문 위치 중 최소값 넘겨준다.
                retVal = Math.min(retVal, visit[next]);
            }
        }
        if (isRoot && child >= 2) {
            djj[n] = true;
        }
        return retVal;
    }
}
