package P_9202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static Node root;

    static int scoreSum, count;
    static String maxString;
    static int[] score = { 0, 0, 0, 1, 1, 2, 3, 5, 11 };

    static char[][] map;
    static boolean[][] visited;
    static StringBuilder sb;

    static int[] mc = { 1, 1, 1, 0, 0, -1, -1, -1 };
    static int[] mr = { 1, 0, -1, 1, -1, 1, 0, -1 };

    public static void main(String[] args) throws IOException {
        root = new Node();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            insert(br.readLine());
        }

        br.readLine();

        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            map = new char[4][4];

            for (int j = 0; j < 4; j++) {
                String s = br.readLine();
                for (int k = 0; k < 4; k++) {
                    map[j][k] = s.charAt(k);
                }
            }

            visited = new boolean[4][4];
            sb = new StringBuilder();
            count = 0;
            scoreSum = 0;
            maxString = "";

            for (int r = 0; r < 4; r++) {
                for (int c = 0; c < 4; c++) {
                    if (root.hasChild(map[r][c])) {
                        dfs(r, c, 1, root.getChild(map[r][c]));
                    }
                }
            }
            root.clearHit();
            System.out.println(scoreSum + " " + maxString + " " + count);
            if (i == n) {
                break;
            } else {
                br.readLine();
            }
        }
    }

    static int ctoi(char c) {
        return c - 'A';
    }

    static void insert(String word) {
        Node cur = root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (cur.getChild(c) == null) {
                cur.child[ctoi(c)] = new Node();
            }

            cur = cur.child[ctoi(c)];
        }
        cur.isEnd = true;
    }

    static int compare(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return 1;
        } else if (s1.length() < s2.length()) {
            return -1;
        } else {
            return s2.compareTo(s1);
        }
    }

    static void dfs(int r, int c, int length, Node cur) {
        // 1. 체크인
        visited[r][c] = true;
        sb.append(map[r][c]);

        // 2. 목적지인가
        if (cur.isEnd && !cur.isHit) {
            cur.isHit = true;

            String word = sb.toString();
            scoreSum += score[word.length()];
            count += 1;
            if (compare(maxString, word) < 0) {
                maxString = word;
            }
        }

        // 3. 갈 수 있는 곳 순회
        for (int i = 0; i < 8; i++) {
            int tr = r + mr[i];
            int tc = c + mc[i];
            // 4. 갈 수 있는가? 방문x, 경계, 자식을 갖는지
            if (0 <= tr && tr < 4 && 0 <= tc && tc < 4) {
                if (!visited[tr][tc] && cur.hasChild(map[tr][tc])) {
                    // 5. 간다.
                    dfs(tr, tc, length + 1, cur.getChild(map[tr][tc]));
                }
            }
        }
        // 6. 체크아웃
        visited[r][c] = false;
        sb.deleteCharAt(length - 1);
    }
}

class Node {
    Node[] child;
    boolean isEnd, isHit;

    public Node() {
        child = new Node[26];
        isEnd = false;
    }

    public void clearHit() {
        isHit = false;

        for (int i = 0; i < child.length; i++) {
            if (child[i] != null) {
                child[i].clearHit();
            }
        }
    }

    public Node getChild(char c) {
        return child[c - 'A'];
    }

    public boolean hasChild(char c) {
        return child[c - 'A'] != null;
    }
}