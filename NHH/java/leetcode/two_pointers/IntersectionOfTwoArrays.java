package leetcode.two_pointers;

import java.util.*;

public class IntersectionOfTwoArrays {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(intersection(new int[]{1, 2, 2, 1}, new int[]{2, 2})));
    }

    public static int[] intersection2(int[] nums1, int[] nums2) {
        boolean[] contains = new boolean[1001];

        for (int num1 : nums1) {
            contains[num1] = true;
        }

        List<Integer> answers = new ArrayList<>();
        for (int num2 : nums2) {
            if (contains[num2]) {
                answers.add(num2);
                contains[num2] = false;
            }
        }

        return answers.stream().mapToInt(Integer::valueOf).toArray();
    }

    public static int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums1.length; i++) {
            Integer key = nums1[i];
            map.putIfAbsent(key, 1);
        }


        Set<Integer> answers = new HashSet<>();
        for (int i = 0; i < nums2.length; i++) {
            Integer key = nums2[i];
            if (map.containsKey(key) && !answers.contains(key)) {
                answers.add(key);
            }
        }

        return answers.stream().mapToInt(Integer::valueOf).toArray();
    }
}
