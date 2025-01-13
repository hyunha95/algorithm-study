package programmers.kakao.kakao_blind_recruitment_2022;

import java.util.Arrays;
import java.util.stream.IntStream;

public class K진수에서소수개수구하기 {

    public static void main(String[] args) {
        System.out.println(solution(437674, 3));
        System.out.println(solution(110011, 10));
        System.out.println(solution(883438, 3)); // output 0
    }

    public static int solution(int n, int k) {
        String strNum = Integer.toString(n, k);

        return (int) Arrays.stream(strNum.split("0"))
                .filter(str -> !str.isEmpty() && isPrime(Double.parseDouble(str)))
                .count();
    }

    public static boolean isPrime(double n) {
        if (n <= 1) return false;
        return IntStream.rangeClosed(2, (int) Math.sqrt(n))
                .noneMatch(i -> n % i == 0);
    }
}
