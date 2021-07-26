import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node {
    String num;
    int count;

    public Node(String num, int count) {
        this.num = num;
        this.count = count;
    }
}

public class Main {
    static int max = -1, size;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String n = st.nextToken();
        size = n.length();
        int k = Integer.parseInt(st.nextToken());
        bfs(n, k);
        System.out.println(max);
    }

    static void bfs(String s, int k) {
        Queue<Node> queue = new LinkedList<>();
        boolean[][] visited = new boolean[1000001][k + 1];
        queue.add(new Node(s, 0));
        visited[Integer.parseInt(s)][0] = true;

        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            String num = cur.num;
            int count = cur.count;

            if (count == k) {
                max = Integer.max(max, Integer.parseInt(num));
            } else {
                for (int i = 0; i < size - 1; i++) {
                    for (int j = i + 1; j < size; j++) {
                        if (i == 0 && num.charAt(j) == '0') {
                            continue;
                        }
                        String next = swap(num, i, j);
                        int intNext = Integer.parseInt(next);

                        if (!visited[intNext][count + 1]) {
                            visited[intNext][count + 1] = true;
                            queue.add(new Node(next, count + 1));
                        }
                    }
                }
            }

        }
    }

    static String swap(String num, int i, int j) {
        String[] numArray = strToArray(num);
        String tmp = numArray[i];
        numArray[i] = numArray[j];
        numArray[j] = tmp;
        return arrayToString(numArray);
    }

    static String arrayToString(String[] s) {
        StringBuilder sb = new StringBuilder();
        for (String n : s) {
            sb.append(n);
        }
        return sb.toString();
    }

    // toCharArray가 있음;;
    static String[] strToArray(String s) {
        String[] arr = new String[s.length()];
        for (int i = 0; i < s.length(); i++) {
            arr[i] = String.valueOf(s.charAt(i));
        }
        return arr;
    }
}
