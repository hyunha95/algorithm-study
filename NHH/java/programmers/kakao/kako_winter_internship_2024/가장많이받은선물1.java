package programmers.kakao.kako_winter_internship_2024;

import java.util.Arrays;

public class 가장많이받은선물1 {

    public static void main(String[] args) {
        String[] friends = {"muzi", "ryan", "frodo", "neo"};
        String[] gifts = {"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"};
        System.out.println(solution(friends, gifts));

        String[] friends1 = {"joy", "brad", "alessandro", "conan", "david"};
        String[] gifts1 = {"alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"};
        System.out.println(solution(friends1, gifts1));

        String[] friends2 = {"a", "b", "c"};
        String[] gifts2 = {"a b", "b a", "c a", "a c", "a c", "c a"};
        System.out.println(solution(friends2, gifts2));
    }

    public static int solution(String[] friends, String[] gifts) {
        int[][] giftCounts = new int[friends.length][friends.length];
        int[] giftIndex = new int[friends.length];

        int maxGiftCount = 0;

        // 선물 개수
        for (int i = 0; i < friends.length ; i++) {
            for (int j = 0; j < friends.length; j++) {
                String temp = friends[i] + " " + friends[j];
                for (String gift : gifts) {
                    if (temp.equals(gift)) {
                        giftCounts[i][j]++;
                    }
                }
            }
        }

        // 선물 지수
        for (int i = 0; i < friends.length; i++) {
            for (String gift : gifts) {
                String giver = gift.split(" ")[0];
                String receiver = gift.split(" ")[1];

                if (friends[i].equals(giver)) {
                    giftIndex[i]++;
                }

                if (friends[i].equals(receiver)) {
                    giftIndex[i]--;
                }
            }
        }

        // 선물 계산
        for (int i = 0; i < friends.length; i++) {
            int giftCount = 0;
            for (int j = 0; j < friends.length; j++) {

                if (giftCounts[i][j] > giftCounts[j][i]) {
                    giftCount++;
                } else if (giftCounts[i][j] == giftCounts[j][i]) {
                    if (giftIndex[i] > giftIndex[j]) {
                        giftCount++;
                    }
                }
            }
            maxGiftCount = Math.max(maxGiftCount, giftCount);
        }
        return maxGiftCount;
    }
}
