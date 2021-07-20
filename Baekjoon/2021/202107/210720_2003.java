import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N, M;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);

        nums = new int[N];
        String[] token = br.readLine().split(" ");

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(token[i]);
        }

        int left = 0;
        int right = 1;
        int answer = 0;

        while (right <= N) {
            int sum = 0;

            for (int i = left; i < right; i++) {
                sum += nums[i];
            }

            if (sum > M) {
                left++;
            } else if (sum == M) {
                answer++;
                right++;
            } else {
                right++;
            }
        }
        System.out.println(answer);
        br.close();
    }
}
