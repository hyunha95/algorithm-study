package programmers.완전탐색;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 모의고사 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[] {1,2,3,4,5})));
        System.out.println(Arrays.toString(solution(new int[] {1,3,2,4,2})));
    }

    public static int[] solution(int[] answers) {
        int[][] omrs = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };

        int[] correctCounts = new int[3];
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < omrs.length; j++) {
                System.out.println(i % omrs[j].length);
                if (omrs[j][i % omrs[j].length] == answers[i]) {
                    correctCounts[j]++;
                }
            }
        }

        int max = Arrays.stream(correctCounts).max().getAsInt();
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (correctCounts[i] == max) {
                answer.add(i + 1);
            }
        }

        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}
