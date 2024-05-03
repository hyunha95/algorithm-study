package leetcode.two_pointers;

public class MergeStringsAlternately {

    public static void main(String[] args) {
        System.out.println(mergeAlternately("abc", "pqr"));
        System.out.println(mergeAlternately("ab", "pqrs"));
        System.out.println(mergeAlternately("abcd", "pq"));
    }

    public static String mergeAlternately(String word1, String word2) {
        char[] chars = new char[word1.length() + word2.length()];

        int i = 0;
        int j = 0;
        int k = 0;
        while (i < word1.length() && j < word2.length()) {
            chars[k++] = word1.charAt(i++);
            chars[k++] = word2.charAt(j++);
        }

        while (i < word1.length()) {
            chars[k++] = word1.charAt(i++);
        }

        while (j < word2.length()) {
            chars[k++] = word2.charAt(j++);
        }

        return new String(chars);
    }
}
