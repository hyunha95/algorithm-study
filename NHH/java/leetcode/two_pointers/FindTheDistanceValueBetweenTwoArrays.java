package leetcode.two_pointers;

public class FindTheDistanceValueBetweenTwoArrays {
    public static void main(String[] args) {
        System.out.println(findTheDistanceValue(new int[]{4,5,8}, new int[]{10,9,1,8}, 2));
    }

    public static int findTheDistanceValue(int[] arr1, int[] arr2, int d) {

        int distance = 0;
        for (int i = 0; i < arr1.length; i++) {
            boolean found = true;

            for (int j = 0; j < arr2.length; j++) {
                if (Math.abs(arr1[i] - arr2[j]) <= d) {
                    found = false;
                    break;
                }
            }

            if (found) distance++;
        }

        return distance;
    }
}
