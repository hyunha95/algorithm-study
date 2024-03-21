package leetcode.easy;

import java.util.HashMap;
import java.util.Map;

public class ClimbingStairs {

    public static void main(String[] args) {
        System.out.println(climbStairs(2));
        System.out.println(climbStairs(3));
        System.out.println(climbStairs(4)); // 5
        System.out.println(climbStairs(5)); // 8
        System.out.println(climbStairs(6)); // 13
        System.out.println(climbStairs(45));
    }

    private static Map<Integer, Integer> map = new HashMap<>();

    public static int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        if (map.get(n) != null) {
            return map.get(n);
        }

        map.put(n, climbStairs(n - 1) + climbStairs(n - 2));

        return map.get(n);
    }

    public static int climbStairsV2(int n) {
        if (n <= 2) {
            return n;
        }

        int[] array = new int[n];
        array[0] = 1;
        array[1] = 2;

        for (int i = 2; i < n; i++) {
            array[i] = array[i - 1] + array[i - 2];
        }

        return array[n - 1];
    }

    /*
       1 = 1
       2 = 2
       3 = 3
       4 = 1 1 1 1
           1 1 2
           1 2 1
           2 1 1
           2 2

        1 1 1 1 1
        1 1 1 2
        1 1 2 1
        1 2 1 1
        2 1 1 1
        1 2 2
        2 1 2
        2 2 1

     */
}
