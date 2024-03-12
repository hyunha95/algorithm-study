package leetcode.easy;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.stream.Collectors;

public class PlusOne {

    public static void main(String[] args) {
        System.out.println(plusOne(new int[]{1,2,3}));
        System.out.println(plusOne(new int[]{4,3,2,1}));
        System.out.println(plusOne(new int[]{9}));
    }

    public static int[] plusOne(int[] digits) {
        String digit = Arrays.stream(digits)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining());

        BigInteger result = new BigInteger(digit).add(BigInteger.ONE);

        return Arrays.stream(String.valueOf(result).split(""))
                .mapToInt(Integer::valueOf)
                .toArray();
    }

    public static int[] plusOneV2(int[] digits) {
        for (int i = digits.length - 1; i >= 0 ; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
