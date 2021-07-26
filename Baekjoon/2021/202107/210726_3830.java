import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            if (N == 0 && M == 0) {
                break;
            }

            parent = new int[N + 1][2]; // 0: 부모 집합 1: 부모와의 무게 차이
            for (int i = 0; i < N + 1; i++) {
                parent[i][0] = i;
                parent[i][1] = 0;
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                String flag = st.nextToken();

                if (flag.equals("!")) {
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());
                    int c = Integer.parseInt(st.nextToken());
                    union(a, b, c);
                } else {
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());

                    if (find(a) != find(b)) {
                        sb.append("UNKNOWN").append("\n");
                    } else {
                        sb.append(parent[b][1] - parent[a][1]).append("\n");
                    }
                }
            }
        }
        System.out.println(sb.toString());
    }

    static int find(int a) {
        if (parent[a][0] == a) {
            return a;
        }
        int pId = find(parent[a][0]);
        parent[a][1] += parent[parent[a][0]][1];
        return parent[a][0] = pId;
    }

    static void union(int a, int b, int c) {
        int pa = find(a);
        int pb = find(b);

        if (pa != pb) {
            parent[pb][1] = parent[a][1] - parent[b][1] + c;
            parent[pb][0] = pa;
        }
    }
}
