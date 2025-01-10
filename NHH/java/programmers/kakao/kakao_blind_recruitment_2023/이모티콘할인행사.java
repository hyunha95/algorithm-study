package programmers.kakao.kakao_blind_recruitment_2023;

import java.util.Arrays;

/**
 * https://lift-ing.tistory.com/250
 */
public class 이모티콘할인행사 {

    public static void main(String[] args) {
        int[][] users = {{40, 10000}, {25, 10000}};
        int[] emoticons = {7000, 9000};
        System.out.println(Arrays.toString(solution(users, emoticons)));
    }

    public static int[] solution(int[][] users, int[] emoticons) {
        // 이모티콘별 할인율 배열
        int[] saleRate = new int[emoticons.length];
        // 이모티콘 할인율 경우의 수
        int saleRateCase = (int) Math.pow(4, emoticons.length);
        int join = 0; // 가입자수
        int sum = 0; // 매출액

        for (int i = 0; i < saleRateCase; i++) {
            // 이모티콘별 할인율 계산
            for (int j = 0; j < saleRate.length; j++) {
                saleRate[j] = 10 * (1 + (i / (int) Math.pow(4, j)) % 4);
            }
            int userJoin = 0;
            int userSums = 0;

            for (int j = 0; j < users.length; j++) {
                int userSum = 0; // 유저금액 합계
                int userRate = users[j][0];
                for (int k = 0; k < saleRate.length; k++) {
                    if (saleRate[k] >= userRate) {
                        userSum += emoticons[k] * (100 - saleRate[k]) / 100;
                    }
                }
                if (userSum >= users[j][1]) {
                    userJoin++;
                } else {
                    userSums += userSum;
                }
            }
            if (userJoin == join) {
                // 가입자 수가 동일한 여러 조합 중에서 매출액이 가장 큰 것을 선택.
                join = userJoin;
                sum = Math.max(sum, userSums);
            } else if (userJoin > join) {
                join = userJoin;
                sum = userSums;
            }
        }

        int[] answer = {join, sum};
        return answer;
    }

}
