import java.io.*;
import java.util.*;

public class Main {
    static int V, E;
    static int[] colors;
    static boolean flag;
    static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int i = 0; i < tc; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());

            colors = new int[V + 1];
            graph = new ArrayList<>();

            for (int j = 0; j < V + 1; j++) {
                graph.add(new ArrayList<Integer>());
            }

            for (int j = 0; j < E; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                graph.get(a).add(b);
                graph.get(b).add(a);
            }
            flag = false;

            for (int j = 1; j < V + 1; j++) {
                if (colors[j] == 0) {
                    dfs(j, 1);
                    if (flag)
                        break;
                }
            }
            System.out.println(flag ? "NO" : "YES");
        }
    }

    static void dfs(int start, int color) {
        colors[start] = color;

        graph.get(start).forEach(nextNum -> {
            if (colors[nextNum] == color) {
                flag = true;
            }

            if (colors[nextNum] == 0) {
                dfs(nextNum, -color);
            }
        });
    }
}