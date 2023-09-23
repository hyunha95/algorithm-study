package baekjoon;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
public class P1235_학생_번호 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = 0;

        String[] nums = new String[n];

        for (int i = 0; i < n; i++) {
            nums[i] = sc.next();
        }

        while (true) {
            Set<String> numSet = new HashSet();

            for (String num : nums) {
                int startIndex = Math.max(num.length() - k, 0);

                if (startIndex < num.length()) {
                    numSet.add(num.substring(startIndex));
                }
            }

            if (numSet.size() == n) {
                break;
            }
            k++;
        }
        System.out.println(k);

    }
}
