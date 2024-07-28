package leetcode.two_pointers;

import java.util.*;

public class MergeTwo2DArraysBySummingValues {

    public static void main(String[] args) {
        int[][] nums1 = {{1,2},{2,3},{4,5}};
        int[][] nums2 = {{1,4},{3,2},{4,1}};
        System.out.println(Arrays.deepToString(mergeArrays2(nums1, nums2)));
    }

    public static int[][] mergeArrays2(int[][] nums1, int[][] nums2) {
        int n = nums1.length;
        int m = nums2.length;

        int i = 0;
        int j = 0;

        List<int[]> list = new ArrayList<>();
        while (i < n && j < m) {
            if (nums1[i][0] == nums2[j][0]) {
                list.add(new int[] {nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                list.add(new int[] {nums1[i][0], nums1[i][1]});
                i++;
            } else {
                list.add(new int[] {nums2[j][0], nums2[j][1]});
                j++;
            }
        }

        while(i < n) {
            list.add(new int[]{ nums1[i][0], nums1[i][1]});
            i++;
        }

        while(j < m) {
            list.add(new int[]{ nums2[j][0], nums2[j][1]});
            j++;
        }

        int[][] answers = new int[list.size()][2];
        for (int k = 0; k < answers.length; k++) {
            answers[k] = list.get(k);
        }
        return answers;
    }

    public static int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> map = new LinkedHashMap<>();

        for (int i = 0; i < nums1.length; i++) {
            map.put(nums1[i][0], nums1[i][1]);
        }

        for (int i = 0; i < nums2.length; i++) {
            map.put(nums2[i][0], map.getOrDefault(nums2[i][0], 0) + nums2[i][1]);
        }

        return map.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByKey())
                .map(entry -> new int[]{entry.getKey(), entry.getValue()})
                .toArray(int[][]::new);
    }

}
