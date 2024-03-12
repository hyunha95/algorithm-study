package leetcode.easy;

public class SearchInsertPosition {

    public static void main(String[] args) {
        System.out.println(searchInsert(new int[] {1,3,5,6}, 5));
        System.out.println(searchInsert(new int[] {1,3,5,6}, 2));
        System.out.println(searchInsert(new int[] {1,3,5,6}, 7));
    }

    public static int searchInsert(int[] nums, int target) {
        if (target > nums[nums.length - 1]) {
            return nums.length;
        }

        int index = 0;
        while (nums[index] < target) {
            index++;
        }

        return index;
    }
}
