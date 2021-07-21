package day3;

import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

public class sol_1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        List<Point> jewels = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            jewels.add(new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        List<Integer> bags = new ArrayList<>();

        for (int i = 0; i < K; i++) {
            bags.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(jewels, Comparator.comparingInt(o -> o.x));
        Collections.sort(bags);

        PriorityQueue<Point> pq = new PriorityQueue<>((o1, o2) -> o2.y - o1.y);

        long answer = 0;
        int idx = 0;
        for (int bag : bags) {
            while (true) {
                if (idx >= jewels.size() || jewels.get(idx).x > bag) {
                    break;
                }
                pq.add(jewels.get(idx++));
            }
            if (pq.size() > 0) {
                answer += pq.poll().y;
            }
        }

        System.out.println(answer);
    }
}