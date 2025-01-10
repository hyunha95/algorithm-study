package programmers.kakao.kakao_tech_internship_2022;

import java.util.LinkedList;
import java.util.Queue;

/**
 * ChatGPT 풀이
 */
public class 두큐합같게만들기 {

    public static void main(String[] args) {
        int[] queue1 = {3, 2, 7, 2};
        int[] queue2 = {4, 6, 5, 1};
        System.out.println(solution(queue1, queue2));

        int[] queue3 = {1, 2, 1, 2};
        int[] queue4 = {1, 10, 1, 2};
        System.out.println(solution(queue3, queue4));

        int[] queue5 = {1, 1};
        int[] queue6 = {1, 5};
        System.out.println(solution(queue5, queue6));
    }
    public static int solution(int[] queue1, int[] queue2) {
        long sum1 = 0, sum2 = 0;
        for (int num : queue1) sum1 += num;
        for (int num : queue2) sum2 += num;

        long totalSum = sum1 + sum2;

        if (totalSum % 2 != 0) return -1;

        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();

        for (int num : queue1) q1.add(num);
        for (int num : queue2) q2.add(num);

        long target = totalSum / 2;

        int steps = 0;
        int maxSteps = queue1.length * 3;

        while (sum1 != target && steps < maxSteps) {
            if (sum1 > target) {
                int moved = q1.poll();
                sum1 -= moved;
                sum2 += moved;
                q2.add(moved);
            } else {
                int moved = q2.poll();
                sum2 -= moved;
                sum1 += moved;
                q1.add(moved);
            }
            steps++;
        }

        return sum1 == target ? steps : -1;
    }

//    public static int solution(int[] queue1, int[] queue2) {
//        // 합 계산
//        long sum1 = 0, sum2 = 0;
//        for (int num : queue1) sum1 += num;
//        for (int num : queue2) sum2 += num;
//
//        // 두 큐의 합을 구함
//        long totalSum = sum1 + sum2;
//
//        // 합이 홀수면 각 큐의 합을 같게 만들 수 없음
//        if (totalSum % 2 != 0) return -1;
//
//        long target = totalSum / 2; // 각 큐의 목표 합
//
//        // 큐를 구현하기 위해 LinkedList 사용
//        Queue<Integer> q1 = new LinkedList<>();
//        Queue<Integer> q2 = new LinkedList<>();
//
//        for (int num : queue1) q1.add(num);
//        for (int num : queue2) q2.add(num);
//
//        int steps = 0; // 작업 횟수
//        int maxSteps = queue1.length * 3; // 최대 작업 횟수 제한 (무한 루프 방지)
//
//        while (sum1 != target && steps <= maxSteps) {
//            if (sum1 > target) {
//                // q1에서 pop하여 q2로 이동
//                int moved = q1.poll();
//                sum1 -= moved;
//                sum2 += moved;
//                q2.add(moved);
//            } else {
//                // q2에서 pop하여 q1으로 이동
//                int moved = q2.poll();
//                sum2 -= moved;
//                sum1 += moved;
//                q1.add(moved);
//            }
//            steps++;
//        }
//
//        // 목표 당성 여부 확인
//        return sum1 == target ? steps : -1;
//    }
}
