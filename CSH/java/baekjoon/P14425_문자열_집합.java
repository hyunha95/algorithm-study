package baekjoon;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class P14425_문자열_집합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        Set<String> set = new HashSet<>();

        for (int i = 0; i < N; i++) {
            set.add(sc.next());
        }


        int count = 0;
        for (int i = 0; i < M; i++) {
            if (set.contains(sc.next())) {
                count++;
            }
        }

        System.out.println(count);
    }
}
