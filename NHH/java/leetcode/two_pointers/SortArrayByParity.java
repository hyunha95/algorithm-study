package leetcode.two_pointers;

import java.util.Arrays;

public class SortArrayByParity {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(sortArrayByParity(new int[] {3,1,2,4})));
    }

    public static int[] sortArrayByParity(int[] nums) {
        int even = 0;
        int odd = nums.length - 1;

        int[] arr = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                arr[even] = nums[i];
                even++;
            } else {
                arr[odd] = nums[i];
                odd--;
            }
        }

        return arr;
    }
}
