import java.io.*;
import java.util.*;

class Problem {
    int dead, noodle;

    public Problem(int dead, int noodle) {
        this.dead = dead;
        this.noodle = noodle;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Problem> pq = new PriorityQueue<>((p1, p2) -> {
            if (p1.dead == p2.dead) {
                return p2.noodle - p1.noodle;
            }
            return p1.dead - p2.dead;
        });

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            pq.add(new Problem(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        PriorityQueue<Problem> curNoodles = new PriorityQueue<>((o1, o2) -> o1.noodle - o2.noodle);

        while (!pq.isEmpty()) {
            Problem curProblem = pq.poll();

            if (curNoodles.size() < curProblem.dead) {
                curNoodles.add(curProblem);
            } else {
                if (curNoodles.peek().noodle < curProblem.noodle) {
                    curNoodles.poll();
                    curNoodles.add(curProblem);
                }
            }
        }

        long ans = curNoodles.stream().mapToLong(x -> x.noodle).sum();
        System.out.println(ans);
    }

}