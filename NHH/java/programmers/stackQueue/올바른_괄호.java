package programmers.stackQueue;

import java.util.LinkedList;
import java.util.Queue;

public class 올바른_괄호 {

    public static void main(String[] args) {
        System.out.println(solution("()()"));
        System.out.println(solution("(())()"));
        System.out.println(solution(")()("));
        System.out.println(solution("(()("));
    }

    static boolean solution(String s) {
        boolean answer = true;

        Queue<Character> queue = new LinkedList<>();
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                queue.add(ch);
            } else {
                if (queue.isEmpty()) {
                    return false;
                }

                queue.poll();
            }
        }

        if (!queue.isEmpty()) {
            return false;
        }

        return answer;
    }
}
