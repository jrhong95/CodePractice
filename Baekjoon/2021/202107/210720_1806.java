import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    final static int MAX_VALUE = 1000000;
    static int N, M;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        nums = new int[N + 1];

        s = br.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(s[i]);
        }

        int left = 0, right = 0, answer = MAX_VALUE;
        int sum = nums[0];
        while (right < N) {
            if (sum >= M) {
                answer = Integer.min(answer, right - left + 1);
                sum -= nums[left++];
            } else {
                sum += nums[++right];
            }
        }

        System.out.println(answer != MAX_VALUE ? answer : 0);
    }
}
