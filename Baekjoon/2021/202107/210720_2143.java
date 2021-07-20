import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int T, An, Bn;
    static int[] A, B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        An = Integer.parseInt(br.readLine());
        A = new int[An];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < An; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer> aSort = sumArray(A, An);
        Collections.sort(aSort);

        Bn = Integer.parseInt(br.readLine());
        B = new int[Bn];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < Bn; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer> bSort = sumArray(B, Bn);
        Collections.sort(bSort, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2.intValue() - o1.intValue();
            }
        });

        System.out.println(twoPointer(aSort, bSort));
    }

    static ArrayList<Integer> sumArray(int[] arr, int size) {
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            int tmpSum = 0;
            for (int j = i; j < size; j++) {
                tmpSum += arr[j];
                ans.add(tmpSum);
            }
        }
        return ans;
    }

    static long twoPointer(ArrayList<Integer> A, ArrayList<Integer> B) {
        int aPos = 0, bPos = 0;
        long answer = 0;

        while (true) {
            int sum = A.get(aPos) + B.get(bPos);
            if (sum > T) {
                bPos++;
            } else if (sum == T) {
                int curValue = A.get(aPos++);
                long aCount = 1, bCount = 1;

                while (aPos < A.size() && A.get(aPos) == curValue) {
                    aPos++;
                    aCount++;
                }

                curValue = B.get(bPos++);
                while (bPos < B.size() && B.get(bPos) == curValue) {
                    bPos++;
                    bCount++;
                }
                answer += aCount * bCount;
            } else {
                aPos++;
            }
            if (aPos == A.size() || bPos == B.size()) {
                break;
            }
        }
        return answer;
    }
}
