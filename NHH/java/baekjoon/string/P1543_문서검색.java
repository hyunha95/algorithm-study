package baekjoon.string;

import java.util.Scanner;

public class P1543_문서검색 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String words = sc.nextLine();
        String findWord = sc.nextLine();

        words = words.replaceAll(findWord, "*");

        int answer = 0;
        while (true) {
            int index = words.indexOf(findWord);
            if (index == -1) {
                break;
            }

            words = words.substring(index + findWord.length());
            answer++;
        }

        System.out.println(answer);


    }
}
