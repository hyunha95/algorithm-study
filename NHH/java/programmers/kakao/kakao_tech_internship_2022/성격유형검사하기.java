package programmers.kakao.kakao_tech_internship_2022;

import java.util.HashMap;
import java.util.Map;

public class 성격유형검사하기 {
    public static void main(String[] args) {
        String[] survey = {"AN", "CF", "MJ", "RT", "NA"};
        int[] choices = {5, 3, 2, 7, 5};
        System.out.println(solution(survey, choices));

        String[] survey1 = {"TR", "RT", "TR"};
        int[] choices1 = {7, 1, 3};
        System.out.println(solution(survey1, choices1));
    }

    public static String solution(String[] survey, int[] choices) {
        Map<Character, Integer> map = new HashMap<>(Map.of(
                'R', 0, 'T', 0,
                'C', 0, 'F', 0,
                'J', 0, 'M', 0,
                'A', 0, 'N', 0
        ));

        Map<Integer, Integer> scores = Map.of(
                1, 3,
                2, 2,
                3, 1,
                4, 0,
                5, 1,
                6, 2,
                7, 3
        );

        for (int i = 0; i < choices.length; i++) {
            char first = survey[i].split("")[0].charAt(0);
            char second = survey[i].split("")[1].charAt(0);

            int choice = choices[i];

            if (choice < 4) {
                map.put(first, map.get(first) + scores.get(choice));
            } else {
                map.put(second, map.get(second) + scores.get(choice));
            }
        }

        StringBuilder sb = new StringBuilder();
        if (map.get('R') >= map.get('T')) {
            sb.append("R");
        } else {
            sb.append("T");
        }

        if (map.get('C') >= map.get('F')) {
            sb.append("C");
        } else {
            sb.append("F");
        }

        if (map.get('J') >= map.get('M')) {
            sb.append("J");
        } else {
            sb.append("M");
        }

        if (map.get('A') >= map.get('N')) {
            sb.append("A");
        } else {
            sb.append("N");
        }

        return sb.toString();
    }
}
