import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static final int INF = Integer.MAX_VALUE;
    static int[] mr = { -1, 1, 0, 0 };
    static int[] mc = { 0, 0, -1, 1 };

    static int R, C;
    static Node[][] map;
    static long[][] dist;
    static boolean flag;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            C = Integer.parseInt(st.nextToken());
            R = Integer.parseInt(st.nextToken());
            flag = false;
            if (R == 0 && C == 0) {
                break;
            }

            map = new Node[R][C];
            dist = new long[R][C];
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    map[i][j] = new Node(i, j, 1);
                    dist[i][j] = INF;
                }
            }
            dist[0][0] = 0;

            int e = Integer.parseInt(br.readLine());
            for (int i = 0; i < e; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                map[y][x].isTomb = true;
            }

            int hole = Integer.parseInt(br.readLine());
            for (int i = 0; i < hole; i++) {
                st = new StringTokenizer(br.readLine());
                int x1 = Integer.parseInt(st.nextToken());
                int y1 = Integer.parseInt(st.nextToken());
                int x2 = Integer.parseInt(st.nextToken());
                int y2 = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());

                map[y1][x1].setHolePoint(y2, x2, cost);
            }

            bellmanFord();

            if (flag) {
                sb.append("Never\n");
            } else {
                if (dist[R - 1][C - 1] == INF) {
                    sb.append("Impossible\n");
                } else {
                    sb.append(dist[R - 1][C - 1] + "\n");
                }
            }
        }

        System.out.println(sb.toString());
    }

    static void bellmanFord() {
        for (int n = 0; n < R * C - 1; n++) {
            for (int i = 0; i < R; i++) { // r
                for (int j = 0; j < C; j++) { // c
                    Node cur = map[i][j];

                    if (cur.isTomb || (i == R - 1 && j == C - 1) || dist[i][j] == INF) {
                        continue;
                    }

                    if (cur.isHole) {
                        dist[cur.holeR][cur.holeC] = Math.min(dist[cur.holeR][cur.holeC], dist[i][j] + cur.cost);
                    } else {
                        for (int t = 0; t < 4; t++) {
                            int cr = i + mr[t];
                            int cc = j + mc[t];
                            if (cr < 0 || cr >= R || cc < 0 || cc >= C) {
                                continue;
                            }
                            Node next = map[cr][cc];
                            if (next.isTomb) {
                                continue;
                            }

                            dist[cr][cc] = Math.min(dist[cr][cc], dist[i][j] + cur.cost);
                        }
                    }

                }
            }
        }

        for (int i = 0; i < R; i++) { // r
            for (int j = 0; j < C; j++) { // c
                Node cur = map[i][j];

                if (cur.isTomb || (i == R - 1 && j == C - 1) || dist[i][j] == INF) {
                    continue;
                }

                if (cur.isHole) {
                    if (dist[cur.holeR][cur.holeC] > dist[i][j] + cur.cost) {
                        flag = true;
                        return;
                    }

                } else {
                    for (int t = 0; t < 4; t++) {
                        int cr = i + mr[t];
                        int cc = j + mc[t];

                        if (cr < 0 || cr >= R || cc < 0 || cc >= C) {
                            continue;
                        }

                        Node next = map[cr][cc];
                        if (next.isTomb) {
                            continue;
                        }

                        if (dist[cr][cc] > dist[i][j] + cur.cost) {
                            flag = true;
                            return;
                        }
                    }
                }

            }
        }
    }
}

class Node {
    int r, c;
    int cost;
    boolean isTomb, isHole;
    int holeR, holeC;

    public Node(int r, int c, int cost) {
        super();
        this.r = r;
        this.c = c;
        this.cost = cost;
    }

    public void setHolePoint(int r, int c, int cost) {
        this.holeR = r;
        this.holeC = c;
        this.isHole = true;
        this.cost = cost;
    }
}
