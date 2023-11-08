package baekjoon;

import java.util.Scanner;

public class P1817_짐_챙기는_숌 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int count = 0;

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int i = 0;

        // 책의 개수를 넘지 않는 동안 반복 한다.
        while (i < N){
            int tmp = 0; // 책의 무게를 담을 변수
            while (tmp <= M) { // 무게가 박스 최대 무게를 넘지 않는 동안 반복한다.
                tmp += arr[i]; // 책의 무게를 더한다.
                i++; // 다음 책으로 넘어 간다.

                if (i >= N) { // 이 때 책의 개수를 넘어갔다면 반복문을 종료한다.
                    break;
                }
            }

            if (tmp > M) { // 다음 책의 무게를 더했을 때 박스 최대 무게를 넘었다면 마지막에 넣은 책을 도로 내려놓는다.
                i --; // 책을 내려놓는 것이기 때문에 인덱스를 하나 빼준다.
            }
            tmp = 0; // 무게를 초기화 한다.
            count++; // 박스 개수를 증가시킨다.
        }

        System.out.println(count);
    }
}
