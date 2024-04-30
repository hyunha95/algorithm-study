package leetcode.two_pointers;

import java.util.Arrays;

public class FlippingAnImage {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(flipAndInvertImage(new int[][] {{1,1,0},{1,0,1},{0,0,0}})));
    }

    public static int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            reverse(row);
            invert(row);
        }
        return image;
    }

    private static void reverse(int[] row) {
        int start = 0;
        int end = row.length - 1;
        while (start < end) {
            swap(row, start, end);
            start++;
            end--;
        }
    }

    private static void swap(int[] row, int i, int j) {
        int temp = row[i];
        row[i] = row[j];
        row[j] = temp;
    }

    private static void invert(int[] row) {
        for (int i = 0; i < row.length; i++) {
            row[i] = invert(row[i]);
        }
    }

    private static int invert(int num) {
        return num == 0 ? 1 : 0;
    }
}
