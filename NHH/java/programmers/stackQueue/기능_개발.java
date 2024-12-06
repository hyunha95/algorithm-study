package programmers.stackQueue;

import java.util.*;

public class 기능_개발 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{93, 30, 55}, new int[]{1, 30, 5})));
    }

    public static int[] solution(int[] progresses, int[] speeds) {
        List<Integer> result = new ArrayList<>();

        // 각 작업의 남은 일수를 계산
        Queue<Integer> daysQueue = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++) {
            int remainingWork = 100 - progresses[i];
            int days = (int) Math.ceil((double) remainingWork / speeds[i]);
            daysQueue.add(days);
        }

        // 배포 일정을 그룹화
        while (!daysQueue.isEmpty()) {
            int deployDay = daysQueue.poll();
            int count = 1;

            while (!daysQueue.isEmpty() && daysQueue.peek() <= deployDay) {
                daysQueue.poll();
                count++;
            }
            result.add(count);
        }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
