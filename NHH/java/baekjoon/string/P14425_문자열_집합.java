package baekjoon.string;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class P14425_문자열_집합 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        List<String> nArr = new ArrayList<>();
        List<String> mArr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nArr.add(sc.next());
        }

        for (int i = 0; i < m; i++) {
            mArr.add(sc.next());
        }

        long count = mArr.stream()
                .filter(nArr::contains)
                .count();

        System.out.println(count);

    }
}
