package programmers.kakao.kakao_blind_recruitment_2022;

import java.util.*;
import java.util.stream.Collectors;

public class 신고결과받기 {

    public static void main(String[] args) {
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        System.out.println(Arrays.toString(solution(id_list, report, 2)));

        String[] id_list1 = {"con", "ryan"};
        String[] report1 = {"ryan con", "ryan con", "ryan con", "ryan con"};
        System.out.println(Arrays.toString(solution(id_list1, report1, 3)));
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<String>> map = new HashMap<>();
        for (String id : id_list) {
            map.put(id, new HashSet<>());
        }

        for (String temp : report) {
            String from = temp.split(" ")[0];
            String to = temp.split(" ")[1];
            map.get(from).add(to);
        }

        Map<String, Integer> reportedUsers = new HashMap<>();
        for (String id : map.keySet()) {
            for (String reportedUserByMe : map.get(id)) {
                reportedUsers.put(reportedUserByMe, reportedUsers.getOrDefault(reportedUserByMe,0) + 1);
            }
        }

        Set<String> blockedIds = reportedUsers.entrySet().stream()
                .filter(entry -> entry.getValue() >= k)
                .map(Map.Entry::getKey)
                .collect(Collectors.toSet());

        int[] answers = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            for (String reportedUserId : map.get(id_list[i])) {
                if (blockedIds.contains(reportedUserId)) {
                    answers[i]++;
                }
            }
        }

        return answers;
    }
}
