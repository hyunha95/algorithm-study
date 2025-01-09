package baekjoon.알고리즘책.투포인터;

import java.util.Scanner;

public class 연속된_자연수의_합구하기 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int sum = 1;
        int count = 1;
        int startIndex = 1;
        int endIndex = 1;

        while (endIndex != N) {
            if (sum > N) {
                sum -= startIndex;
                startIndex++;
            } else if (sum < N) {
                sum += endIndex;
                endIndex++;
            } else {
                count++;
                endIndex++;
                sum += endIndex;
            }
        }

        System.out.println(count);
    }
}
