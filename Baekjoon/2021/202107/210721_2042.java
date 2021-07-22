import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M, K, S;
    static long[] nums, tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        nums = new long[N];

        for (int i = 0; i < N; i++) {
            nums[i] = Long.parseLong(br.readLine());
        }
        S = 1;
        while (S < N) {
            S *= 2;
        }
        tree = new long[S * 2];
        initBU();

        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) {
                // update
                updateBU(b, c);
            } else {
                // query
                // System.out.println(query(1, S, 1, b, c));
                System.out.println(queryBU(b, (int) c));
            }
        }
    }

    static void initBU() {
        // for 문으로 leaf 채움 S -> S * 2 - 1
        for (int i = 0; i < nums.length; i++) {
            tree[i + S] = nums[i];
        }
        // 내부노드 채운다
        for (int i = S - 1; i > 0; i--) {
            tree[i] = tree[i * 2] + tree[i * 2 + 1];
        }
    }

    static long query(int left, int right, int node, int queryLeft, int queryRight) {
        // 연관 없음 -> 결과에 영향 없는 값 return
        if (queryRight < left || queryLeft > right) {
            return 0;
        }
        // 판단 가능 -> 쿼리에 영향 줄 수 있는 값, 현재 노드의 값 return
        else if (queryLeft <= left && queryRight >= right) {
            return tree[node];
        }
        // 판단 불가 -> 자식에게 위임, 자식에서 올라온 합을 return
        else {
            int mid = (left + right) / 2;
            return query(left, mid, node * 2, queryLeft, queryRight)
                    + query(mid + 1, right, node * 2 + 1, queryLeft, queryRight);
        }
    }

    static void update(int left, int right, int node, int target, long diff) {
        // 연관 없음
        if (left > target || right < target) {
            return;
        }
        // 연관 있음 -> 현재 노드에 diff 반영
        else {
            tree[node] += diff;
            if (left != right) {
                int mid = (left + right) / 2;
                update(left, mid, node * 2, target, diff);
                update(mid + 1, right, node * 2 + 1, target, diff);
            }
        }
    }

    static long queryBU(int queryLeft, int queryRight) {
        // leaf Left, Right 설정
        int left = S + queryLeft - 1;
        int right = S + queryRight - 1;

        long sum = 0;
        while (left <= right) {
            // 좌측 노드가 홀수면 현재 노드값 사용하고 한칸 옆으로
            if (left % 2 == 1) {
                sum += tree[left++];
            }
            // 우측 노드가 짝수면 현재 노드값 사용하고 한칸 옆으로
            if (right % 2 == 0) {
                sum += tree[right--];
            }
            // 좌측, 우측 모두 부모 이동
            left /= 2;
            right /= 2;
        }

        return sum;
    }

    static void updateBU(int target, long value) {
        // leaf 에서 target 찾음
        int node = S + target - 1;
        tree[node] = value;

        // root까지 반복
        node /= 2;
        while (node > 0) {
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
            node /= 2;
        }
    }
}
