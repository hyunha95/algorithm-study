package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 구간_합_구하기_2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] sumArr = new int[N+1][N+1];
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < N+1; j++) {
                sumArr[i][j] = arr[i][j-1] + arr[i-1][j] + arr[i-1][j-1];
            }
        }

        System.out.println(Arrays.deepToString(arr));
        System.out.println(Arrays.deepToString(sumArr));
    }
}