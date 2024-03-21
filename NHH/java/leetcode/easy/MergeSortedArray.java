package leetcode.easy;

import java.util.Arrays;

public class MergeSortedArray {

    public static void main(String[] args) {
        merge2(new int[]{1, 2, 3, 0, 0, 0}, 3, new int[]{2, 5, 6}, 3);
        merge2(new int[]{-1, 0, 0, 3, 3, 3, 0, 0, 0}, 6, new int[]{1, 2, 2}, 3);
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int num2Pointer = 0;
        for (int i = 0; i < m + n; i++) {
            if (nums1[i] == 0 && num2Pointer < n) {
                nums1[i] = nums2[num2Pointer++];
            }
        }
        Arrays.sort(nums1);

        int[] newNums1 = new int[m + n];
        for (int i = 0, j = 0; i < m + n; i++) {
            if (nums1[i] != 0) {
                newNums1[j++] = nums1[i];
            }
        }

        nums1 = newNums1;

        System.out.println(Arrays.toString(nums1));
    }

    public static void merge2(int[] nums1, int m, int[] nums2, int n) {
        int mP = m - 1;
        int nP = n - 1;
        int k = m + n - 1;

        while (nP > -1) {
            if (mP >= 0 && nums1[mP] > nums2[nP]) {
                nums1[k] = nums1[mP];
                mP--;
            } else {
                nums1[k] = nums2[nP];
                nP--;
            }
            k--;
        }

        System.out.println(Arrays.toString(nums1));
    }
}