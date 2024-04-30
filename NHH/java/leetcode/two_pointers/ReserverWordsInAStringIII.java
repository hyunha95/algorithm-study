package leetcode.two_pointers;

import java.util.Arrays;
import java.util.stream.Collectors;

public class ReserverWordsInAStringIII {

    public static void main(String[] args) {
        System.out.println(reverseWords("Let's take LeetCode contest"));
        System.out.println(reverseWords("Mr Ding"));
        System.out.println(reverseWords2("Let's take LeetCode contest"));
        System.out.println(reverseWords2("Mr Ding"));
    }

    public static String reverseWords2(String s) {
        String[] strings = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String string : strings) {
            sb.append(new StringBuilder(string).reverse());
            sb.append(" ");
        }

        return sb.toString().trim();
    }

    public static String reverseWords(String s) {
        String[] strings = s.split(" ");
        String[] newStrings = new String[strings.length];
        for (int i = 0; i < strings.length; i++) {
            newStrings[i] = reverseWord(strings[i]);
        }
        return Arrays.stream(newStrings).collect(Collectors.joining(" "));
    }

    private static String reverseWord(String string) {
        char[] charArray = string.toCharArray();
        reverse(charArray);
        return new String(charArray);
    }

    private static void reverse(char[] charArray) {
        int start = 0;
        int end = charArray.length - 1;
        while (start < end) {
            swap(charArray, start, end);
            start++;
            end--;
        }
    }

    private static void swap(char[] chars, int i, int j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
    }

}
