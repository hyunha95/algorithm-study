package programmers.stackQueue;

import java.util.*;

public class 같은_숫자는_싫어 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 1, 3, 3, 0, 1, 1})));
        System.out.println(Arrays.toString(solution(new int[]{4, 4, 4, 3, 3})));
    }

    public static int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();

        int prevVal = -1;
        for (int i = 0; i < arr.length; i++) {
            if (prevVal != arr[i]) {
                answer.add(arr[i]);
            }
            prevVal = arr[i];
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
