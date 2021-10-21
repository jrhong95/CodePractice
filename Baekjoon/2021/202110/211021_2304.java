import java.util.*;
import java.io.*;

class Pos {
    int pos;
    int height;

    public Pos(int pos, int height) {
        this.pos = pos;
        this.height = height;
    }

    @Override
    public String toString() {
        return "[" + pos + ", " + height + "]";
    }
}

public class Test3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        List<Pos> list = new ArrayList<>();

        for (int i = 0; i < tc; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int position = Integer.parseInt(st.nextToken()), height = Integer.parseInt(st.nextToken());
            list.add(new Pos(position, height));
        }

        list.sort((p1, p2) -> {
            return p1.pos - p2.pos;
        });
        System.out.println(list);
        int size = 0;

        int prevHeight = 0, prevPos = 0;
        for (int i = 0; i < list.size(); i++) {
            Pos cur = list.get(i);
            if (prevHeight <= cur.height) {
                size += (cur.pos - prevPos) * prevHeight;
                prevHeight = cur.height;
                prevPos = cur.pos;
            }
        }

        prevHeight = 0;
        prevPos = 0;
        for (int i = list.size() - 1; i >= 0; i--) {
            Pos cur = list.get(i);
            if (prevHeight < cur.height) {
                size += (prevPos - cur.pos) * prevHeight;
                prevHeight = cur.height;
                prevPos = cur.pos;
            }
        }

        System.out.println(size + prevHeight);
    }
}
