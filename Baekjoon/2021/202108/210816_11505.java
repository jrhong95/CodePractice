import java.io.*;
import java.util.*;

public class Main {
    static final int div = 1_000_000_007;
    static int N, M, K, S;
    static long[] tree;
    static int[] nums;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        S = 1;
        while (S < N) {
            S *= 2;
        }
        tree = new long[2 * S];
        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        initTree();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == 1) {
                update(b, c);
            } else {
                sb.append(query(b, c)).append("\n");
            }
        }
        System.out.println(sb);
    }

    static void initTree() {
        int idx = 0;

        while (idx < nums.length) {
            tree[idx + S] = nums[idx];
            idx++;
        }

        for (int i = S + idx; i < tree.length; i++) {
            tree[i] = 1;
        }

        for (int i = S - 1; i > 0; i--) {
            tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % div;
        }
    }

    static long query(int queryLeft, int queryRight) {
        int left = S + queryLeft - 1;
        int right = S + queryRight - 1;

        long sum = 1;

        while (left <= right) {
            if (left % 2 == 1) {
                sum = (sum * tree[left++]) % div;
            }

            if (right % 2 == 0) {
                sum = (sum * tree[right--]) % div;
            }
            left /= 2;
            right /= 2;
        }
        return sum;
    }

    static void update(int target, int num) {
        int node = S + target - 1;
        tree[node] = num;

        node /= 2;
        while (node > 0) {
            tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % div;
            node /= 2;
        }
    }
}