package leetcode.two_pointers;

import java.util.Arrays;

public class SquaresOfASortedArray {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sortedSquares2(new int[]{-4, -1, 0, 3, 10})));
    }

    public static int[] sortedSquares2(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        int[] sortedNums = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                sortedNums[i] = nums[right] * nums[right];
                right--;
            } else {
                sortedNums[i] = nums[left] * nums[left];
                left++;
            }

        }

        return sortedNums;
    }


    public static int[] sortedSquares(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }

        Arrays.sort(nums);

        return nums;
    }

}
