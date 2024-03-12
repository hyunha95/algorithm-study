package leetcode.easy;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class RemoveDuplicatesFromSortedArray {

    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[] {1,1,2}));
        System.out.println(removeDuplicates(new int[] {0,0,1,1,1,2,2,3,3,4}));
    }

    public static int removeDuplicates(int[] nums) {
        int pointer = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[pointer] != nums[i]) {
                pointer++;
                nums[pointer] = nums[i];
            }
        }
        return pointer + 1;
    }
}
