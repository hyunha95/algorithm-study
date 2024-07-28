package leetcode.two_pointers;

import java.util.Arrays;

public class SortArrayByParityII {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sortArrayByParityII(new int[]{4,2,5,7})));
    }

    public static int[] sortArrayByParityII(int[] nums) {
        int even = 0;
        int odd = 1;

        int[] answers = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                answers[even] = nums[i];
                even += 2;
            } else {
                answers[odd] = nums[i];
                odd += 2;
            }
        }
        return answers;
    }

}
