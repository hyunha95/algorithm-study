package leetcode.two_pointers;

import java.util.Arrays;

public class LargestPositiveIntegerThatExistsWithItsNegative {

    public static void main(String[] args) {
//        System.out.println(findMaxK(new int[]{-1,2,-3,3}));
//        System.out.println(findMaxK(new int[]{-1,10,6,7,-7,1}));
        System.out.println(findMaxK(new int[]{-10,8,6,7,-2,-3}));
    }

    static int [] count = new int[1000 + 1];

    public static int findMaxK(int[] nums) {
        for (int num : nums) {
            if (num > 0) count[num]++;
        }

        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num < 0 && count[-num] > 0) max = Math.max(max, -num);
        }

        return max == Integer.MIN_VALUE ? -1 : max;
    }
}
