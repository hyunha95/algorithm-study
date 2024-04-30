package leetcode.two_pointers;

import java.util.*;

public class NumberOfArithmeticTriplets {

    public static void main(String[] args) {
        System.out.println(arithmeticTriplets(new int[] {0,1,4,6,7,10}, 3));
        System.out.println(arithmeticTriplets(new int[] {4,5,6,7,8,9}, 2));
    }

    public static int arithmeticTriplets(int[] nums, int diff) {
        int cnt = 0;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num - diff) && seen.contains(num - diff * 2)) {
                cnt += 1;
            }
            seen.add(num);
        }
        return cnt;
    }
}
