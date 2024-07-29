package leetcode.two_pointers;

public class FindTheArrayConcatenationValue {

    public static void main(String[] args) {
        System.out.println(findTheArrayConcVal(new int[] {5,14,13,8,12}));
    }

    public static long findTheArrayConcVal(int[] nums) {
        int i = 0;
        int j = nums.length - 1;

        long answer = 0;
        while (i < j) {
            String conc = "" + nums[i] + nums[j];
            answer += Long.parseLong(conc);
            i++;
            j--;
        }

        if (nums.length % 2 != 0) {
            answer += nums[nums.length / 2];
        }

        return answer;
    }
}
