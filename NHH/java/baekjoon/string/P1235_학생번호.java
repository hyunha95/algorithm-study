package baekjoon.string;

import java.util.*;

public class P1235_학생번호 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<String> studentNumbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            studentNumbers.add(sc.next());
        }

        int index = 0;
        Set<String> set = new HashSet<>();
        while (true) {

            for (String studentNumber : studentNumbers) {
                set.add(studentNumber.substring(studentNumber.length() - 1 - index));
            }

            if (set.size() == N) {
                System.out.println(index+1);
                break;
            } else {
                set.clear();
            }
            index++;
        }
    }
}
