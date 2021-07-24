package P_1644;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static List<Integer> primes;
    static boolean[] check;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n == 1) {
            System.out.println(0);
        } else {
            makePrimes(n);

            int left = 0, right = 0, answer = 0;
            long sum = primes.get(0);

            while (true) {
                if (sum < n) {
                    if (right == primes.size() - 1) {
                        break;
                    }
                    sum += primes.get(++right);
                } else if (sum > n) {
                    sum -= primes.get(left++);
                } else {
                    answer++;
                    sum -= primes.get(left++);
                }

                if (left > right) {
                    break;
                }
            }
            System.out.println(answer);
        }
    }

    static void makePrimes(int n) {
        check = new boolean[n + 1];
        primes = new ArrayList<>();
        for (int i = 2; i < n + 1; i++) {
            if (!check[i]) {
                primes.add(i);
                for (int j = i * 2; j < n + 1; j += i) {
                    check[j] = true;
                }
            }
        }
    }
}
