package programmers.kakao.kako_winter_internship_2024;

public class 가장많이받은선물 {

    public static void main(String[] args) {
        System.out.println(solution(new String[]{"muzi", "ryan", "frodo", "neo"}, new String[]{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"}));
        System.out.println(solution(new String[]{"joy", "brad", "alessandro", "conan", "david"}, new String[]{"alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"}));
    }

    public static int solution(String[] friends, String[] gifts) {
        int[][] giftCount = new int[friends.length][friends.length];
        int[] giftIndex = new int[friends.length];

        // 선물 개수
        for (int i = 0; i < friends.length; i++) {
            for (int j = 0; j < friends.length; j++) {
                String gift = friends[i] + " " + friends[j];
                for (String temp : gifts) {
                    if (gift.equals(temp)) {
                        giftCount[i][j]++;
                    }
                }
            }
        }

        // 선물 지수
        for (int i = 0; i < friends.length; i++) {
            for (String temp : gifts) {
                String giver = temp.split(" ")[0];
                String receiver = temp.split(" ")[1];

                if (giver.equals(friends[i])) {
                    giftIndex[i]++;
                }

                if (receiver.equals(friends[i])) {
                    giftIndex[i]--;
                }
            }
        }

        // 선물 계산
        int max = 0;
        for (int i = 0; i < friends.length; i++) {
            int giftCnt = 0;
            for (int j = 0; j < friends.length; j++) {
                if (i == j) continue;

                // 선물을 주고받은 기록이 없거나 주고받은 수가 같다면
                if (giftCount[i][j] == giftCount[j][i]) {
                    // 선물 지수가 더 큰사람이 선물을 받는다.
                    if (giftIndex[i] > giftIndex[j]) {
                        giftCnt++;
                    }
                } else {
                    if (giftCount[i][j] > giftCount[j][j]) {
                        giftCnt++;
                    }
                }
            }

            if (max < giftCnt) {
                max = giftCnt;
            }
        }

        return max;
    }
}
