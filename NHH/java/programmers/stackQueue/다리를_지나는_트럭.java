package programmers.stackQueue;

import java.util.*;

public class 다리를_지나는_트럭 {

    public static void main(String[] args) {
        System.out.println(solution(2, 10, new int[]{7,4,5,6}));
        System.out.println(solution(100, 100, new int[]{10}));
        System.out.println(solution(100, 100, new int[]{10,10,10,10,10,10,10,10,10,10}));
    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> queue = new LinkedList<>();

        int sum = 0;
        int seconds = 0;
        for (int truckWeight : truck_weights) {
            while (true) {
                if (queue.isEmpty()) {
                    queue.offer(truckWeight);
                    sum += truckWeight;
                    seconds++;
                    break;
                } else if (queue.size() == bridge_length) {
                    sum -= queue.poll();
                } else {
                    if (sum + truckWeight <= weight) {
                        queue.offer(truckWeight);
                        sum += truckWeight;
                        seconds++;
                        break;
                    } else {
                        queue.offer(0);
                        seconds++;
                    }
                }
            }
        }
        return seconds + bridge_length;
    }
}
