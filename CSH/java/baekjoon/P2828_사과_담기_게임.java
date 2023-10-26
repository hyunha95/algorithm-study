package baekjoon;

import java.util.List;
import java.util.Scanner;

public class P2828_사과_담기_게임 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int j = sc.nextInt();

        int[] arr = new int[j];
        int result = 0;

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }


        int endPoint = m;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > endPoint) {
                result += arr[i] - endPoint;
                endPoint = arr[i];
            } else {
                if ((endPoint - (m-1)) > arr[i]) {
                    result += endPoint -(m-1) - arr[i];
                    endPoint = arr[i] + (m-1);
                }
            }

        }

        System.out.println(result);
    }
}
