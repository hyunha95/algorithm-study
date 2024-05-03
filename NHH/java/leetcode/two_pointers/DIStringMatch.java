package leetcode.two_pointers;

import java.util.Arrays;

public class DIStringMatch {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(diStringMatch("IDID")));
        System.out.println(Arrays.toString(diStringMatch("III")));
        System.out.println(Arrays.toString(diStringMatch("DDI")));
    }

    public static int[] diStringMatch(String s) {
        int[] nums = new int[s.length() + 1];
        int[] answers = new int[s.length() + 1];

        for (int i = 0; i <= s.length(); i++) {
            nums[i] = i;
        }

        int min = 0;
        int max = s.length();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'I') {
                answers[i] = nums[min++];
            } else {
                answers[i] = nums[max--];
            }
        }

        answers[answers.length - 1] = nums[min];
        return answers;
    }
}
