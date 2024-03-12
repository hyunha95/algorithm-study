package leetcode.easy;

public class RomanToInteger {
    public static void main(String[] args) {
        System.out.println(romanToInt("III"));
        System.out.println(romanToInt("LVIII"));
        System.out.println(romanToInt("MCMXCIV"));
    }

    public static int romanToInt(String s) {
        int prev = 0;
        int answer = 0;
        for (char ch : s.toCharArray()) {
            int curr = getInt(ch);
            answer += curr;
            if (prev < curr) {
                answer -= prev * 2;
            }
            prev = curr;
        }
        return answer;
    }

    public static int getInt(char ch) {
        switch (ch) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            default: return 1000;
        }
    }
}
