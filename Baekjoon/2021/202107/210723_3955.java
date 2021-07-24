import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static final int MAX = (int) 1e9;

    public static void main(String[] args) throws IOException {

        // X : 인당 나눠줄 사탕 수
        // Y : 사탕 봉지 수
        // A * x + 1 = B * Y => -Ax + By = 1 => A(-x) + By = 1
        // x > 0 && 0 < y <= 10 ** 9

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            // D = gcd(A, B)
            // Ax + By = C 일 때 C % D == 0 이어야 해를 갖는다. 베주항등식. so, D == 1 이어야 해가 있다.
            EGResult result = extendedGcd(a, b);
            if (result.r != 1) {
                System.out.println("IMPOSSIBLE");
            } else {
                long left = (result.t - MAX) / a;
                long tmpX = (long) Math.ceil((double) -result.s / a) - 1;
                long tmpY = (long) Math.ceil((double) result.t / a) - 1;
                long K = Math.min(tmpX, tmpY);

                if (left > K) {
                    System.out.println("IMPOSSIBLE");
                } else {
                    System.out.println(result.t - a * K);
                }
            }
            // x0 = s * C/D
            // y0 = t * C/D
            // x = x0 + B/D * K
            // y = y0 - A/D * K

            // x < 0 (x == -x 이기 때문)
            // x0 + B * K < 0 ( x = x0 + B/D * K 인데 D = 1 이므로 x0->x 라 할 때 성립)
            // K < -x0 / B
            // 0 < y <= 10**9
            // 0 < y0 - A * K <= 10**9
            // -y0 < -A * K <= 10**9 - y0
            // (y0 - 10**9) / A <= K < y0 / A
            // K < -x0 / B
            // y0/A 와 -x0/B 중에 작은 값의 정수를 K의 우측 경계값으로 정한다. 올림 후 -1 해야 정확한 경계 나옴
            // 좌측경계가 우측경계보다 크다면 impossible

        }
    }

    static EGResult extendedGcd(long a, long b) {
        long s0 = 1, t0 = 0, r0 = a;
        long s1 = 0, t1 = 1, r1 = b;

        long tmp;
        while (r1 != 0) {
            long q = r0 / r1;

            tmp = r0 - r1 * q;
            r0 = r1;
            r1 = tmp;

            tmp = s0 - s1 * q;
            s0 = s1;
            s1 = tmp;

            tmp = t0 - t1 * q;
            t0 = t1;
            t1 = tmp;
        }

        return new EGResult(s0, t0, r0);
    }
}

class EGResult {
    long s, t, r;

    public EGResult(long s, long t, long r) {
        this.s = s;
        this.t = t;
        this.r = r;
    }
}