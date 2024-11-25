package leetcode.two_pointers;

public class LongestPalindromicSubstring {

    public static void main(String[] args) {
        System.out.println(longestPalindrome("babad"));
        System.out.println(longestPalindrome("cbbd"));
        System.out.println(longestPalindrome("a"));
        System.out.println(longestPalindrome("bb"));
    }

    public static String longestPalindrome(String s) {

        if (s.length() == 1) {
            return s;
        }
        String answer = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length() + 1; j++) {
                String word = s.substring(i, j);
                if (isPalindrome(word)) {
                    if (answer.length() < word.length()) {
                        answer = word;
                    }
                }
            }
        }

        return answer;
    }

    public static boolean isPalindrome(String s) {
        if (s == null || s.isBlank()) {
            return false;
        }

        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
