package programmers.hash;

import java.util.HashMap;
import java.util.Map;

public class 의상 {

    public static void main(String[] args) {
        System.out.println(solution(new String[][]{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}}));
        System.out.println(solution(new String[][]{{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}}));
    }

    public static int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();

        for (String[] clothe : clothes) {
            if (map.containsKey(clothe[1])) {
                map.put(clothe[1], map.get(clothe[1]) + 1);
            } else {
                map.put(clothe[1], 1);
            }
        }

        // 경우의 수를 수식으로 작성한다.
        // 기본적으로 N x M이 경우의 수이다.
        // 안입는 경우를 +1로 계산한다. (N+1) x (M+1)
        // 모두 안입는 경우는 없으므로, -1 해줘야 조건에 만족하는 경우의 수를 구할 수 있다
        // 수식 = (N+1) x (M+1) - 1
        int answer = 1;
        for (String key : map.keySet()) {
            answer *= map.get(key) + 1;
        }
        return answer - 1;
    }
}
