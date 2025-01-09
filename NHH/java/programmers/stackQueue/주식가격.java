package programmers.stackQueue;

import java.util.Arrays;
import java.util.Stack;

public class 주식가격 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1,2,3,2,3})));
    }

    public static int[] solution(int[] prices) {
        int[] answers = new int[prices.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[i] < prices[stack.peek()]) {
                int index = stack.pop();
                answers[index] = i - index;
            }
            stack.push(i);
        }

        while (!stack.isEmpty()) {
            int index = stack.pop();
            answers[index] = prices.length - 1 - index;
        }
        return answers;
    }
}
