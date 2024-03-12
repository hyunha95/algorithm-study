package leetcode.easy;

import java.util.HashSet;
import java.util.Set;

public class LongestCommonPrefix {

    public static void main(String[] args) {
        System.out.println(longestCommonPrefix(new String[]{"flower","flow","flight"}));
        System.out.println(longestCommonPrefix(new String[]{"dog","racecar","car"}));
        System.out.println(longestCommonPrefix(new String[]{"cir","car"}));
    }

    public static String longestCommonPrefix(String[] strs) {
        int shortestLength = 200;
        for (String str: strs) {
            shortestLength = Math.min(str.length(), shortestLength);
        }

        String answer = "";
        for (int i = 0; i < shortestLength; i++) {
            Set<Character> set = new HashSet<>();
            char curr = ' ';
            for (int j = 0; j < strs.length; j++) {
                curr = strs[j].charAt(i);
                set.add(curr);
            }

            if (set.size() == 1) {
                answer += curr;
            } else {
                break;
            }
        }
        return answer;
    }
}
