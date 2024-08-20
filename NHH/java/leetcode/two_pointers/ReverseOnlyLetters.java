package leetcode.two_pointers;

public class ReverseOnlyLetters {

    public static void main(String[] args) {

//        System.out.println(reverseOnlyLetters("ab-cd"));
//        System.out.println(reverseOnlyLetters("a-bC-dEf-ghIj"));
//        System.out.println(reverseOnlyLetters("Test1ng-Leet=code-Q!"));
//        System.out.println(reverseOnlyLetters("Czyr^"));
//        System.out.println(reverseOnlyLetters("Czyr^").equals("ryzC^"));
        System.out.println(reverseOnlyLetters("7_28]"));
        System.out.println(reverseOnlyLetters("7_28]").equals("7_28]"));
    }

    public static String reverseOnlyLetters(String s) {

        char[] charArray = s.toCharArray();

        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (!Character.isLetter(s.charAt(left))) {
                left++;
                continue;
            }
            if (!Character.isLetter(s.charAt(right))) {
                right--;
                continue;
            }

            swap(charArray, left, right);
            left++;
            right--;
        }

        return new String(charArray);
    }

    public static void swap(char[] chars, int currPointer, int lastPointer) {
        char temp = chars[currPointer];
        chars[currPointer] = chars[lastPointer];
        chars[lastPointer] = temp;
    }
}
