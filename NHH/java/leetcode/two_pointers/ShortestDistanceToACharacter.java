package leetcode.two_pointers;

import java.util.Arrays;

public class ShortestDistanceToACharacter {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(shortestToChar2("loveleetcode", 'e')));
    }

    public static int[] shortestToChar2(String s, char c) {
        int n = s.length();
        int i = 0;
        int position = -n;
        int[] dist = new int[n];

        for(char ch : s.toCharArray()) {
            if (c == ch) position = i;
            dist[i] = i - position;
            i++;
        }
        for (int j = n - 1; j >= 0; j--) {
            if (c == s.charAt(j)) position = j;
            dist[j] = Math.min(dist[j], Math.abs(j - position));
        }
        return dist;
    }

    public static int[] shortestToChar(String s, char c) {

        int[] answers = new int[s.length()];

        for (int i = 0; i < s.length(); i++) {
            if (c == s.charAt(i)) {
                continue;
            }

            String left = s.substring(0, i + 1);
            String right = s.substring(i + 1);

            int min = Integer.MAX_VALUE;

            for (int j = left.length() - 1; j >= 0; j--) {
                if (c == left.charAt(j)) {
                    min = Math.min(Math.abs(i - j), min);
                    break;
                }
            }

            for (int j = 0; j < right.length(); j++) {
                if (c == right.charAt(j)) {
                    min = Math.min(Math.abs(j + 1), min);
                    break;
                }
            }


            answers[i] = Integer.MAX_VALUE == min ? 0 : min;
        }

        return answers;
    }
}
