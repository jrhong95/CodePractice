package P_2960;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        System.out.println(findDeletePrime(N, K));
    }

    static int findDeletePrime(int N, int K) {
        boolean[] primes = new boolean[N + 1];
        int count = 0;

        for (int i = 2; i < N + 1; i++) {
            if (!primes[i]) {
                for (int j = i; j < N + 1; j += i) {
                    if (!primes[j]) {
                        primes[j] = true;
                        count++;
                    }

                    if (count == K) {
                        return j;
                    }
                }
            }

        }
        return -1;
    }
}
