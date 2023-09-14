package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class P1543_문서검색 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String alpha = sc.nextLine();

        word = word.replaceAll(alpha, "*");

        int count = (int) word.chars()
                .filter(ch -> ch == '*')
                .count();

        System.out.println(count);
    }
}
