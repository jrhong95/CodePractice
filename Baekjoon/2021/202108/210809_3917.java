import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Pos {
    int r, c;

    public Pos(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {
    static final int[] mr = { 0, 1, 0, -1 };
    static final int[] mc = { 1, 0, -1, 0 };

    static int R, C;
    static int endR, endC;
    static char[][] lake;
    static Queue<Pos> alreadyWater, melt;
    static Queue<Pos> canMove, nextMove;

    static boolean[][] waterVisited, swanVisited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        alreadyWater = new LinkedList<>();
        melt = new LinkedList<>();
        canMove = new LinkedList<>();
        nextMove = new LinkedList<>();

        waterVisited = new boolean[R][C];
        swanVisited = new boolean[R][C];
        lake = new char[R][C];

        boolean flag = true;

        for (int i = 0; i < R; i++) {
            String s = br.readLine();
            for (int j = 0; j < C; j++) {
                char c = s.charAt(j);
                lake[i][j] = c;

                if (c == '.') { // 물일경우
                    alreadyWater.add(new Pos(i, j));
                    waterVisited[i][j] = true;
                } else if (c == 'L') {
                    if (flag) {
                        canMove.add(new Pos(i, j));
                        swanVisited[i][j] = true;
                        flag = false;
                    } else {
                        endR = i;
                        endC = j;
                    }
                    lake[i][j] = '.';
                    alreadyWater.add(new Pos(i, j));
                    waterVisited[i][j] = true;
                }
            }
        }

        int count = 0;
        while (true) {
            waterMelt();
            if (swanMove()) {
                break;
            }
            count++;
            alreadyWater = melt;
            canMove = nextMove;

            melt = new LinkedList<>();
            nextMove = new LinkedList<>();
        }
        System.out.println(count);
    }

    static void waterMelt() {
        while (!alreadyWater.isEmpty()) {
            Pos curPos = alreadyWater.poll();

            if (lake[curPos.r][curPos.c] == 'X') {
                lake[curPos.r][curPos.c] = '.';
            }

            for (int i = 0; i < 4; i++) {
                int nr = curPos.r + mr[i];
                int nc = curPos.c + mc[i];

                if (nr < 0 || nr >= R || nc < 0 || nc >= C || waterVisited[nr][nc]) {
                    continue;
                }
                if (lake[nr][nc] == 'X') {
                    melt.add(new Pos(nr, nc));
                    waterVisited[nr][nc] = true;
                }
            }
        }
    }

    static boolean swanMove() {
        while (!canMove.isEmpty()) {
            Pos curPos = canMove.poll();

            if (curPos.r == endR && curPos.c == endC) {
                return true;
            }

            for (int i = 0; i < 4; i++) {
                int nr = curPos.r + mr[i];
                int nc = curPos.c + mc[i];

                if (nr < 0 || nr >= R || nc < 0 || nc >= C || swanVisited[nr][nc]) {
                    continue;
                }
                if (lake[nr][nc] == '.') {
                    canMove.add(new Pos(nr, nc));
                } else {
                    nextMove.add(new Pos(nr, nc));
                }
                swanVisited[nr][nc] = true;
            }
        }
        return false;
    }
}
