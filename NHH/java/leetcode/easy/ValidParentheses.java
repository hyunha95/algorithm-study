package leetcode.easy;

import java.util.Stack;

public class ValidParentheses {

    public static void main(String[] args) {
//        System.out.println(isValid("()"));
//        System.out.println(isValid("()[]{}"));
//        System.out.println(isValid("(]"));
//        System.out.println(isValid("{[]}")); // true
//        System.out.println(isValid("){")); // false
//        System.out.println(isValid("(){}}{")); // false
        System.out.println(isValid("(([]){})")); // true
    }

    public static boolean isValid(String s) {
        if (s.length() % 2 == 1) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == ')' || ch == '}' || ch == ']') {
                if (stack.isEmpty()) {
                    return false;
                }

                char pop = stack.pop();
                if (ch == ')' && pop != '(') {
                    return false;
                } else if (ch == '}' && pop != '{') {
                    return false;
                } else if ( ch == ']' && pop != '[') {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }

        if (!stack.isEmpty()) {
            return false;
        }

        return true;
    }

}
