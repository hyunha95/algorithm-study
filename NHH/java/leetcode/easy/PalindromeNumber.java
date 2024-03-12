package leetcode.easy;
public class PalindromeNumber {

    public static void main(String[] args) {
        System.out.println(isPalindrome(1234567899));
    }

    /**
     * 스트링으로 변환
     */
    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        char[] charArray = String.valueOf(x).toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            if (charArray[i] != charArray[charArray.length-1-i]) {
                return false;
            }
        }

        return true;
    }

}
