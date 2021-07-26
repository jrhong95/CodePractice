import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int[][] board = new int[9][9];
    static ArrayList<Point> rest;
    static int restSize;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        rest = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                int n = Integer.parseInt(st.nextToken());
                board[i][j] = n;

                if (n == 0) {
                    rest.add(new Point(j, i));
                }
            }
        }
        restSize = rest.size();
        if (restSize == 0) {
            printBoard();
        } else {
            backTracking(0);
        }
    }

    static void printBoard() {
        StringBuilder sb = new StringBuilder();
        for (int[] l : board) {
            for (int n : l) {
                sb.append(n).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    static void backTracking(int idx) {
        if (idx == restSize) {
            printBoard();
            System.exit(0);
        }

        int r = rest.get(idx).y;
        int c = rest.get(idx).x;
        for (int i = 1; i < 10; i++) {
            if (check(r, c, i)) {
                board[r][c] = i;
                backTracking(idx + 1);
                board[r][c] = 0;
            }
        }
    }

    static boolean check(int r, int c, int num) {
        for (int i = 0; i < 9; i++) {
            // 가로 검사
            if (num == board[r][i]) {
                return false;
            }
            // 세로 검사
            if (num == board[i][c]) {
                return false;
            }
        }

        for (int i = (r / 3) * 3; i < (r / 3) * 3 + 3; i++) {
            for (int j = (c / 3) * 3; j < (c / 3) * 3 + 3; j++) {
                if (num == board[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
