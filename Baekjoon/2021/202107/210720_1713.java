import java.util.*;

class People implements Comparable<People> {
    int idx;
    int num;
    int recommend;

    public People(int idx, int num, int recommend) {
        this.idx = idx;
        this.num = num;
        this.recommend = recommend;
    }

    @Override
    public int compareTo(People p) {
        return this.num - p.num;
    }
}

class Main {
    public static int n, m;
    public static ArrayList<People> frame = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            int num = sc.nextInt();

            if (!personInFrame(num)) {// 사진틀에 해당 번호가 걸려있지 않은 경우
                if (frame.size() == n) { // 걸릴 자리가 없는 경우
                    Collections.sort(frame, new Comparator<People>() {
                        @Override
                        public int compare(People p1, People p2) {
                            if (p1.recommend == p2.recommend) {
                                return p1.idx - p2.idx;
                            } else {
                                return p1.recommend - p2.recommend;
                            }
                        }
                    });

                    frame.remove(0);
                }
                frame.add(new People(i, num, 1));
            }
        }
        Collections.sort(frame);
        for (People p : frame) {
            System.out.print(p.num + " ");
        }
    }

    static boolean personInFrame(int num) {
        for (People person : frame) {
            if (person.num == num) {
                person.recommend++;
                return true;
            }
        }
        return false;
    }
}
