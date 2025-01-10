package programmers.kakao.kakao_blind_recruitment_2023;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class 개인정보수집유효기간 {

    static DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy.MM.dd");

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution("2022.05.19", new String[] {"A 6", "B 12", "C 3"}, new String[] {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"})));
        System.out.println(Arrays.toString(solution("2020.01.01", new String[] {"Z 3", "D 5"}, new String[] {"2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"})));
    }

    public static int[] solution(String today, String[] terms, String[] privacies) {

        LocalDate now = LocalDate.parse(today, formatter);
        Map<String, Integer> map = new HashMap<>();
        for (String temp : terms) {
            String term = temp.split(" ")[0];
            int month = Integer.parseInt(temp.split(" ")[1]);
            map.put(term, month);
        }

        List<Integer> answers = new ArrayList<>();
        for (int i = 0; i < privacies.length; i++) {
            String temp = privacies[i];
            LocalDate registeredDate = LocalDate.parse(temp.split(" ")[0], formatter);
            String term = temp.split(" ")[1];

            int month = map.get(term);
            LocalDate expireAt = registeredDate.plusMonths(month);

            if (expireAt.isEqual(now) || expireAt.isBefore(now)) {
                answers.add(i + 1);
            }
        }

        return answers.stream().mapToInt(Integer::valueOf).toArray();
    }
}
