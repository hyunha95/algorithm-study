package programmers.stackQueue;

import java.util.LinkedList;
import java.util.Queue;

public class 프로세스 {

    public static void main(String[] args) {
        System.out.println(solution(new int[]{2, 1, 3, 2}, 2));
        System.out.println(solution(new int[]{1, 1, 9, 1, 1, 1}, 0));
    }

    public static int solution(int[] priorities, int location) {
        Queue<Process> queue = new LinkedList<>();

        // Step 1: 큐에 프로세스와 위치를 함께 저장
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new Process(priorities[i], i));
        }

        int answer = 0; // 몇 번째로 실행되는지 나타내는 변수
        while (!queue.isEmpty()) {
            Process polled = queue.poll();

            // Step 2: 현재 프로세스보다 높은 우선순위가 있는지 확인
            boolean hasHigherPriority = queue.stream().anyMatch(peeked -> peeked.priority > polled.priority);

            if (hasHigherPriority) {
                // 우선순위가 더 높은 프로세스가 있으면 다시 큐에 추가
                queue.offer(polled);
            } else {
                // 현재 프로세스 실행
                answer++;
                if (polled.location == location) {
                    // 실행한 프로세스가 우리가 찾는 프로세스일 경우 실행 순서를 반환
                    return answer;
                }
            }
        }

        return answer;
    }

    static class Process {
        int priority;
        int location;

        public Process(int priority, int location) {
            this.priority = priority;
            this.location = location;
        }
    }

}
