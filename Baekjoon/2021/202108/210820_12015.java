import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] nums, indices;
    static ArrayList<Integer> tmp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[N];
        indices = new int[N];
        tmp = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int idx = 1;
        tmp.add(nums[0]);
        for (int i = 1; i < N; i++) {
            if (tmp.get(tmp.size() - 1) < nums[i]) {
                indices[i] = idx++;
                tmp.add(nums[i]);
            } else {
                int findIdx = biSearch(nums[i]);
                tmp.set(findIdx, nums[i]);
                indices[i] = findIdx;
            }
        }
        System.out.println(idx);
    }

    static int biSearch(int target) {
        int start = 0, end = tmp.size();

        while (start < end) {
            int mid = (start + end) / 2;
            if (target <= tmp.get(mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
}
