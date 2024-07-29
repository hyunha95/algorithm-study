package leetcode.two_pointers;

public class ApplyOperationsToAnArray {

    public static void main(String[] args) {

    }

    public int[] applyOperations(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1]) {
                nums[i] = nums[i] * 2;
                nums[i+1] = 0;
            }
        }

        int[] newNums = new int[nums.length];
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                newNums[index++] = nums[i];
            }
        }

        return newNums;
    }
}
