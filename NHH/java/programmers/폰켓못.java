package programmers;

import java.util.HashSet;
import java.util.Set;

public class 폰켓못 {

    public static void main(String[] args) {
        System.out.println(solution(new int[]{3,1,2,3}));
        System.out.println(solution(new int[]{3,3,3,2,2,4}));
        System.out.println(solution(new int[]{3,3,3,2,2,2}));
    }

    public static int solution(int[] nums) {

        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        if (set.size() > nums.length / 2) {
            return nums.length / 2;
        } else {
            return set.size();
        }
    }
}
