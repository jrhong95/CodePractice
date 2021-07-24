import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static String P;
    static int K;
    static boolean[] primeNums;
    static List<Integer> primes;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        P = st.nextToken();
        K = Integer.parseInt(st.nextToken());

        makePrimeNumber();
        solve();
    }

    static void makePrimeNumber() {
        primeNums = new boolean[K];
        primes = new ArrayList<>();
        for (int i = 2; i < K; i++) {
            if (!primeNums[i]) {
                primes.add(i);

                for (int j = 2;; j++) {
                    int idx = i * j;
                    if (idx >= K)
                        break;
                    primeNums[idx] = true;
                }
            }
        }
    }

    static void solve() {
        for (int i : primes) {
            int curNum = 0;

            for (int j = 0; j < P.length(); j++) {
                curNum = (curNum * 10 + Integer.parseInt(String.valueOf(P.charAt(j)))) % i;
            }

            if (curNum == 0) {
                System.out.println("BAD " + i);
                return;
            }
        }
        System.out.println("GOOD");
    }
}
