package programmers.kakao.kakao_blind_recruitment_2023;

public class 택배배달과수거하기1 {

    public static void main(String[] args) {
        int[] deliveries = {1, 0, 3, 1, 2};
        int[] pickups = {0, 3, 0, 4, 0};
        System.out.println(solution(4, 5, deliveries, pickups));

        int[] deliveries1 = {1, 0, 2, 0, 1, 0, 2};
        int[] pickups1 = {0, 2, 0, 1, 0, 2, 0};
        System.out.println(solution(2, 7, deliveries1, pickups1));
    }

    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {

        int maxDistance = 0;
        int deliveryIndex = n - 1;
        int pickupIndex= n - 1;
        while (deliveryIndex >= 0 || pickupIndex >= 0) {
            int load = 0;
            int distance = 0;

            // 배달
            while (deliveryIndex >= 0 && load < cap) {
                if (deliveries[deliveryIndex] > 0) {
                    int canDeliver = Math.min(cap - load, deliveries[deliveryIndex]);
                    deliveries[deliveryIndex] -= canDeliver;
                    load += canDeliver;
                    distance = Math.max(distance, deliveryIndex + 1);
                } else {
                    deliveryIndex--;
                }
            }

            // 수거
            load = 0;
            while (pickupIndex >= 0 && load < cap) {
                if (pickups[pickupIndex] > 0) {
                    int canPickup = Math.min(cap - load, pickups[pickupIndex]);
                    pickups[pickupIndex] -= canPickup;
                    load += canPickup;
                    distance = Math.max(distance, pickupIndex + 1);
                } else {
                    pickupIndex--;
                }
            }

            maxDistance += distance * 2;
        }

        return maxDistance;
    }
}
