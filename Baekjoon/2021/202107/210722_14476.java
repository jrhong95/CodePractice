package P_14476;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] nums = new long[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        long[] lToR = new long[n];
        lToR[0] = nums[0];
        long[] rToL = new long[n];
        rToL[n - 1] = nums[n - 1];

        for (int i = 1; i < n; i++) {
            lToR[i] = gcd(lToR[i - 1], nums[i]);
        }
        for (int i = n - 2; i > -1; i--) {
            rToL[i] = gcd(rToL[i + 1], nums[i]);
        }

        long K = -1, max = 0;
        for (int i = 0; i < n; i++) {
            long gcd = 0;
            if (i == 0) {
                gcd = rToL[i + 1];
            } else if (i == n - 1) {
                gcd = lToR[i - 1];
            } else {
                gcd = gcd(lToR[i - 1], rToL[i + 1]);
            }
            if (nums[i] % gcd != 0) {
                if (nums[i] > K) {
                    K = nums[i];
                    max = gcd;
                }
            }
        }
        System.out.println(K == -1 ? -1 : max + " " + K);
    }

    // gcd(a, b) == gcd(b, a % b) , stop when a % b == 0
    static long gcd(long a, long b) {
        while (b != 0) {
            long r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
